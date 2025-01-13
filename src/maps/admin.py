from django.contrib import admin

from .models import CartoCompany


@admin.register(CartoCompany)
class CartoCompanyAdmin(admin.ModelAdmin):
    list_display = [
        "siret",
        "nom_etablissement",
        "coords",
        "code_commune_insee",
        "code_departement_insee",
        "code_region_insee",
    ]
    search_fields = ["siret", "nom_etablissement"]
