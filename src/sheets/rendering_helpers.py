from django.db import transaction
from django.shortcuts import get_object_or_404

from .constants import PLOTLY_GRAPHS_TO_RENDER_IN_PDF
from .models import ComputedInspectionData
from .plotly_utils import data_to_bs64_plot


def render_pdf_graph_fn(computed_pk, name):
    """Render a plolty png to base64 from stored precomputed data"""
    if name not in PLOTLY_GRAPHS_TO_RENDER_IN_PDF:
        raise Exception("Invalid argument")

    with transaction.atomic():
        computed = get_object_or_404(ComputedInspectionData.objects.select_for_update(), pk=computed_pk)
        if not computed.is_computed:
            return
        graph_data = getattr(computed, f"{name}_data")
        graph = ""
        if graph_data is not None and graph_data != "{}":
            graph = data_to_bs64_plot(graph_data)
        name = f"{name}_graph" if "_graph" not in name else name
        setattr(computed, name, graph)

        computed.save()
