import json
import uuid

import numpy as np
from django.contrib.postgres.fields import ArrayField
from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _


# todo : rename
class CustomJSONEncoder(json.JSONEncoder):
    def default(self, obj):
        return (
            super().encode(bool(obj))
            if isinstance(obj, np.bool_)
            else super().default(obj)
        )


class ComputedInspectionData(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    org_id = models.CharField(_("Organization ID"), max_length=20)
    company_name = models.CharField(_("Company Name"), max_length=255, blank=True)
    company_profiles = ArrayField(
        models.CharField(_("Company profiles"), max_length=255),
        blank=True,
        default=list,
    )
    company_address = models.CharField(_("Company address"), max_length=255, blank=True)
    created = models.DateTimeField(_("Created"), default=timezone.now)

    bsdd_created_rectified_graph = models.BinaryField(
        blank=True, null=True, editable=True
    )
    bsdd_stock_graph = models.BinaryField(blank=True, null=True, editable=True)
    bsdd_stats_graph = models.BinaryField(blank=True, null=True, editable=True)

    bsdd_created_rectified_data = models.JSONField(default=dict)
    bsdd_stock_data = models.JSONField(default=dict)
    bsdd_stats_data = models.JSONField(default=dict, encoder=CustomJSONEncoder)

    bsda_created_rectified_data = models.JSONField(default=dict)
    bsda_stock_data = models.JSONField(default=dict)
    bsda_stats_data = models.JSONField(default=dict, encoder=CustomJSONEncoder)

    bsdasri_created_rectified_data = models.JSONField(default=dict)
    bsdasri_stock_data = models.JSONField(default=dict)
    bsdasri_stats_data = models.JSONField(default=dict, encoder=CustomJSONEncoder)

    bsff_created_rectified_data = models.JSONField(default=dict)
    bsff_stock_data = models.JSONField(default=dict)
    bsff_stats_data = models.JSONField(default=dict, encoder=CustomJSONEncoder)

    bsvhu_created_rectified_data = models.JSONField(default=dict)
    bsvhu_stock_data = models.JSONField(default=dict)
    bsvhu_stats_data = models.JSONField(default=dict, encoder=CustomJSONEncoder)

    storage_data = models.JSONField(default=dict)

    waste_origin_data = models.JSONField(default=dict)
    waste_origin_map = models.JSONField(default=dict)

    input_output_waste_data = models.JSONField(default=dict)

    outliers_data = models.JSONField(default=dict)
    icpe_data = models.JSONField(default=dict)
    agreement_data = models.JSONField(default=dict)

    class Meta:
        verbose_name = _("ComputedInspectionData")
        verbose_name_plural = _("ComputedInspectionDatas")
        ordering = ("-created",)
        app_label = "sheets"

    def __str__(self):
        return f"Inspection {self.org_id}"

    @property
    def period_start(self):
        return self.created.replace(year=self.created.year - 1)

    @property
    def period_end(self):
        return self.created
