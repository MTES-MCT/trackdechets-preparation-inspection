from django.contrib.gis.db import models
from django.contrib.postgres.fields import ArrayField
from django.utils.translation import gettext_lazy as _


class CartoCompany(models.Model):
    siret = models.TextField(db_index=True)
    nom_etablissement = models.TextField(null=True, blank=True)

    profils = ArrayField(models.TextField(), null=True, blank=True)
    profils_collecteur = ArrayField(models.TextField(), null=True, blank=True)
    profils_installation = ArrayField(models.TextField(), null=True, blank=True)

    bsdd = models.BooleanField(null=True, blank=True)
    bsdnd = models.BooleanField(null=True, blank=True)
    bsda = models.BooleanField(null=True, blank=True)
    bsff = models.BooleanField(null=True, blank=True)
    bsdasri = models.BooleanField(null=True, blank=True)
    bsvhu = models.BooleanField(null=True, blank=True)
    texs_dd = models.BooleanField(null=True, blank=True)
    dnd = models.BooleanField(null=True, blank=True)
    texs = models.BooleanField(null=True, blank=True)
    ssd = models.BooleanField(null=True, blank=True)
    pnttd = models.BooleanField(null=True, blank=True)

    processing_operations_bsdd = ArrayField(models.TextField(), null=True, blank=True)
    processing_operations_bsdnd = ArrayField(models.TextField(), null=True, blank=True)
    processing_operations_bsda = ArrayField(models.TextField(), null=True, blank=True)
    processing_operations_bsff = ArrayField(models.TextField(), null=True, blank=True)
    processing_operations_bsdasri = ArrayField(models.TextField(), null=True, blank=True)
    processing_operations_bsvhu = ArrayField(models.TextField(), null=True, blank=True)
    processing_operation_dnd = ArrayField(models.CharField(max_length=255), null=True, blank=True)
    processing_operation_texs = ArrayField(models.CharField(max_length=255), null=True, blank=True)

    code_commune_insee = models.CharField(max_length=255, null=True, blank=True)
    code_departement_insee = models.CharField(null=True, blank=True)
    code_region_insee = models.IntegerField(null=True, blank=True)

    adresse_td = models.TextField(null=True, blank=True)
    adresse_insee = models.TextField(null=True, blank=True)

    latitude_td = models.DecimalField(max_digits=20, decimal_places=10, null=True, blank=True)
    longitude_td = models.DecimalField(max_digits=20, decimal_places=10, null=True, blank=True)
    latitude_ban = models.FloatField(null=True, blank=True)
    longitude_ban = models.FloatField(null=True, blank=True)

    coords = models.PointField(null=True, blank=True)

    class Meta:
        verbose_name = _("Établissement")
        verbose_name_plural = _("Établissements")
