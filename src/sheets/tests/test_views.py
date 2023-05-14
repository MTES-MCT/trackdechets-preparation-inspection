import pytest
from django.urls import reverse

from content.models import FeedbackResult

pytestmark = pytest.mark.django_db


def test_home_deny_anon(anon_client):
    url = reverse("home")
    res = anon_client.get(url)
    assert res.status_code == 302


def test_home(logged_in_user):
    url = reverse("home")
    res = logged_in_user.get(url)
    assert res.status_code == 200
    assert "Préparer une fiche" in res.content.decode()

    assert "Interface d'administration équipe" not in res.content.decode()

    # User did not fill survey
    assert "Aidez-nous à améliorer cet outil" in res.content.decode()


def test_home_for_staff(logged_in_staff):
    url = reverse("home")
    res = logged_in_staff.get(url)
    assert res.status_code == 200

    assert "Interface d'administration équipe" in res.content.decode()


def test_home_when_user_has_filled_survey(logged_in_user):
    url = reverse("home")

    FeedbackResult.objects.create(author=logged_in_user.user.email)

    res = logged_in_user.get(url)
    assert res.status_code == 200
    assert "Aidez-nous à améliorer cet outil" not in res.content.decode()
