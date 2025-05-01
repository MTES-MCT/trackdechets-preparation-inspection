import datetime as dt

from django.core.management.base import BaseCommand
from django.utils import timezone

from ...constants import RegistryV2ExportState
from ...models import RegistryV2Export
from ...task import refresh_registry_export


class Command(BaseCommand):
    """Get pending RegistryV2Export` and update their state by checking on TD api. This must be put in a cron job."""

    help = "Refresh pending exports states"

    def handle(self, *args, **options):
        regs = RegistryV2Export.objects.recent().filter(
            state__in=[RegistryV2ExportState.PENDING, RegistryV2ExportState.STARTED]
        )

        for reg in regs:
            if reg.registry_export_id:
                refresh_registry_export.delay(reg.pk)
                continue
            # if too old ans still pending, mark as failed
            if timezone.now() - reg.created_at > dt.timedelta(hours=1):
                reg.mark_as_failed()
