import datetime as dt
import logging

import httpx
from celery import chain
from django.conf import settings
from django.utils import timezone

from config.celery_app import app

from .constants import RegistryV2ExportState
from .gql import graphql_generate_registry_export, graphql_read_registry_export
from .models import RegistryV2Export

logger = logging.getLogger(__name__)


def process_export(registry_v2_export_pk):
    if getattr(settings, "CELERY_TASK_ALWAYS_EAGER", False):
        # for testing purposes
        generate_registry_export.delay(registry_v2_export_pk)
        return

    task_chain = chain(generate_registry_export.s(registry_v2_export_pk), refresh_registry_export.s())
    task_chain()


MAX__GENERATE_DELAY = dt.timedelta(minutes=15)


@app.task(bind=True)
def generate_registry_export(self, registry_v2_export_pk):
    """Create a registry export on TD api"""
    geo_retry_delay = min(10 * self.request.retries, 300)
    export = RegistryV2Export.objects.get(pk=registry_v2_export_pk)

    # Distant export ID already retrieved
    if export.registry_export_id:
        return registry_v2_export_pk

    now = timezone.now()
    if now - export.created_at > MAX__GENERATE_DELAY:
        logger.info("Max delay reached")
        export.mark_as_failed()
        return None

    client = httpx.Client(timeout=60)  # 60 seconds
    variables = export.get_gql_variables()

    try:
        res = client.post(
            url=settings.TD_API_URL,
            headers={"Authorization": f"Bearer {settings.TD_API_TOKEN}"},
            json={
                "query": graphql_generate_registry_export,
                "variables": variables,
            },
        )
    except httpx.RequestError:
        logger.info("HTTP error")
        raise self.retry(countdown=geo_retry_delay)

    resp = res.json()

    try:
        registry_export_id = resp["data"]["generateRegistryV2Export"]["id"]
        status = resp["data"]["generateRegistryV2Export"]["status"]
    except (TypeError, KeyError):
        logger.info("Api response error")
        raise self.retry(countdown=geo_retry_delay)

    export.registry_export_id = registry_export_id
    export.state = status
    export.save()

    return registry_v2_export_pk


MAX__REFRESH_DELAY = dt.timedelta(minutes=15)


@app.task(bind=True, max_retries=None)
def refresh_registry_export(self, registry_v2_export_pk):
    static_retry_delay = 10
    geo_retry_delay = min(10 * self.request.retries, 300)

    try:
        export = RegistryV2Export.objects.get(pk=registry_v2_export_pk)
    except RegistryV2Export.DoesNotExist:
        if self.request.retries < 3:
            # retry 2 times with a 1s delay
            raise self.retry(countdown=1)
        # really does not exist, exit
        return None

    if export.state in [
        RegistryV2ExportState.CANCELED,
        RegistryV2ExportState.SUCCESSFUL,
        RegistryV2ExportState.SUCCESSFUL,
    ]:
        return None

    now = timezone.now()
    if now - export.created_at > MAX__REFRESH_DELAY:
        logger.info("Max delay reached")
        export.mark_as_failed()
        return None

    client = httpx.Client(timeout=10)  # 10 seconds

    try:
        res = client.post(
            url=settings.TD_API_URL,
            headers={"Authorization": f"Bearer {settings.TD_API_TOKEN}"},
            json={
                "query": graphql_read_registry_export,
                "variables": {
                    "id": export.registry_export_id,
                },
            },
        )
    except httpx.RequestError:
        # http error, geometric retry delay
        logger.info("HTTP error")
        raise self.retry(countdown=geo_retry_delay)

    if res.status_code == 200:
        resp = res.json()
        try:
            registry_export_state = resp["data"]["registryV2Export"]["status"]

        except (TypeError, KeyError):
            logger.info("Api error")
            raise self.retry(countdown=static_retry_delay)
        if registry_export_state not in [RegistryV2ExportState.PENDING, RegistryV2ExportState.STARTED]:
            export.state = registry_export_state
            export.save()
            return None
        else:
            # Registry not ready yet, retry after static_retry_delay
            logger.info("registry not ready")
            raise self.retry(countdown=static_retry_delay)

    else:
        # Api error, geometric retry delay
        logger.info("Api error")
        raise self.retry(countdown=geo_retry_delay)
