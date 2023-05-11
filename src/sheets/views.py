import base64
import datetime as dt

from braces.views import LoginRequiredMixin
from celery.result import AsyncResult
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.views.generic import DetailView, FormView, TemplateView

from config.celery_app import app

from .forms import SiretForm
from .models import ComputedInspectionData
from .task import prepare_sheet, render_pdf

# test


class HomeView(TemplateView):
    template_name = "home.html"

    def get(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return HttpResponseRedirect(reverse("login"))
        return super().get(request, *args, **kwargs)


CHECK_INSPECTION = False


class Prepare(LoginRequiredMixin, FormView):
    """
    View to prepare an inspection shee:.
        - render a form
        - launch an async task
        - redirect to a self refreshing waiting page
    """

    template_name = "sheets/prepare.html"
    form_class = SiretForm

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.existing_inspection = None
        self.new_inspection = None

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

        self.new_inspection = ComputedInspectionData.objects.create(
            org_id=siret, created_by=self.request.user.email
        )
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


class ComputingView(LoginRequiredMixin, TemplateView):
    """Optional `task_id` trigger result polling in template"""

    template_name = "sheets/result.html"

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx.update(
            {
                "task_id": self.kwargs.get("task_id", None),
                "compute_pk": self.kwargs.get("compute_pk", None),
                "redirect_to": "html",
            }
        )
        return ctx


class RenderingView(ComputingView):
    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx.update(
            {
                "redirect_to": "pdf",
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

        else:
            progress = 100.0 if done else 0.0

        ctx.update({"progress": int(progress)})

        if not job.ready():
            ctx.update({"state": STATE_RUNNING})
        else:
            result = job.get()
            ctx.update(
                {
                    "errors": result.get("errors", []),
                    "state": STATE_DONE,
                    "redirect_to": result.get("redirect", ""),
                }
            )
        return ctx


class Sheet(LoginRequiredMixin, DetailView):
    model = ComputedInspectionData
    template_name = "sheets/sheet.html"
    context_object_name = "sheet"


class PrepareSheetPdf(LoginRequiredMixin, DetailView):
    model = ComputedInspectionData

    def get(self, request, *args, **kwargs):
        self.object = self.get_object()

        if self.object.is_graph_rendered:
            return HttpResponseRedirect(reverse("sheet_pdf", args=[self.object.pk]))
        if self.object.is_computed:
            task = render_pdf.delay(self.object.pk)
            return HttpResponseRedirect(
                reverse(
                    "pollable_result_pdf",
                    kwargs={"compute_pk": self.object.pk, "task_id": task.id},
                )
            )
        return HttpResponseRedirect("/")


class SheetPdfHtml(LoginRequiredMixin, DetailView):
    """For debugging purpose"""

    model = ComputedInspectionData
    template_name = "sheets/sheetpdf.html"
    context_object_name = "sheet"

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data()

        # todo: useless, remove
        ctx.update(
            {
                "bsdd_created_rectified_graph": self.object.bsdd_created_rectified_graph,
                "bsdd_stock_graph": self.object.bsdd_stock_graph,
                "bsda_created_rectified_graph": self.object.bsda_created_rectified_graph,
                "bsda_stock_graph": self.object.bsda_stock_graph,
                "bsdasri_created_rectified_graph": self.object.bsdasri_created_rectified_graph,
                "bsdasri_stock_graph": self.object.bsdasri_stock_graph,
                "bsff_created_rectified_graph": self.object.bsff_created_rectified_graph,
                "bsff_stock_graph": self.object.bsff_stock_graph,
                "bsvhu_created_rectified_graph": self.object.bsvhu_created_rectified_graph,
                "bsvhu_stock_graph": self.object.bsvhu_stock_graph,
                "waste_origin_graph": self.object.waste_origin_graph,
                "waste_origin_map_graph": self.object.waste_origin_map_graph,
            }
        )
        return ctx


class SheetPdf(LoginRequiredMixin, DetailView):
    model = ComputedInspectionData

    def get(self, request, *args, **kwargs):
        sheet = self.get_object()
        # todo: check state
        decoded = base64.b64decode(sheet.pdf)

        response = HttpResponse(content_type="application/pdf")
        response[
            "Content-Disposition"
        ] = f'attachment; filename="{sheet.pdf_filename}.pdf"'
        response.write(decoded)
        return response
