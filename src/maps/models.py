from django.contrib.gis.db import models
from django.contrib.postgres.fields import ArrayField
from django.utils.translation import gettext_lazy as _


class CartoCompany(models.Model):
    siret = models.TextField(db_index=True)
    nom_etablissement = models.TextField(null=True, blank=True)

    profils = ArrayField(models.TextField(), null=True, blank=True)
    profils_collecteur = ArrayField(models.TextField(), null=True, blank=True)
    profils_installation = ArrayField(models.TextField(), null=True, blank=True)

    # Bsdd
    bsdd = models.BooleanField(null=True, blank=True)
    bsdd_emitter = models.BooleanField(default=False)
    bsdd_transporter = models.BooleanField(default=False)
    bsdd_destination = models.BooleanField(default=False)

    # Bsdnd
    bsdnd = models.BooleanField(null=True, blank=True)
    bsdnd_emitter = models.BooleanField(default=False)
    bsdnd_transporter = models.BooleanField(default=False)
    bsdnd_destination = models.BooleanField(default=False)

    # Bsda
    bsda = models.BooleanField(null=True, blank=True)
    bsda_emitter = models.BooleanField(default=False)
    bsda_transporter = models.BooleanField(default=False)
    bsda_destination = models.BooleanField(default=False)

    # Bsff
    bsff = models.BooleanField(null=True, blank=True)
    bsff_emitter = models.BooleanField(default=False)
    bsff_transporter = models.BooleanField(default=False)
    bsff_destination = models.BooleanField(default=False)

    # Bsdasri
    bsdasri = models.BooleanField(null=True, blank=True)
    bsdasri_emitter = models.BooleanField(default=False)
    bsdasri_transporter = models.BooleanField(default=False)
    bsdasri_destination = models.BooleanField(default=False)

    # Bsvhu
    bsvhu = models.BooleanField(null=True, blank=True)
    bsvhu_emitter = models.BooleanField(default=False)
    bsvhu_transporter = models.BooleanField(default=False)
    bsvhu_destination = models.BooleanField(default=False)

    # Texs dd
    texs_dd = models.BooleanField(null=True, blank=True)
    texs_dd_emitter = models.BooleanField(default=False)
    texs_dd_transporter = models.BooleanField(default=False)
    texs_dd_destination = models.BooleanField(default=False)

    # Dnd
    dnd = models.BooleanField(null=True, blank=True)
    dnd_emitter = models.BooleanField(default=False)
    dnd_destination = models.BooleanField(default=False)

    # Texs
    texs = models.BooleanField(null=True, blank=True)
    texs_emitter = models.BooleanField(default=False)
    texs_destination = models.BooleanField(default=False)



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

    # Waste codes fields
    waste_codes_bordereaux = models.TextField(null=True, blank=True)
    waste_codes_dnd_statements = models.TextField(null=True, blank=True)
    waste_codes_texs_statements = models.TextField(null=True, blank=True)
    waste_codes_processed = models.TextField(null=True, blank=True)


    code_commune_insee = models.CharField(max_length=255, null=True, blank=True)
    code_departement_insee = models.CharField(null=True, blank=True)
    code_region_insee = models.IntegerField(null=True, blank=True)

    adresse_td = models.TextField(null=True, blank=True)
    adresse_insee = models.TextField(null=True, blank=True)

    latitude_td = models.DecimalField(max_digits=20, decimal_places=10, null=True, blank=True)
    longitude_td = models.DecimalField(max_digits=20, decimal_places=10, null=True, blank=True)
    latitude_ban = models.DecimalField(max_digits=20, decimal_places=10, null=True, blank=True)
    longitude_ban = models.DecimalField(max_digits=20, decimal_places=10, null=True, blank=True)

    coords = models.PointField(null=True, blank=True)

    class Meta:
        verbose_name = _("Établissement")
        verbose_name_plural = _("Établissements")


    def __str__(self):
        return f"{self.siret} - {self.nom_etablissement}"


