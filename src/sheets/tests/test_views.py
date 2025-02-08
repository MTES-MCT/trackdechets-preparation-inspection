import datetime as dt

import pytest
from django.urls import reverse

from accounts.models import UserCategoryChoice
from content.models import FeedbackResult

from ..models import ComputedInspectionData

pytestmark = pytest.mark.django_db


def test_home_deny_anon(anon_client):
    url = reverse("private_home")
    res = anon_client.get(url)
    assert res.status_code == 302


def test_home(verified_user):
    url = reverse("private_home")
    res = verified_user.get(url)
    assert res.status_code == 200

    assert "Admin équipe" not in res.content.decode()


def test_home_observatoire(verified_observatoire):
    url = reverse("private_home")
    res = verified_observatoire.get(url)
    assert res.status_code == 200

    assert "Observatoires" in res.content.decode()


@pytest.mark.parametrize("get_client", ["verified_client", "logged_monaiot_client"], indirect=True)
def test_private_home_menu(get_client):
    url = reverse("private_home")
    res = get_client.get(url)
    assert res.status_code == 200

    assert "Établissements" in res.content.decode()
    assert "Préparer une fiche" in res.content.decode()
    assert "Registre" in res.content.decode()
    assert "Contrôle routier" in res.content.decode()
    assert "Bordereau" in res.content.decode()

    assert "Admin équipe" not in res.content.decode()
    assert "Observatoires" not in res.content.decode()
    assert "Cartographie" not in res.content.decode()

    assert "Guide" in res.content.decode()


@pytest.mark.parametrize("get_client", ["verified_client", "logged_monaiot_client"], indirect=True)
def test_private_home_menu_for_observatoire(get_client):
    user = get_client.user
    user.user_category = UserCategoryChoice.OBSERVATOIRE
    user.save()

    user.refresh_from_db()

    assert user.is_observatoire

    url = reverse("private_home")
    res = get_client.get(url)
    assert res.status_code == 200
    assert "Préparer une fiche" not in res.content.decode()

    assert "Bordereau" not in res.content.decode()

    assert "Admin équipe" not in res.content.decode()
    assert "Observatoires" in res.content.decode()
    assert "Contrôle routier" not in res.content.decode()
    assert "Cartographie" not in res.content.decode()
    assert "Bordereau" not in res.content.decode()
    assert "Guide" in res.content.decode()


def test_home_for_staff(verified_staff):
    url = reverse("private_home")
    res = verified_staff.get(url)
    assert res.status_code == 200

    assert "Admin équipe" in res.content.decode()
    assert "Observatoire" in res.content.decode()


def test_home_when_user_has_filled_survey(verified_user):
    url = reverse("private_home")

    FeedbackResult.objects.create(author=verified_user.user.email)

    res = verified_user.get(url)
    assert res.status_code == 200


def test_sheet_prepare_deny_anon(anon_client):
    url = reverse("sheet_prepare")
    res = anon_client.get(url)
    assert res.status_code == 302


def test_sheet_prepare_deny_observatoire(verified_observatoire):
    url = reverse("sheet_prepare")
    res = verified_observatoire.get(url)
    assert res.status_code == 403


@pytest.mark.parametrize("get_client", ["verified_client", "logged_monaiot_client"], indirect=True)
def test_sheet_prepare(get_client):
    url = reverse("sheet_prepare")
    res = get_client.get(url)
    assert res.status_code == 200
    form = res.context["form"]
    today = dt.date.today()
    assert form.initial == {
        "start_date": (today - dt.timedelta(days=365)).isoformat(),
        "end_date": today.isoformat(),
    }

    assert form.fields["siret"]
    assert form.fields["start_date"].widget.attrs == {"max": today.isoformat()}
    assert form.fields["end_date"].widget.attrs == {
        "max": dt.date(day=31, month=12, year=dt.date.today().year).isoformat()
    }

    content = res.content.decode()
    assert "id_siret" in content

    assert "id_start_date" in content
    assert "id_end_date" in content


@pytest.mark.parametrize("get_client", ["verified_client", "logged_monaiot_client"], indirect=True)
def test_sheet_prepare_post(get_client):
    url = reverse("sheet_prepare")
    res = get_client.post(
        url,
        data={
            "siret": "51212357100030",
            "start_date": "2024-01-01",
            "end_date": "2024-12-31",
        },
    )
    assert res.status_code == 302
    sheet = ComputedInspectionData.objects.get()
    assert res.url == reverse("pollable_result", args=["fake-task-id", str(sheet.id)])
