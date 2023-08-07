from datetime import datetime, timedelta
from django.forms import CharField, DateField, Form, ValidationError
from django.forms.widgets import DateInput
from sqlalchemy.sql import text

from .database import wh_engine

sql_company_query_str = """
select
    id
 from
    trusted_zone_trackdechets.company
where
    siret = :siret ;
"""


class SiretForm(Form):
    siret = CharField(max_length=14)
    start_date = DateField(
        label="Date de début des données",
        initial=datetime.now() - timedelta(days=365),
        help_text="Saisissez la date minimale pour laquelle vous souhaitez récupérer les données",
        widget=DateInput(
            attrs={
                "type": "date",
            },
            format="%d-%m-%Y",
        ),
    )
    end_date = DateField(
        label="Date de fin des données",
        initial=datetime.now(),
        help_text="Saisissez la date maximale pour laquelle vous souhaitez récupérer les données",
        widget=DateInput(
            attrs={"type": "date", "max": datetime.now().strftime(format="%Y-%m-%d")},
            format="%d-%m-%Y",
        ),
    )

    def clean_siret(self):
        siret = self.cleaned_data["siret"]
        prepared_query = text(sql_company_query_str)
        with wh_engine.connect() as con:
            companies = con.execute(prepared_query, siret=siret).all()
        if not companies:
            raise ValidationError("Siret non trouvé")
        return siret
