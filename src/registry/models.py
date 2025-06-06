import datetime as dt
import uuid
from datetime import datetime

from django import forms
from django.contrib.postgres.fields import ArrayField
from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _

from accounts.models import User

from .constants import (
    RegistryV2DeclarationType,
    RegistryV2ExportState,
    RegistryV2ExportType,
    RegistryV2Format,
    RegistryV2WasteCode,
)
from .managers import RegistryV2ExportQuerySet


class _TypedMultipleChoiceField(forms.TypedMultipleChoiceField):
    def __init__(self, *args, **kwargs):
        kwargs.pop("base_field", None)
        kwargs.pop("max_length", None)
        super().__init__(*args, **kwargs)


class ChoiceArrayField(ArrayField):
    """
    A field that allows us to store an array of choices.

    Uses Django 4.2's postgres ArrayField
    and a TypeMultipleChoiceField for its formfield.

    Usage:

        choices = ChoiceArrayField(
            models.CharField(max_length=..., choices=(...,)), blank=[...], default=[...]
        )
    """

    def formfield(self, **kwargs):
        defaults = {
            "form_class": _TypedMultipleChoiceField,
            "choices": self.base_field.choices,
            "coerce": self.base_field.to_python,
        }
        defaults.update(kwargs)
        # Skip our parent's formfield implementation completely as we don't care for it.
        # pylint:disable=bad-super-call
        return super().formfield(**defaults)


class RegistryDownload(models.Model):
    """Deprecated model"""

    org_id = models.CharField(_("Organization ID"), max_length=20)

    data_start_date = models.DateTimeField(_("Data Start Date"), default=datetime(2022, 1, 1))
    data_end_date = models.DateTimeField(_("Data End Date"), default=timezone.now)

    created = models.DateTimeField(_("Created"), default=timezone.now)

    created_by = models.EmailField(verbose_name=_("Created by x"), blank=True)

    class Meta:
        verbose_name = _("Téléchargement de registre")
        verbose_name_plural = _("Téléchargements de registre")
        ordering = ("-created",)


MAX_PROCESSING_DELAY = 10  # minutes


class RegistryV2Export(models.Model):
    """Export V2 model"""

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    siret = models.CharField(_("Établissement concerné"), max_length=20)
    registry_type = models.CharField(
        _("Type de registre"),
        max_length=20,
        choices=RegistryV2ExportType.choices,
        default=RegistryV2ExportType.INCOMING,
    )
    declaration_type = models.CharField(
        _("Type de déclaration"),
        max_length=20,
        choices=RegistryV2DeclarationType.choices,
        default=RegistryV2DeclarationType.ALL,
    )
    waste_types_dnd = models.BooleanField(_("Déchets non dangereux"), default=False, blank=True)
    waste_types_dd = models.BooleanField(_("Déchets dangereux"), default=False, blank=True)
    waste_types_texs = models.BooleanField(_("Terres et sédiments"), default=False, blank=True)

    waste_codes = ChoiceArrayField(
        models.CharField(max_length=32, blank=True, choices=RegistryV2WasteCode),
        verbose_name=_("Codes déchets"),
        default=list,
        blank=True,
    )
    start_date = models.DateTimeField(_("Data Start Date"), default=datetime(2022, 1, 1))
    end_date = models.DateTimeField(_("End Date"), default=timezone.now)
    export_format = models.CharField(
        _("Format d'export"),
        max_length=20,
        choices=RegistryV2Format.choices,
        default=RegistryV2Format.CSV,
    )

    state = models.CharField(
        _("State"),
        max_length=20,
        choices=RegistryV2ExportState.choices,
        default=RegistryV2ExportState.PENDING,
    )

    created_at = models.DateTimeField(_("Created"), default=timezone.now)
    created_by = models.ForeignKey(
        User, verbose_name=_("Created by"), on_delete=models.SET_NULL, blank=True, null=True
    )
    created_by_email = models.EmailField(
        verbose_name=_("Created by email"), blank=True
    )  # keep history if user is deleted

    registry_export_id = models.CharField(_("Trackdéchets Export id"), blank=True)

    objects = RegistryV2ExportQuerySet.as_manager()

    class Meta:
        verbose_name = _("Téléchargement de registre V2")
        verbose_name_plural = _("Téléchargements de registre V2")
        ordering = ("-created_at",)

    def __str__(self):
        return f"Export {self.id} {self.siret}"

    @property
    def successful(self):
        return self.state == RegistryV2ExportState.SUCCESSFUL

    @property
    def is_timeout(self):
        return timezone.now() - self.created_at > dt.timedelta(minutes=MAX_PROCESSING_DELAY)

    @property
    def in_progress(self):
        return self.state in [RegistryV2ExportState.PENDING, RegistryV2ExportState.STARTED] and not self.is_timeout

    @property
    def waste_types(self):
        WASTE_TYPES = ["DND", "DD", "TEXS"]
        bool_vector = [self.waste_types_dnd, self.waste_types_dd, self.waste_types_texs]

        return [item for item, keep in zip(WASTE_TYPES, bool_vector) if keep]

    def mark_as_failed(self):
        self.state = RegistryV2ExportState.FAILED
        self.save()

    def get_gql_variables(self):
        variables = {
            "siret": self.siret,
            "registryType": self.registry_type,
            "format": self.export_format,
            "dateRange": {"_gte": self.start_date.isoformat(), "_lte": self.end_date.isoformat()},
        }
        where = {"declarationType": {"_eq": self.declaration_type}}

        if self.waste_types:
            where.update({"wasteType": {"_in": self.waste_types}})
        if self.waste_codes:
            where.update({"wasteCode": {"_in": self.waste_codes}})

        if where:
            variables.update({"where": where})
        return variables
