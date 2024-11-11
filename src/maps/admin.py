from django.contrib import admin

from .models import CartoCompany


@admin.register(CartoCompany)
class CartoCompanyAdmin(admin.ModelAdmin):
    list_display = ["siret", "nom_etablissement", "coords"]
    search_fields = ["siret", "nom_etablissement"]
