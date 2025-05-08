from django.core.management.base import BaseCommand

from maps.processors.stats_processor import build_stats_and_figs

from ...processors.clear import clear_figs
from ...processors.create_df import build_dataframes


class Command(BaseCommand):
    def handle(self, verbosity=0, **options):
        clear_figs()

        build_dataframes()

        for year in [2022, 2023, 2024, 2025]:
            build_stats_and_figs(year, clear_year=True)
