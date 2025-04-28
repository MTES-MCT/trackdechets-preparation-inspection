from django.contrib import admin

from .models import RegistryDownload, RegistryV2Export


@admin.register(RegistryDownload)
class RegistryDownloadAdmin(admin.ModelAdmin):
    list_display = ["id", "org_id", "created", "created_by"]
    list_filter = ["created"]
    search_fields = ["org_id"]


@admin.register(RegistryV2Export)
class RegistryV2ExportAdmin(admin.ModelAdmin):
    list_display = ["id", "siret", "state", "created_at", "created_by", "registry_type", "start_date", "end_date"]
    list_filter = ["registry_type"]
    search_fields = ["siret"]
    list_select_related = ["created_by"]
