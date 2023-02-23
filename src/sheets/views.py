import datetime as dt
from base64 import b64encode

from braces.views import LoginRequiredMixin
from celery.result import AsyncResult
from django.urls import reverse
from django.views.generic import DetailView, FormView, TemplateView
from django_weasyprint import WeasyTemplateResponseMixin
from plotly.io import from_json

from config.celery_app import app

from .forms import SiretForm
from .models import ComputedInspectionData
from .task import prepare_sheet


class HomeView(TemplateView):
    template_name = "base.html"


CHECK_INSPECTION = False


class Prepare(FormView):
    template_name = "sheets/prepare.html"
    form_class = SiretForm

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.existing_inspection = None
        self.new_inspection = None

    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)

    def check_existing_inspection(self, siret):
        if not CHECK_INSPECTION:
            self.existing_inspection = None
            return
        today = dt.date.today()
        self.existing_inspection = ComputedInspectionData.objects.filter(
            org_id=siret, created__date=today
        ).first()

    def form_valid(self, form):
        siret = form.cleaned_data["siret"]

        if self.existing_inspection:
            return super().form_valid(form)

        self.new_inspection = ComputedInspectionData.objects.create(org_id=siret)
        self.task_id = prepare_sheet.delay(self.new_inspection.pk)

        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        return super().get_context_data(**kwargs, computed=self.new_inspection)

    def get_success_url(self):
        if self.existing_inspection:
            return reverse("sheet", args=[self.existing_inspection.pk])
        return reverse(
            "pollable_result",
            kwargs={"compute_pk": self.new_inspection.pk, "task_id": self.task_id},
        )


class ResultView(TemplateView):
    """Optional `task_id` trigger result polling in template"""

    template_name = "sheets/result.html"

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx.update(
            {
                "task_id": self.kwargs.get("task_id", None),
                "compute_pk": self.kwargs.get("compute_pk", None),
            }
        )
        return ctx


STATE_RUNNING = "running"
STATE_DONE = "done"


class FragmentResultView(LoginRequiredMixin, TemplateView):
    """View to be called by ResultView template to render api call results when done"""

    template_name = "sheets/_prepare_result.html"

    def dispatch(self, request, *args, **kwargs):
        self.task_id = self.kwargs.get("task_id")
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        job = AsyncResult(self.task_id, app=app)
        done = job.ready()
        result = job.result

        if isinstance(result, dict):
            progress = result.get("progress", 0)
            subscription_count = result.get("subscription_count", 0)
        else:
            progress = 100.0 if done else 0.0
            subscription_count = 0

        ctx.update(
            {"progress": int(progress), "subscription_count": subscription_count}
        )

        if not job.ready():
            ctx.update({"state": STATE_RUNNING})
        else:
            ctx.update({"errors": job.get(), "state": STATE_DONE})
        return ctx


class Sheet(DetailView):
    model = ComputedInspectionData
    template_name = "sheets/sheet.html"
    context_object_name = "sheet"


def plotly_to_bs64(fig):
    return b64encode(fig.to_image(format="png")).decode("ascii")


class SheetPdfHtml(DetailView):
    """For debugging purposes"""

    model = ComputedInspectionData
    template_name = "sheets/sheetpdf.html"
    context_object_name = "sheet"

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data()
        # bsdd
        bsdd_created_rectified_data = from_json(self.object.bsdd_created_rectified_data)
        bsdd_created_rectified_graph = plotly_to_bs64(bsdd_created_rectified_data)

        bsdd_stock_data = from_json(self.object.bsdd_stock_data)
        bsdd_stock_graph = plotly_to_bs64(bsdd_stock_data)

        # bsda
        if self.object.bsda_created_rectified_data:
            bsda_created_rectified_data = from_json(
                self.object.bsda_created_rectified_data
            )
            bsda_created_rectified_graph = plotly_to_bs64(bsda_created_rectified_data)
        else:
            bsda_created_rectified_graph = None
        if self.object.bsda_stock_data:
            bsda_stock_data = from_json(self.object.bsda_stock_data)
            bsda_stock_graph = plotly_to_bs64(bsda_stock_data)
        else:
            bsda_stock_graph = None

        # bsdasri
        if self.object.bsdasri_created_rectified_data:
            bsdasri_created_rectified_data = from_json(
                self.object.bsdasri_created_rectified_data
            )
            bsdasri_created_rectified_graph = plotly_to_bs64(
                bsdasri_created_rectified_data
            )
        else:
            bsdasri_created_rectified_graph = None
        if self.object.bsdasri_stock_data:
            bsdasri_stock_data = from_json(self.object.bsdasri_stock_data)
            bsdasri_stock_graph = plotly_to_bs64(bsdasri_stock_data)
        else:
            bsdasri_stock_graph = None
        # bsff
        if self.object.bsff_created_rectified_data:
            bsff_created_rectified_data = from_json(
                self.object.bsff_created_rectified_data
            )
            bsff_created_rectified_graph = plotly_to_bs64(bsff_created_rectified_data)
        else:
            bsff_created_rectified_graph = None
        if self.object.bsff_stock_data:
            bsff_stock_data = from_json(self.object.bsff_stock_data)
            bsff_stock_graph = plotly_to_bs64(bsff_stock_data)
        else:
            bsff_stock_graph = None

        # bsvhu
        if self.object.bsvhu_created_rectified_data:
            bsvhu_created_rectified_data = from_json(
                self.object.bsvhu_created_rectified_data
            )
            bsvhu_created_rectified_graph = plotly_to_bs64(bsvhu_created_rectified_data)
        else:
            bsvhu_created_rectified_graph = None

        if self.object.bsvhu_stock_data:
            bsvhu_stock_data = from_json(self.object.bsvhu_stock_data)
            bsvhu_stock_graph = plotly_to_bs64(bsvhu_stock_data)
        else:
            bsvhu_stock_graph = None

        waste_origin_data = from_json(self.object.waste_origin_data)
        waste_origin_graph = plotly_to_bs64(waste_origin_data)

        waste_origin_map_data = from_json(self.object.waste_origin_map)
        waste_origin_map = plotly_to_bs64(waste_origin_map_data)

        ctx.update(
            {
                "bsdd_created_rectified_graph": bsdd_created_rectified_graph,
                "bsdd_stock_graph": bsdd_stock_graph,
                "bsda_created_rectified_graph": bsda_created_rectified_graph,
                "bsda_stock_graph": bsda_stock_graph,
                "bsdasri_created_rectified_graph": bsdasri_created_rectified_graph,
                "bsdasri_stock_graph": bsdasri_stock_graph,
                "bsff_created_rectified_graph": bsff_created_rectified_graph,
                "bsff_stock_graph": bsff_stock_graph,
                "bsvhu_created_rectified_graph": bsvhu_created_rectified_graph,
                "bsvhu_stock_graph": bsvhu_stock_graph,
                "waste_origin_graph": waste_origin_graph,
                "waste_origin_map": waste_origin_map,
            }
        )
        return ctx


class SheetPdf(WeasyTemplateResponseMixin, SheetPdfHtml):
    def get_pdf_filename(self):
        return f"FI-Trackdéchets-{self.object.org_id}-{self.object.created:%d-%m-%Y}"
