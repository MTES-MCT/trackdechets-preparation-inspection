import logging

import httpx
from django.conf import settings

from config.celery_app import app
from sheets.models import PROCESSED
from sheets.rendering_helpers import prepare_sheet_fn, render_pdf_fn, render_pdf_graph_fn

logger = logging.getLogger(__name__)


@app.task(queue=settings.API_QUEUE)
def render_indiv_graph_api(computed_pk, name):
    render_pdf_graph_fn(computed_pk, name)
    return True


@app.task(queue=settings.API_QUEUE)
def prepare_sheet_api(computed_pk):
    prepare_sheet_fn(computed_pk)

    render_pdf_fn(computed_pk, render_indiv_graph_api)
    return computed_pk


@app.task(bind=True, queue=settings.API_QUEUE, default_retry_delay=3, max_retries=5)
def send_webhook(self, computed_pk):
    """
    Pollable task to prepare html view.

    :param computed_pk: ComputedInspectionData pk
    """

    client = httpx.Client(timeout=10)

    try:
        print(f"Try {self.request.retries}/{self.max_retries}")

        resp = client.post(
            url=settings.TD_WEBHOOK_URL,
            headers={"Authorization": f"Token {settings.TD_WEBHOOK_TOKEN}"},
            json={"distantId": str(computed_pk), "status": PROCESSED},
        )

        resp.raise_for_status()
    except httpx.HTTPError as exc:
        raise self.retry(exc=exc)
