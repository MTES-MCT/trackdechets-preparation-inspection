from django.db import models
from solo.models import SingletonModel


class SiteConfiguration(SingletonModel):
    banner_title = models.CharField(blank=True, verbose_name="Bannière d'information - titre")
    banner_content = models.TextField(blank=True, verbose_name="Bannière d'information - contenu")

    def __str__(self):
        return "Site Configuration"

    class Meta:
        verbose_name = "Site Configuration"
