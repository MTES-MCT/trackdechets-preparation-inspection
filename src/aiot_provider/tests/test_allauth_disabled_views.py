import pytest
from django.urls import NoReverseMatch, reverse

pytestmark = pytest.mark.django_db


@pytest.mark.parametrize(
    "view_name",
    ["account_login", "account_inactive", "account_logout"],
)
def test_allauth_view_404(anon_client, view_name):
    res = anon_client.get(reverse(view_name))

    assert res.status_code == 404


def test_allauth_3rdparty_signup_404(anon_client):
    res = anon_client.get("accounts/3rdparty/signup/")

    assert res.status_code == 404


@pytest.mark.parametrize(
    "view_name",
    [
        "account_signup",
        "account_reauthenticate",
        "account_email_verification_sent",
        "account_confirm_email",
        "account_change_passwordaccount_set_password",
        "account_reset_password",
        "account_reset_password_done",
        "account_request_login_code",
        "account_confirm_login_code",
        "socialaccount_signup",
    ],
)
def test_allauth_view_disabled(anon_client, view_name):
    with pytest.raises(NoReverseMatch):
        reverse("account_signup")
