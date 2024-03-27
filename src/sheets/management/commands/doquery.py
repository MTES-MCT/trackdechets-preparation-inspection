from django.core.management.base import BaseCommand

from ...views import get_registry


class Command(BaseCommand):
    def handle(self, verbosity=0, **options):
        get_registry()
