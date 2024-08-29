from django.forms import CharField, Form, ValidationError
from sqlalchemy.sql import text

from sheets.database import wh_engine
from sheets.queries import sql_company_query_exists_str


class RoadControlSearchForm(Form):
    siret = CharField(
        label="Numéro de SIRET",
        min_length=14,
        max_length=17,
        help_text="Format: 14 chiffres 123 456 789 00099",
    )

    plate = CharField(
        label="Immatriculation",
        min_length=7,
        max_length=14,
        help_text="Format: 7-14 caractères (AB-123-YZ)",
    )

    def clean_plate(self):
        plate = self.cleaned_data["plate"]
        plate = plate.replace("-", "")
        plate = "".join(plate.split())  # strip all whitespace
        return plate

    def clean_siret(self):
        siret = self.cleaned_data["siret"]
        siret = "".join(siret.split())  # strip all whitespace

        prepared_query = text(sql_company_query_exists_str)
        with wh_engine.connect() as con:
            companies = con.execute(prepared_query, siret=siret).all()

        if not companies:
            raise ValidationError("Établissement non inscrit sur Trackdéchets.")
        return siret
