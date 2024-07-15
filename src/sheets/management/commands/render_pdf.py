from django.core.management.base import BaseCommand

from ...models import ComputedInspectionData
from ...rendering_helpers import render_pdf_sheet_fn


class Command(BaseCommand):
    def handle(self, verbosity=0, **kwargs):
        obj = ComputedInspectionData.objects.first()
        render_pdf_sheet_fn(obj.pk)
