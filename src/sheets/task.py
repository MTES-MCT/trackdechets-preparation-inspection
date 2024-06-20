import logging

from django.conf import settings

from config.celery_app import app

from .rendering_helpers import prepare_sheet_fn, render_pdf_fn, render_pdf_graph_fn

logger = logging.getLogger(__name__)


@app.task(queue=settings.WEB_QUEUE)
def render_indiv_graph(computed_pk, name):
    render_pdf_graph_fn(computed_pk, name)
    return True


@app.task(queue=settings.WEB_QUEUE)
def prepare_sheet(computed_pk):
    """
    Pollable task to prepare html view.

    :param computed_pk: ComputedInspectionData pk
    """
    return prepare_sheet_fn(computed_pk)


@app.task(queue=settings.WEB_QUEUE)
def render_pdf(computed_pk: str):
    return render_pdf_fn(computed_pk, render_indiv_graph)
