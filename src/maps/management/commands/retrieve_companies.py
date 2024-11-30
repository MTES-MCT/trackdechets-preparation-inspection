from django.conf import settings
from django.core.management.base import BaseCommand
from sqlalchemy import create_engine
from sqlalchemy.sql import text

from ...models import CartoCompany

wh_engine = create_engine(settings.WAREHOUSE_URL, pool_pre_ping=True)

BATCH_SIZE = 10000
query = """
 SELECT
	*
FROM
	refined_zone_analytics.cartographie_des_etablissements
	ORDER BY siret
LIMIT :limit
OFFSET :offset
"""


class Command(BaseCommand):
    def handle(self, verbosity=0, **options):
        CartoCompany.objects.all().delete()
        has_next_page = True
        offset = 0
        while has_next_page:
            prepared_query = text(query)
            with wh_engine.connect() as con:
                companies = con.execute(prepared_query, {"offset": offset, "limit": BATCH_SIZE + 1}).all()

            offset += BATCH_SIZE

            data = [CartoCompany(**c._asdict()) for c in companies[:BATCH_SIZE]]
            CartoCompany.objects.bulk_create(data)

            has_next_page = len(companies) > BATCH_SIZE
