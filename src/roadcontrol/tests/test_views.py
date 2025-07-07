import pytest
from django.urls import reverse

from accounts.factories import UserFactory

from ..factories import BsdPdfFactory, PdfBundleFactory
from ..models import PdfBundle

pytestmark = pytest.mark.django_db


# Road control search


def test_roadcontrol_anon(anon_client):
    url = reverse("roadcontrol")
    res = anon_client.get(url)
    assert res.status_code == 302


def test_roadcontrol_observatoires(verified_observatoire):
    url = reverse("roadcontrol")
    res = verified_observatoire.get(url)
    assert res.status_code == 403


@pytest.mark.parametrize(
    "get_client", ["verified_client", "logged_monaiot_client", "logged_proconnect_client"], indirect=True
)
def test_roadcontrol(get_client):
    url = reverse("roadcontrol")
    res = get_client.get(url)
    assert res.status_code == 200

    assert "Rechercher un transport" in res.content.decode()


def test_roadcontrol_search_result_anon(anon_client):
    url = reverse("roadcontrol_search_result")
    res = anon_client.get(url)
    assert res.status_code == 302


def test_roadcontrol_search_result_observatoires(verified_observatoire):
    url = reverse("roadcontrol_search_result")
    res = verified_observatoire.get(url)
    assert res.status_code == 403


def test_roadcontrol_search_result(verified_user):
    url = reverse("roadcontrol_search_result")
    res = verified_user.get(url)
    assert res.status_code == 200


def test_roadcontrol_pdf_bundle_anon(anon_client):
    url = reverse("roadcontrol_pdf_bundle")
    res = anon_client.get(url)
    assert res.status_code == 302


def test_roadcontrol_pdf_observatoires(verified_observatoire):
    url = reverse("roadcontrol_pdf_bundle")
    res = verified_observatoire.get(url)
    assert res.status_code == 403


def test_roadcontrol_pdf_bundle(verified_user):
    url = reverse("roadcontrol_pdf_bundle")
    res = verified_user.get(url)
    assert res.status_code == 200


def test_roadcontrol_recent_pdfs_anon(anon_client):
    url = reverse("roadcontrol_recent_pdfs")
    res = anon_client.get(url)
    assert res.status_code == 302


def test_roadcontrol_recent_pdfs_observatoires(verified_observatoire):
    url = reverse("roadcontrol_pdf_bundle")
    res = verified_observatoire.get(url)
    assert res.status_code == 403


def test_roadcontrol_recent_pdfs(verified_user):
    other_user = UserFactory()
    other_bsd = BsdPdfFactory(created_by=other_user)
    individual_bsd = BsdPdfFactory(created_by=verified_user.user, request_type="BSD")
    other_bundle = PdfBundleFactory(created_by=other_user, state=PdfBundle.BundleChoice.READY)

    bsd = BsdPdfFactory(created_by=verified_user.user)
    bundle = PdfBundleFactory(created_by=verified_user.user, state=PdfBundle.BundleChoice.READY)
    non_ready_bundle = PdfBundleFactory(created_by=verified_user.user, state=PdfBundle.BundleChoice.PROCESSING)
    url = reverse("roadcontrol_recent_pdfs")
    res = verified_user.get(url)

    assert res.status_code == 200

    assert str(bsd.id) in res.content.decode()
    assert str(bundle.id) in res.content.decode()

    assert str(other_bsd.id) not in res.content.decode()
    assert str(other_bundle.id) not in res.content.decode()
    assert str(other_bundle.id) not in res.content.decode()
    assert str(non_ready_bundle.id) not in res.content.decode()
    assert str(individual_bsd.id) not in res.content.decode()


def test_roadcontrol_pdf_bundle_result_anon(anon_client):
    bundle = PdfBundleFactory(state=PdfBundle.BundleChoice.READY)
    url = reverse("roadcontrol_pdf_bundle_result", args=[bundle.pk])
    res = anon_client.get(url)
    assert res.status_code == 302


