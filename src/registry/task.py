import logging

import httpx
from django.conf import settings

from config.celery_app import app

from .gql import graphql_generate_registry_export, graphql_read_registry_export
from .models import RegistryV2Export

logger = logging.getLogger(__name__)


@app.task(queue=settings.API_QUEUE)
def generate_registry_export(registry_v2_export_pk):
    export = RegistryV2Export.objects.get(pk=registry_v2_export_pk)
    client = httpx.Client(timeout=60)  # 60 seconds

    res = client.post(
        url=settings.TD_API_URL,
        headers={"Authorization": f"Bearer {settings.TD_API_TOKEN}"},
        json={
            "query": graphql_generate_registry_export,
            "variables": {
                "siret": export.siret,
                "registryType": export.registry_type,
                "format": export.export_format,
                "dateRange": {"_gte": export.start_date.isoformat(), "_lte": export.start_date.isoformat()},
            },
        },
    )
    resp = res.json()

    try:
        registry_export_id = resp["data"]["generateRegistryV2Export"]["id"]
        status = resp["data"]["generateRegistryV2Export"]["status"]
    except (TypeError, KeyError):
        return

    export.registry_export_id = registry_export_id
    export.state = status
    export.save()


@app.task(queue=settings.API_QUEUE)
def refresh_registry_export(registry_v2_export_pk):
    export = RegistryV2Export.objects.get(pk=registry_v2_export_pk)
    client = httpx.Client(timeout=60)  # 60 seconds

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
    resp = res.json()

    try:
        registry_export_state = resp["data"]["registryV2Export"]["status"]

    except (TypeError, KeyError):
        return
    export.state = registry_export_state
    export.save()
