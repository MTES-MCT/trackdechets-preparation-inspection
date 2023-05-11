import pytest
from django.core import mail
from django.urls import reverse

from ..models import FeedbackResult

pytestmark = pytest.mark.django_db


def test_form_view_deny_anon(anon_client):
    url = reverse("feedback_form")
    res = anon_client.get(url)
    assert res.status_code == 302


def test_form_view_get(logged_in_user):
    url = reverse("feedback_form")
    res = logged_in_user.get(url)
    assert res.status_code == 200


def test_form_view_post(logged_in_user):
    url = reverse("feedback_form")
    res = logged_in_user.post(
        url, data={"was_useful": 2, "did_save_time": 4, "was_clear": 1}, follow=True
    )

    assert reverse("feedback_done") in res.redirect_chain[-1][0]
    result = FeedbackResult.objects.first()

    assert "Cette fiche vous a-t-elle été utile ? Ne se prononce pas" in result.content
    assert "Les informations présentées sont :  Peu compréhensibles" in result.content
    assert (
        "Par rapport à votre inspection, vous a-t-elle permis de : Gagner beaucoup de temps"
        in result.content
    )

    assert len(mail.outbox) == 1

    message = mail.outbox[0]
    assert message.subject == "Un utilisateur a rempli un formulaire de feedback"
    assert message.to == ["lorem@ipsum.lol"]