def test_roadcontrol_pdf_bundle_result(verified_user):
    bundle = PdfBundleFactory(created_by=verified_user.user, state=PdfBundle.BundleChoice.READY)

    url = reverse("roadcontrol_pdf_bundle_result", args=[bundle.pk])
    res = verified_user.get(url)
    assert res.status_code == 200

    other_user = UserFactory()
    other_bundle = PdfBundleFactory(created_by=other_user, state=PdfBundle.BundleChoice.READY)

    url = reverse("roadcontrol_pdf_bundle_result", args=[other_bundle.pk])
    res = verified_user.get(url)
    assert res.status_code == 404


# Bsd search


def test_bsd_search_anon(anon_client):
    url = reverse("roadcontrol_bsd_search")
    res = anon_client.get(url)
    assert res.status_code == 302


@pytest.mark.parametrize(
    "get_client", ["verified_client", "logged_monaiot_client", "logged_proconnect_client"], indirect=True
)
def test_bsd_search(get_client):
    url = reverse("roadcontrol_bsd_search")
    res = get_client.get(url)
    assert res.status_code == 200

    assert "Rechercher un bordereau" in res.content.decode()


def test_bsd_recent_pdfs_anon(anon_client):
    url = reverse("bsd_recent_pdfs")
    res = anon_client.get(url)
    assert res.status_code == 302


def test_bsd_recent_pdfs(verified_user):
    other_user = UserFactory()
    other_bsd = BsdPdfFactory(created_by=other_user)
    individual_bsd = BsdPdfFactory(created_by=verified_user.user, request_type="BSD")
    other_bundle = PdfBundleFactory(created_by=other_user, state=PdfBundle.BundleChoice.READY)

    bsd = BsdPdfFactory(created_by=verified_user.user)
    bundle = PdfBundleFactory(created_by=verified_user.user, state=PdfBundle.BundleChoice.READY)
    non_ready_bundle = PdfBundleFactory(created_by=verified_user.user, state=PdfBundle.BundleChoice.PROCESSING)
    url = reverse("bsd_recent_pdfs")
    res = verified_user.get(url)

    assert res.status_code == 200

    assert str(bsd.id) not in res.content.decode()
    assert str(bundle.id) not in res.content.decode()

    assert str(other_bsd.id) not in res.content.decode()
    assert str(other_bundle.id) not in res.content.decode()
    assert str(other_bundle.id) not in res.content.decode()
    assert str(non_ready_bundle.id) not in res.content.decode()
    assert str(individual_bsd.id) in res.content.decode()


def test_roadcontrol_bsd_search_result_anon(anon_client):
    url = reverse("roadcontrol_bsd_search_result")
    res = anon_client.get(url)
    assert res.status_code == 302


def test_roadcontrol_bsd_search_result(verified_user):
    url = reverse("roadcontrol_bsd_search_result")
    res = verified_user.get(url)
    assert res.status_code == 200


def test_single_bsd_pdf_download_anon(anon_client):
    url = reverse("single_bsd_pdf_download")
    res = anon_client.get(url)
    assert res.status_code == 302


@pytest.mark.parametrize(
    "get_profile",
    [
        "verified_icpe",
        "verified_ctt",
        "verified_inspection_travail",
        "verified_gendarme",
        "verified_ars",
        "verified_douane",
        "verified_adm_centrale",
    ],
    indirect=True,
)
def test_single_bsd_pdf_download_is_allowed(get_profile):
    url = reverse("single_bsd_pdf_download")
    res = get_profile.get(url)
    assert res.status_code == 200


@pytest.mark.parametrize(
    "get_profile",
    ["verified_observatoire"],
    indirect=True,
)
def test_single_bsd_pdf_download_is_denied(get_profile):
    url = reverse("single_bsd_pdf_download")
    res = get_profile.get(url)
    assert res.status_code == 403
