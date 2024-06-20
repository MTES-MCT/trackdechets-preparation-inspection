from django.core.management.base import BaseCommand

from sheets.data_processing import SheetProcessor


class Command(BaseCommand):
    def add_arguments(self, parser):
        parser.add_argument("sheet_pk")

    def handle(self, verbosity=0, **options):
        pk = options.get("sheet_pk")
        processor = SheetProcessor(pk)
        processor.process()
