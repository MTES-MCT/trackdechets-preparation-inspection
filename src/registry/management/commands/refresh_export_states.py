import datetime as dt
import time

from django.core.management.base import BaseCommand
from django.utils import timezone

from ...constants import RegistryV2ExportState
from ...models import RegistryV2Export
from ...task import refresh_registry_export


class Command(BaseCommand):
    """
    Get pending RegistryV2Export and update their state by checking on TD api.
    This runs for a specified duration, checking at regular intervals
    ."""

    help = "Refresh pending exports states at regular intervals for a specified duration"

    def add_arguments(self, parser):
        parser.add_argument(
            "--duration", type=int, default=10 * 60, help="Total duration to run in seconds (default: 600 s)"
        )
        parser.add_argument(
            "--interval", type=int, default=60, help="Interval between checks in seconds (default: 60)"
        )

    def handle(self, *args, **options):
        duration_seconds = options["duration"]
        interval_seconds = options["interval"]

        end_time = timezone.now() + dt.timedelta(seconds=duration_seconds)

        self.stdout.write(
            self.style.SUCCESS(
                f"Starting refresh task at {timezone.now().strftime('%H:%M:%S')}, "
                f"will run until {end_time.strftime('%H:%M:%S')} "
                f"with {interval_seconds} seconds interval"
            )
        )

        iteration = 1

        while timezone.now() < end_time:
            current_time = timezone.now()
            self.stdout.write(f"Iteration {iteration} at {current_time.strftime('%H:%M:%S')}")
            self._process_pending_exports()

            remaining_time = (end_time - timezone.now()).total_seconds()

            if remaining_time <= 0:
                break

            sleep_time = min(interval_seconds, remaining_time)
            self.stdout.write(f"Sleeping for {int(sleep_time)} seconds...")
            time.sleep(sleep_time)
            iteration += 1

        self.stdout.write(self.style.SUCCESS(f"Finished refresh task at {timezone.now().strftime('%H:%M:%S')}"))

    def _process_pending_exports(self):
        regs = RegistryV2Export.objects.recent().filter(
            state__in=[RegistryV2ExportState.PENDING, RegistryV2ExportState.STARTED]
        )

        count = regs.count()
        self.stdout.write(f"Found {count} pending exports")

        for reg in regs:
            if reg.registry_export_id:
                self.stdout.write(f"Queuing refresh for export {reg.pk}")
                refresh_registry_export.delay(reg.pk)
                continue
            # if too old and still pending, mark as failed
            if timezone.now() - reg.created_at > dt.timedelta(hours=1):
                self.stdout.write(f"Marking export {reg.pk} as failed (too old)")
                reg.mark_as_failed()
