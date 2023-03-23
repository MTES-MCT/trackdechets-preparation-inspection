from django.contrib import admin
from django.urls import reverse_lazy
from django.utils.html import format_html

from .models import ComputedInspectionData


@admin.register(ComputedInspectionData)
class ComputedInspectionDataAdmin(admin.ModelAdmin):
    list_display = ["id", "org_id", "created", "get_render", "state", "created_by"]
    list_filter = ["created"]
    search_fields = ["org_id"]

    def get_render(self, obj):
        if obj.state in [
            ComputedInspectionData.StateChoice.INITIAL,
            ComputedInspectionData.StateChoice.COMPUTED_FAILED,
        ]:
            return None
        url = reverse_lazy("sheet", args=[obj.pk])
        return format_html("<a href='{}' _target='blank'>Voir</a>", url)

    get_render.short_description = "Rendu"
