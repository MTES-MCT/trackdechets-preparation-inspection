from django.contrib import admin
from django.urls import reverse_lazy
from django.utils.html import format_html
from rangefilter.filters import DateRangeFilterBuilder

from .models import ComputedInspectionData


@admin.register(ComputedInspectionData)
class ComputedInspectionDataAdmin(admin.ModelAdmin):
    list_display = [
        "id",
        "org_id",
        "company_name",
        "created",
        "get_render",
        "state",
        "data_start_date",
        "data_end_date",
        "creation_mode",
        "created_by",
        "processing_duration",
        "pdf_rendering_duration",
    ]
    list_filter = (("created", DateRangeFilterBuilder()), "creation_mode")
    search_fields = ["id", "org_id"]

    def get_queryset(self, request):
        # Don't load heavy unused fields
        return (
            super()
            .get_queryset(request)
            .only(
                "id",
                "org_id",
                "company_name",
                "created",
                "state",
                "data_start_date",
                "data_end_date",
                "creation_mode",
                "created_by",
                "processing_end",
                "processing_start",
                "pdf_rendering_end",
                "pdf_rendering_start",
            )
        )

    @admin.display(description="Rendu")
    def get_render(self, obj):
        if obj.state in [
            ComputedInspectionData.StateChoice.INITIAL,
            ComputedInspectionData.StateChoice.COMPUTED_FAILED,
        ]:
            return None
        url = reverse_lazy("sheet", args=[obj.pk])
        return format_html("<a href='{}' _target='blank'>Voir</a>", url)
