import pandas as pd
from django.conf import settings
from django.core.management.base import BaseCommand

from sheets.database import build_query
from sheets.ssh import ssh_tunnel

from ...models import CartoCompany

query = """
SELECT
    siret,
    nom_etablissement,
    profils,
    profils_collecteur,
    profils_installation,
    profils_installation_vhu,
    bsdd,
    bsdd_emitter,
    bsdd_transporter,
    bsdd_destination,
    bsdnd,
    bsdnd_emitter,
    bsdnd_transporter,
    bsdnd_destination,
    bsda,
    bsda_emitter,
    bsda_transporter,
    bsda_destination,
    bsda_worker,
    bsff,
    bsff_emitter,
    bsff_transporter,
    bsff_destination,
    bsdasri,
    bsdasri_emitter,
    bsdasri_transporter,
    bsdasri_destination,
    bsvhu,
    bsvhu_emitter,
    bsvhu_transporter,
    bsvhu_destination,
    texs_dd,
    texs_dd_emitter,
    texs_dd_transporter,
    texs_dd_destination,
    dnd,
    dnd_emitter,
    dnd_destination,
    texs,texs_emitter,texs_destination,
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
    
    waste_codes_bordereaux,
    waste_codes_dnd_statements,
    waste_codes_texs_statements,
    waste_codes_processed,
    
    code_commune_insee,
    code_departement_insee,
    code_region_insee,
    adresse_td,
    adresse_insee,
    
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
