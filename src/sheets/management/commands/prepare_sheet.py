from django.core.management.base import BaseCommand

from ...task import prepare_sheet_fn


class Command(BaseCommand):
    def add_arguments(self, parser):
        parser.add_argument("sheet_pk")

    def handle(self, verbosity=0, **options):
        pk = options.get("sheet_pk")
        prepare_sheet_fn(pk, force_recompute=True)
