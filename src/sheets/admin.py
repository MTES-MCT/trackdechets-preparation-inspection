from django.contrib import admin
from django.urls import reverse_lazy
from django.utils.html import format_html

from .models import ComputedInspectionData


@admin.register(ComputedInspectionData)
class ComputedInspectionDataAdmin(admin.ModelAdmin):
    list_display = ["id", "org_id", "created", "get_render", "state"]

    def get_render(self, obj):
        url = reverse_lazy("sheet", args=[obj.pk])
        return format_html("<a href='{}' _target='blank'>Voir</a>", url)

    get_render.short_description = "Rendu"
