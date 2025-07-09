import datetime as dt

import httpx
from django.conf import settings
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.views.generic import CreateView, FormView, ListView
from rest_framework.reverse import reverse_lazy

from accounts.constants import PERMS_SHEET_AND_REGISTRY
from common.constants import HISTORY_SIZE
from common.mixins import FullyLoggedMixin
from data_exports.views import DummyForm

from .forms import RegistryV2PrepareForm
from .gql import graphql_registry_V2_export_download_signed_url
from .models import RegistryV2Export
from .task import process_export


class RegistryDownloadException(Exception):
    def __init__(self, message="Erreur de téléchargement"):
        self.message = message
        super().__init__(self.message)


class RegistryV2Prepare(FullyLoggedMixin, CreateView):
    """
    View to download a registry
    """

    template_name = "registry/registry_v2_prepare.html"
    form_class = RegistryV2PrepareForm
    allowed_user_categories = PERMS_SHEET_AND_REGISTRY
    success_url = reverse_lazy("registry_v2_prepare")

    def get_form_kwargs(self):
        kw = super().get_form_kwargs()
        kw["created_by"] = self.request.user
        return kw

    def get_context_data(self, **kwargs):
        year = dt.date.today().year
        label_this_year = year
        label_prev_year = year - 1
        return super().get_context_data(**kwargs, label_this_year=label_this_year, label_prev_year=label_prev_year)

    def form_valid(
        self,
        form,
    ):
        res = super().form_valid(form)

        process_export(self.object.pk)
        return res


class RegistryV2ListContent(FullyLoggedMixin, ListView):
    template_name = "registry/fragments/_registry_v2_list_content.html"
    allowed_user_categories = PERMS_SHEET_AND_REGISTRY
    model = RegistryV2Export
    context_object_name = "exports"

    def get_queryset(self):
        return super().get_queryset().filter(created_by=self.request.user)[:HISTORY_SIZE]


class RegistryV2Retrieve(FullyLoggedMixin, FormView):
    template_name = "registry/fragments/_registry_v2_list_content.html"
    form_class = DummyForm
    success_url = None
    allowed_user_categories = PERMS_SHEET_AND_REGISTRY

    def form_valid(self, form):
        registry_pk = self.kwargs.get("registry_pk")
        export = RegistryV2Export.objects.get(pk=registry_pk)

        client = httpx.Client(timeout=60)  # 60 seconds

        res = client.post(
            url=settings.TD_API_URL,
            headers={"Authorization": f"Bearer {settings.TD_API_TOKEN}"},
            json={
                "query": graphql_registry_V2_export_download_signed_url,
                "variables": {
                    "exportId": export.registry_export_id,
                },
            },
        )
        resp = res.json()
        try:
            url = resp["data"]["registryV2ExportDownloadSignedUrl"]["signedUrl"]
        except (TypeError, KeyError):
            messages.add_message(self.request, messages.ERROR, "Erreur, le registre n'a pu être téléchargé")
            return HttpResponseRedirect(reverse_lazy("registry_v2_prepare"))
        return HttpResponseRedirect(url)
