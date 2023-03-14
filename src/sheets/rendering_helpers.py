from django.db import transaction
from django.shortcuts import get_object_or_404

from .constants import ALLOWED_NAMES
from .models import ComputedInspectionData
from .plotly_utils import data_to_bs64_plot


def render_pdf_graph_fn(computed_pk, name):
    """Render a plolty png to base64 from stored precomputed data"""
    if name not in ALLOWED_NAMES:
        raise Exception("Invalid argument")

    with transaction.atomic():
        computed = get_object_or_404(
            ComputedInspectionData.objects.select_for_update(), pk=computed_pk
        )
        if not computed.is_computed:
            return
        graph = data_to_bs64_plot(getattr(computed, f"{name}_data"))
        setattr(computed, f"{name}_graph", graph)

        computed.save()
