from django.contrib import admin

from .models import ComputedInspectionData


@admin.register(ComputedInspectionData)
class ComputedInspectionDataAdmin(admin.ModelAdmin):
    list_display = ["id", "org_id", "created"]
