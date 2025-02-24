import pandas as pd
from django.conf import settings
from django.core.management.base import BaseCommand

from sheets.database import build_query
from sheets.ssh import ssh_tunnel

from ...models import CartoCompany

BATCH_SIZE = 10000
query = """
SELECT
	siret,
	nom_etablissement,
	profils,
	profils_collecteur,
	profils_installation,
	bsdd,
	bsdnd,
	bsda,
	bsff,
	bsdasri,
	bsvhu,
	texs_dd,
	dnd,
	texs,
	ssd,
	pnttd,
	processing_operations_bsdd,
	processing_operations_bsdnd,
	processing_operations_bsda,
	processing_operations_bsff,
	processing_operations_bsdasri,
	processing_operations_bsvhu,
	processing_operation_dnd,
	processing_operation_texs,
	code_commune_insee,
	code_departement_insee,
	code_region_insee,
	adresse_td,
	adresse_insee,
	latitude_td,
	longitude_td,
	latitude_ban,
	longitude_ban,
	coords
FROM
	refined_zone_analytics.cartographie_des_etablissements_geocoded
"""





class Command(BaseCommand):
    def handle(self, verbosity=0, **options):
        CartoCompany.objects.all().delete()

        with ssh_tunnel(settings):
            companies_df = build_query(query)

        companies_dicts = companies_df.to_dict(orient="records")
        companies_dicts_without_nan = [
            {k: (None if (isinstance(v, float) and pd.isna(v)) else v) for k, v in e.items()} for e in companies_dicts
        ]

        data = [CartoCompany(**c) for c in companies_dicts_without_nan]
        CartoCompany.objects.bulk_create(data)
