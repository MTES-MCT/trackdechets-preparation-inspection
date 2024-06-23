import pytest
from django.urls import reverse

from sheets.factories import ApiComputedInspectionDataFactory

pytestmark = pytest.mark.django_db


def test_api_sheet_detail_deny_anon(anon_client):
    sheet = ApiComputedInspectionDataFactory()
    url = reverse("api_sheet_detail", args=[sheet.pk])
    res = anon_client.get(url)
    assert res.status_code == 401  # denied


def test_api_sheet_detail(token_auth_api):
    sheet = ApiComputedInspectionDataFactory()
    url = reverse("api_sheet_detail", args=[sheet.pk])
    res = token_auth_api.get(url)
    assert res.status_code == 200


def test_api_sheet_create_deny_anon(anon_client):
    url = reverse("api_sheet_create")
    res = anon_client.post(url, data={})
    assert res.status_code == 401  # denied


def test_api_sheet_pdf_retrieve_deny_anon(anon_client):
    sheet = ApiComputedInspectionDataFactory()
    url = reverse("api_sheet_pdf_retrieve", args=[sheet.pk])
    res = anon_client.get(url)
    assert res.status_code == 401  # denied
