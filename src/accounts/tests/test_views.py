import pytest
from django.urls import reverse

from ..factories import DEFAULT_PASSWORD, UserFactory

pytestmark = pytest.mark.django_db

login_url = reverse("login")


def test_base_view_redirects_to_login(anon_client):
    res = anon_client.get(reverse("home"))
    assert res.status_code == 302
    assert res.url == reverse("login")


def test_login_view_get(anon_client):
    res = anon_client.get(login_url)
    assert res.status_code == 200


def test_login_view_denies_bad_password(anon_client):
    user = UserFactory()

    anon_client.post(login_url, {"email": user.email, "password": "JUNK"})
    assert "_auth_user_id" not in anon_client.session.keys()


def test_login_view_denies_inactive_user(anon_client):
    user = UserFactory(is_active=False)

    anon_client.post(login_url, {"email": user.email, "password": DEFAULT_PASSWORD})
    assert "_auth_user_id" not in anon_client.session.keys()


def test_login_view_accepts_good_password(anon_client):
    user = UserFactory()

    # Good password
    anon_client.post(login_url, {"email": user.email, "password": DEFAULT_PASSWORD})
    assert "_auth_user_id" in anon_client.session.keys()


def test_login_view_redirects_logged_in_user(logged_in_user):
    res = logged_in_user.get(login_url, follow=True)
    assert res.status_code == 200
    assert reverse("home") in res.redirect_chain[-1][0]
    assert res.redirect_chain[-1][1] == 302


def test_logout_view(logged_in_user):
    logout_url = reverse("logout")
    res = logged_in_user.get(logout_url, follow=True)
    assert res.status_code == 200
    assert reverse("login") in res.redirect_chain[-1][0]
    assert res.redirect_chain[-1][1] == 302
    assert "_auth_user_id" not in logged_in_user.session.keys()
