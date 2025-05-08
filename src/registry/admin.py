from django.contrib import admin

from .models import RegistryDownload, RegistryV2Export
from .task import process_export


@admin.register(RegistryDownload)
class RegistryDownloadAdmin(admin.ModelAdmin):
    list_display = ["id", "org_id", "created", "created_by"]
    list_filter = ["created"]
    search_fields = ["org_id"]


@admin.register(RegistryV2Export)
class RegistryV2ExportAdmin(admin.ModelAdmin):
    list_display = [
        "id",
        "siret",
        "state",
        "export_format",
        "created_at",
        "registry_type",
        "start_date",
        "end_date",
        "registry_export_id",
    ]
    list_filter = ["registry_type", "export_format", "state"]
    search_fields = ["siret"]
    list_select_related = ["created_by"]
    actions = [
        "action_update_export",
    ]

    @admin.action(description="Refresh registry states by checking Trackdéchets api")
    def action_update_export(self, request, queryset):
        for obj in queryset:
            process_export(obj.pk)
