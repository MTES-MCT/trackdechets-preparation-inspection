import datetime as dt

import pytest
from django.urls import reverse

from content.models import FeedbackResult

from ..models import ComputedInspectionData

pytestmark = pytest.mark.django_db


def test_home_deny_anon(anon_client):
    url = reverse("private_home")
    res = anon_client.get(url)
    assert res.status_code == 302


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


@pytest.mark.parametrize(
    "get_client", ["verified_client", "logged_monaiot_client", "logged_proconnect_client"], indirect=True
)
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


@pytest.mark.parametrize(
    "get_client", ["verified_client", "logged_monaiot_client", "logged_proconnect_client"], indirect=True
)
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
