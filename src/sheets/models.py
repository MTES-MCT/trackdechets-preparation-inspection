import json
import uuid
from datetime import datetime

import numpy as np
from django.conf import settings
from django.contrib.postgres.fields import ArrayField
from django.core.mail import EmailMessage
from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _


class CustomJSONEncoder(json.JSONEncoder):
    def default(self, obj):
        return super().encode(bool(obj)) if isinstance(obj, np.bool_) else super().default(obj)


def notify_admins(pk):
    body = f"La fiche d'inspection {pk} est en erreur"
    message = EmailMessage(
        subject="Une fiche d'inspection est en erreur",
        body=body,
        from_email=settings.DEFAULT_FROM_EMAIL,
        to=settings.MESSAGE_RECIPIENTS,
    )
    message.send()


class ComputedInspectionDataCustomManager(models.Manager):
    def mark_as_failed(self, pk):
        self.filter(pk=pk).update(state="COMPUTED_FAILED")
        notify_admins(pk)

    def mark_as_graph_rendered(self, pk):
        self.filter(pk=pk).update(state="GRAPH_RENDERED")


class ComputedInspectionData(models.Model):
    class StateChoice(models.TextChoices):
        INITIAL = "INITIAL", _("Initial")
        COMPUTED = "COMPUTED", _("Computed")
        GRAPH_RENDERED = "GRAPH_RENDERED", _("Graph rendered")
        COMPUTED_FAILED = "COMPUTED_FAILED", _("Computation failed")

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    state = models.CharField(
        _("State"),
        max_length=20,
        choices=StateChoice.choices,
        default=StateChoice.INITIAL,
    )
    org_id = models.CharField(_("Organization ID"), max_length=20)
    data_start_date = models.DateTimeField(_("Data Start Date"), default=datetime(2022, 1, 1))
    data_end_date = models.DateTimeField(_("Data End Date"), default=timezone.now)
    company_name = models.CharField(_("Company Name"), max_length=255, blank=True)
    company_profiles = ArrayField(
        models.CharField(_("Company profiles"), max_length=255),
        blank=True,
        default=list,
    )
    company_address = models.CharField(_("Company address"), max_length=255, blank=True)
    company_created_at = models.DateTimeField(_("Company created at"), default=timezone.now)
    created = models.DateTimeField(_("Created"), default=timezone.now)

    linked_companies_data = models.JSONField(default=dict)

    bsdd_created_rectified_data = models.JSONField(default=dict)
    bsdd_stock_data = models.JSONField(default=dict)
    bsdd_stats_data = models.JSONField(default=dict, encoder=CustomJSONEncoder)

    bsdd_non_dangerous_created_rectified_data = models.JSONField(default=dict)
    bsdd_non_dangerous_stock_data = models.JSONField(default=dict)
    bsdd_non_dangerous_stats_data = models.JSONField(default=dict, encoder=CustomJSONEncoder)

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

    all_bsd_data_empty = models.BooleanField(default=True)

    storage_data = models.JSONField(default=dict)

    waste_origin_data = models.JSONField(default=dict)
    waste_origin_map_data = models.JSONField(default=dict)

    waste_flows_data = models.JSONField(default=dict)

    icpe_data = models.JSONField(default=dict)
    agreement_data = models.JSONField(default=dict)
    traceability_interruptions_data = models.JSONField(default=dict)
    waste_is_dangerous_statements_data = models.JSONField(default=dict)
    bsd_canceled_data = models.JSONField(default=dict)
    same_emitter_recipient_data = models.JSONField(default=dict)
    private_individuals_collections_data = models.JSONField(default=dict)
    quantity_outliers_data = models.JSONField(default=dict)

    # Prerendered plotly viz

    bsdd_created_rectified_graph = models.TextField(blank=True)
    bsdd_stock_graph = models.TextField(blank=True)

    bsdd_non_dangerous_created_rectified_graph = models.TextField(blank=True)
    bsdd_non_dangerous_stock_graph = models.TextField(blank=True)

    bsda_created_rectified_graph = models.TextField(blank=True)
    bsda_stock_graph = models.TextField(blank=True)

    bsdasri_created_rectified_graph = models.TextField(blank=True)
    bsdasri_stock_graph = models.TextField(blank=True)

    bsff_created_rectified_graph = models.TextField(blank=True)
    bsff_stock_graph = models.TextField(blank=True)

    bsvhu_created_rectified_graph = models.TextField(blank=True)
    bsvhu_stock_graph = models.TextField(blank=True)

    waste_origin_graph = models.TextField(blank=True)
    waste_origin_map_graph = models.TextField(blank=True)

    icpe_2770_data = models.TextField(blank=True)
    icpe_2770_graph = models.TextField(blank=True)
    icpe_2790_data = models.TextField(blank=True)
    icpe_2790_graph = models.TextField(blank=True)
    icpe_2760_data = models.TextField(blank=True)
    icpe_2760_graph = models.TextField(blank=True)

    bs_processed_without_icpe_authorization = models.JSONField(default=dict)

    bsda_worker_stats_data = models.JSONField(default=dict)
    bsda_worker_quantity_data = models.JSONField(default=dict)
    bsda_worker_quantity_graph = models.TextField(blank=True)

    transporter_bordereaux_stats_graph_data = models.JSONField(default=dict)
    transporter_bordereaux_stats_graph = models.TextField(blank=True)
    quantities_transported_stats_graph_data = models.JSONField(default=dict)
    quantities_transported_stats_graph = models.TextField(blank=True)
    transporter_bordereaux_stats_data = models.JSONField(default=dict)

    pdf = models.TextField(blank=True)

    created_by = models.EmailField(verbose_name=_("Created by"), blank=True)

    objects = ComputedInspectionDataCustomManager()

    class Meta:
        verbose_name = _("ComputedInspectionData")
        verbose_name_plural = _("ComputedInspectionDatas")
        ordering = ("-created",)
        app_label = "sheets"

    def __str__(self):
        return f"Inspection {self.org_id}"

    @property
    def period_start(self):
        return self.data_start_date

    @property
    def period_end(self):
        return self.data_end_date

    @property
    def is_initial(self):
        return self.state == self.StateChoice.INITIAL

    @property
    def is_computed(self):
        return self.state == self.StateChoice.COMPUTED

    @property
    def is_graph_rendered(self):
        return self.state == self.StateChoice.GRAPH_RENDERED

    @property
    def pdf_filename(self):
        return f"FI-Trackdéchets-{self.org_id}-{self.created:%d-%m-%Y}"
