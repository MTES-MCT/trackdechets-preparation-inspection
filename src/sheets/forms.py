from django import forms
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


class SiretForm(forms.Form):
    siret = forms.CharField(max_length=14)
    start_date = forms.DateField()
    end_date = forms.DateField()

    def clean_siret(self):
        siret = self.cleaned_data["siret"]
        prepared_query = text(sql_company_query_str)
        with wh_engine.connect() as con:
            companies = con.execute(prepared_query, siret=siret).all()
        if not companies:
            raise forms.ValidationError("Siret non trouvé")
        return siret
