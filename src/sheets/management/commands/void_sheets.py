import logging

from django.core.management.base import BaseCommand

from sheets.models import ComputedInspectionData

batch_size = 100

logger = logging.getLogger(__name__)


class Command(BaseCommand):
    def handle(self, verbosity=0, **options):
        """Set computed field to empty string or json for ComputedInspectionData older than 90 days iot save db space."""
        qs = ComputedInspectionData.objects.to_void()

        json_fields = ComputedInspectionData.get_json_fields_to_void()
        text_fields = ComputedInspectionData.get_text_fields_to_void()
        all_fields = json_fields + text_fields + ["voided"]

        payload_json = {field_name: {} for field_name in json_fields}
        payload_text = {field_name: "" for field_name in text_fields}
        payload = {**payload_json, **payload_text}

        for sheet in qs:
            for attr, value in payload.items():
                setattr(sheet, attr, value)
            sheet.voided = True
        updated_count = ComputedInspectionData.objects.bulk_update(qs, all_fields, batch_size=batch_size)
        logger.info(f"{updated_count} sheets voided")
