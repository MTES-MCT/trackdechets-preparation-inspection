import base64
import datetime as dt
import json

import httpx
from celery.result import AsyncResult
from django.conf import settings
from django.http import Http404, HttpResponse, HttpResponseRedirect
from django.urls import reverse, reverse_lazy
from django.utils import timezone
from django.views.generic import DetailView, FormView, TemplateView

from common.mixins import SecondFactorMixin
from config.celery_app import app
from content.models import FeedbackResult

from ..constants import (
    REGISTRY_FORMAT_CSV,
    REGISTRY_FORMAT_XLS,
    REGISTRY_TYPE_ALL,
    REGISTRY_TYPE_INCOMING,
    REGISTRY_TYPE_OUTGOING,
    REGISTRY_TYPE_TRANSPORTED,
)
from ..forms import SiretForm
from ..gql import graphql_query_csv, graphql_query_xls
from ..models import ComputedInspectionData, RegistryDownload
from ..task import prepare_sheet, render_pdf


class RegistryDownloadException(Exception):
    def __init__(self, salary, message="Erreur de téléchargement"):
        self.message = message
        super().__init__(self.message)


class PublicHomeView(TemplateView):
    template_name = "public_home.html"

    def get(self, request, *args, **kwargs):
        """Redirect user to private home or second_factor page wether they're logged in or verified."""
        if request.user.is_verified():
            return HttpResponseRedirect(reverse_lazy("private_home"))
        if request.user.is_authenticated:
            return HttpResponseRedirect(reverse_lazy("second_factor"))
        return super().get(request, *args, **kwargs)


class PrivateHomeView(SecondFactorMixin, TemplateView):
    template_name = "private_home.html"

    def has_filled_survey(self):
        return FeedbackResult.objects.filter(author=self.request.user.email).exists()

    def get_context_data(self, **kwargs):
        # display survey links until user fills it
        return super().get_context_data(**kwargs, has_filled_survey=self.has_filled_survey())


CHECK_INSPECTION = False

CONFIG = {
    "csv": {"query": graphql_query_csv, "name": "wastesRegistryCsv"},
    "xls": {"query": graphql_query_xls, "name": "wastesRegistryXls"},
}


class Registry(SecondFactorMixin, TemplateView):
    template_name = "sheets/registry_download.html"

    def get_file_name(self, siret, registry_format, registry_type):
        extension = {REGISTRY_FORMAT_XLS: "xlsx", REGISTRY_FORMAT_CSV: "csv"}.get(registry_format)
        suffix = {
            REGISTRY_TYPE_ALL: "exhaustif",
            REGISTRY_TYPE_INCOMING: "entrant",
            REGISTRY_TYPE_OUTGOING: "sortant",
            REGISTRY_TYPE_TRANSPORTED: "transport",
        }.get(registry_type, "")
        dt = timezone.now().strftime("%Y-%m-%d-%H-%M")
        return f"Registre-{suffix}-{siret}-{dt}.{extension}"

    def get_mime_type(self, registry_format):
        return {
            REGISTRY_FORMAT_XLS: "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
            REGISTRY_FORMAT_CSV: "text/csv",
        }.get(registry_format)

    def get_registry_download_link(self, siret, registry_format, registry_type, start_dt, end_dt):
        config = CONFIG.get(registry_format)
        date_field = (
            "destinationReceptionDate" if registry_type == REGISTRY_TYPE_INCOMING else "transporterTakenOverAt"
        )
        where = {date_field: {"_gte": start_dt, "_lte": end_dt}}
        try:
            res = self.client.post(
                url=settings.TD_API_URL,
                headers={"Authorization": f"Bearer {settings.TD_API_TOKEN}"},
                json={
                    "query": config["query"],
                    "variables": {"sirets": [siret], "registryType": registry_type, "where": where},
                },
            )
        except httpx.RequestError:
            raise RegistryDownloadException()
        try:
            rep = res.json()
        except json.JSONDecodeError:
            raise RegistryDownloadException()

        if errors := rep.get("errors", None):
            raise RegistryDownloadException("".join([e.get("message") for e in errors]))

        link = rep.get("data", {}).get(config["name"], {}).get("downloadLink", None)
        return link

    def get_registry_content(self, link):
        try:
            r = self.client.get(link)
        except httpx.RequestError:
            raise RegistryDownloadException()
        return r.content

    def get(self, request, *args, **kwargs):
        # store template response displaying an error message if download fails

        tpl_response = super().get(request)
        session = self.request.session
        try:
            siret = session.pop("siret")
            registry_type = session.pop("registry_type")
            registry_format = session.pop("registry_format")
            data_start_date = dt.date.fromisoformat(session.pop("start_date"))
            data_end_date = dt.date.fromisoformat(session.pop("end_date"))
            # convert dates to datetime
            data_start_dt = dt.datetime.combine(data_start_date, dt.time.min).isoformat()
            data_end_dt = dt.datetime.combine(data_end_date, dt.time.max).isoformat()
        except KeyError:
            return tpl_response

        # instanciate httpx client for the 2 next requests
        self.client = httpx.Client(timeout=60)  # 60 seconds

        try:
            download_link = self.get_registry_download_link(
                siret=siret,
                registry_format=registry_format,
                registry_type=registry_type,
                start_dt=data_start_dt,
                end_dt=data_end_dt,
            )
        except RegistryDownloadException:
            return tpl_response

        if not download_link:
            return tpl_response

        try:
            content = self.get_registry_content(download_link)
        except httpx.RequestError:
            return tpl_response
        filename = self.get_file_name(siret=siret, registry_format=registry_format, registry_type=registry_type)
        mimetype = self.get_mime_type(registry_format)
        response = HttpResponse(content_type=mimetype)
        response["Content-Disposition"] = f'attachment; filename="{filename}"'
        response.write(content)
        RegistryDownload.objects.create(
            org_id=siret,
            created_by=self.request.user.email,
            data_start_date=data_start_dt,
            data_end_date=data_end_date,
        )
        return response


