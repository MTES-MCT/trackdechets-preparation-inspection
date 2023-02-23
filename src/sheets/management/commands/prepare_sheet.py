from django.core.management.base import BaseCommand

from ...task import prepare_sheet_fn


class Command(BaseCommand):
    def handle(self, verbosity=0, **kwargs):
        prepare_sheet_fn("")
