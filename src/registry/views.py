import datetime as dt
import json

import httpx
from django.conf import settings
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.utils import timezone
from django.views.generic import FormView, TemplateView

from accounts.models import ALL_BUT_OBSERVATOIRE
from common.mixins import FullyLoggedMixin
from common.sirets import validate_siret

from .constants import (
    REGISTRY_FORMAT_CSV,
    REGISTRY_FORMAT_XLS,
    REGISTRY_TYPE_ALL,
    REGISTRY_TYPE_INCOMING,
    REGISTRY_TYPE_OUTGOING,
    REGISTRY_TYPE_TRANSPORTED,
)
from .forms import RegistryPrepareForm
from .gql import graphql_query_csv, graphql_query_xls
from .models import RegistryDownload


class RegistryDownloadException(Exception):
    def __init__(self, message="Erreur de téléchargement"):
        self.message = message
        super().__init__(self.message)


CHECK_INSPECTION = False


class RegistryPrepare(FullyLoggedMixin, FormView):
    """
    View to download a registry
    """

    template_name = "sheets/../../templates/registry/registry_prepare.html"
    form_class = RegistryPrepareForm
    allowed_user_categories = ALL_BUT_OBSERVATOIRE

    def get_initial(self):
        # prefill siret field when coming from map
        siret = self.request.GET.get("siret", "")
        init = super().get_initial()
        if validate_siret(siret):
            init["siret"] = siret
        return init

    def form_valid(self, form):
        return self.handle_registry(form)

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

    def get_context_data(self, **kwargs):
        year = dt.date.today().year
        label_this_year = year
        label_prev_year = year - 1
        return super().get_context_data(**kwargs, label_this_year=label_this_year, label_prev_year=label_prev_year)


CONFIG = {
    "csv": {"query": graphql_query_csv, "name": "wastesRegistryCsv"},
    "xls": {"query": graphql_query_xls, "name": "wastesRegistryXls"},
}


class RegistryView(FullyLoggedMixin, TemplateView):
    template_name = "sheets/../../templates/registry/registry_download.html"
    allowed_user_categories = ALL_BUT_OBSERVATOIRE

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