class Prepare(SecondFactorMixin, FormView):
    """
    View to prepare an inspection sheet $:
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
        self.is_registry = False
        self.is_inspection = False

    def check_existing_inspection(self, siret):
        if not CHECK_INSPECTION:
            self.existing_inspection = None
            return
        today = dt.date.today()
        self.existing_inspection = ComputedInspectionData.objects.filter(org_id=siret, created__date=today).first()

    def form_valid(self, form):
        self.is_registry = bool(self.request.POST.get("registry"))
        self.is_inspection = bool(self.request.POST.get("inspection"))

        if self.is_inspection:
            return self.handle_inspection(form)
        if self.is_registry:
            return self.handle_registry(form)
        raise Http404

    def handle_registry(self, form):
        # store form data in session and redirect to download view
        for fn in [
            "siret",
            "registry_type",
            "registry_format",
        ]:
            self.request.session[fn] = form.cleaned_data[fn]
        for fn in ["start_date", "end_date"]:
            self.request.session[fn] = form.cleaned_data[fn].isoformat()

        return HttpResponseRedirect(reverse("registry"))

    def handle_inspection(self, form):
        siret = form.cleaned_data["siret"]
        data_start_date = form.cleaned_data["start_date"]
        data_end_date = form.cleaned_data["end_date"]
        if self.existing_inspection:
            return super().form_valid(form)

        self.new_inspection = ComputedInspectionData.objects.create(
            org_id=siret,
            data_start_date=data_start_date,
            data_end_date=data_end_date,
            created_by=self.request.user.email,
        )
        self.task_id = prepare_sheet.delay(self.new_inspection.pk)
        return HttpResponseRedirect(self.get_success_url())

    def get_context_data(self, **kwargs):
        year = dt.date.today().year
        label_this_year = year
        label_prev_year = year - 1
        return super().get_context_data(
            **kwargs, computed=self.new_inspection, label_this_year=label_this_year, label_prev_year=label_prev_year
        )

    def get_success_url(self):
        if self.existing_inspection:
            return reverse("sheet", args=[self.existing_inspection.pk])
        return reverse(
            "pollable_result",
            kwargs={"compute_pk": self.new_inspection.pk, "task_id": self.task_id},
        )


class ComputingView(SecondFactorMixin, TemplateView):
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


class FragmentResultView(SecondFactorMixin, TemplateView):
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


class Sheet(SecondFactorMixin, DetailView):
    model = ComputedInspectionData
    template_name = "sheets/sheet.html"
    context_object_name = "sheet"


class PrepareSheetPdf(SecondFactorMixin, DetailView):
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


class SheetPdfHtml(SecondFactorMixin, DetailView):
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
                "bsdd_non_dangerous_created_rectified_graph": self.object.bsdd_non_dangerous_created_rectified_graph,
                "bsdd_non_dangerous_stock_graph": self.object.bsdd_non_dangerous_stock_graph,
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
                "icpe_2770_graph": self.object.icpe_2770_graph,
                "icpe_2790_graph": self.object.icpe_2790_graph,
                "icpe_2760_graph": self.object.icpe_2760_graph,
                "bsda_worker_quantity_graph": self.object.bsda_worker_quantity_graph,
                "bs_transported_graph": self.object.transporter_bordereaux_stats_graph,
                "bs_quantities_transported_graph": self.object.quantities_transported_stats_graph,
            }
        )
        return ctx


class SheetPdf(SecondFactorMixin, DetailView):
    model = ComputedInspectionData

    def get(self, request, *args, **kwargs):
        sheet = self.get_object()
        # todo: check state
        decoded = base64.b64decode(sheet.pdf)

        response = HttpResponse(content_type="application/pdf")
        response["Content-Disposition"] = f'attachment; filename="{sheet.pdf_filename}.pdf"'
        response.write(decoded)
        return response
