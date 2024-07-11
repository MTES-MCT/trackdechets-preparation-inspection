from django.contrib import admin
from django.urls import reverse_lazy
from django.utils.html import format_html

from .models import ComputedInspectionData, RegistryDownload


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
    list_filter = ["created", "creation_mode"]
    search_fields = ["org_id"]

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


@admin.register(RegistryDownload)
class RegistryDownloadAdmin(admin.ModelAdmin):
    list_display = ["id", "org_id", "created", "created_by"]
    list_filter = ["created"]
    search_fields = ["org_id"]
