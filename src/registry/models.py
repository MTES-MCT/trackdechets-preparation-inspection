from datetime import datetime

from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _


class RegistryDownload(models.Model):
    org_id = models.CharField(_("Organization ID"), max_length=20)

    data_start_date = models.DateTimeField(_("Data Start Date"), default=datetime(2022, 1, 1))
    data_end_date = models.DateTimeField(_("Data End Date"), default=timezone.now)

    created = models.DateTimeField(_("Created"), default=timezone.now)

    created_by = models.EmailField(verbose_name=_("Created by x"), blank=True)

    class Meta:
        verbose_name = _("Téléchargement de registre")
        verbose_name_plural = _("Téléchargements de registre")
        ordering = ("-created",)
