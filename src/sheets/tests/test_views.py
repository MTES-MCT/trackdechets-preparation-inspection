import datetime as dt

import pytest
from django.urls import reverse

from content.models import FeedbackResult

pytestmark = pytest.mark.django_db


def test_home_deny_anon(anon_client):
    url = reverse("private_home")
    res = anon_client.get(url)
    assert res.status_code == 302


def test_home(verified_user):
    url = reverse("private_home")
    res = verified_user.get(url)
    assert res.status_code == 200
    assert "Préparer une fiche" in res.content.decode()

    assert "Interface d'administration équipe" not in res.content.decode()

    assert "Aidez-nous à améliorer cet outil" in res.content.decode()


@pytest.mark.parametrize("get_client", ["verified_client", "logged_monaiot_client"], indirect=True)
def test_home_aiot_user(get_client):
    url = reverse("private_home")
    res = get_client.get(url)
    assert res.status_code == 200
    assert "Préparer une fiche" in res.content.decode()

    assert "Interface d'administration équipe" not in res.content.decode()

    assert "Aidez-nous à améliorer cet outil" in res.content.decode()


def test_home_for_staff(verified_staff):
    url = reverse("private_home")
    res = verified_staff.get(url)
    assert res.status_code == 200

    assert "Interface d'administration équipe" in res.content.decode()


def test_home_when_user_has_filled_survey(verified_user):
    url = reverse("private_home")

    FeedbackResult.objects.create(author=verified_user.user.email)

    res = verified_user.get(url)
    assert res.status_code == 200
    assert "Aidez-nous à améliorer cet outil" in res.content.decode()


def test_sheet_prepare_deny_anon(anon_client):
    url = reverse("prepare")
    res = anon_client.get(url)
    assert res.status_code == 302


@pytest.mark.parametrize("get_client", ["verified_client", "logged_monaiot_client"], indirect=True)
def test_sheet_prepare(get_client):
    url = reverse("prepare")
    res = get_client.get(url)
    assert res.status_code == 200
    form = res.context["form"]
    today = dt.date.today()
    assert form.initial == {
        "start_date": (today - dt.timedelta(days=365)).isoformat(),
        "end_date": today.isoformat(),
    }

    assert form.fields["start_date"].widget.attrs == {"max": today.isoformat()}
    assert form.fields["end_date"].widget.attrs == {
        "max": dt.date(day=31, month=12, year=dt.date.today().year).isoformat()
    }
