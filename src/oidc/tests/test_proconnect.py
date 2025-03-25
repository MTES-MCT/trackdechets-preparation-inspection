import datetime as dt
from unittest.mock import patch

import pytest
from django.contrib import auth
from django.urls import reverse

from accounts.constants import UserCategoryChoice
from accounts.factories import UserFactory
from accounts.models import User

from ..constants import ProviderChoice
from ..models import OidcLogin

pytestmark = pytest.mark.django_db

token_response = {
    "access_token": "access_token_123",
    "id_token": "id_token_456",
    "expires_in": 60,
    "refresh_token": "refresh_token_789",
    "scope": "openid email given_name usual_name uid siret idp_id organizational_unit belonging_population custom",
    "token_type": "Bearer",
}


def test__callback_url():
    # let's ensure we did not change inadvertently
    assert reverse("proconnect_oidc_authentication_callback") == "/oidc/proconnect-callback/"


def verify_token_response():
    return {
        "sub": "abcd-efgh1",
        "auth_time": dt.datetime.now().timestamp(),
        "nonce": "9chboIL4E9eHwbqjLQx9IX1zKtrXVtmF",
        "at_hash": "vd8Eew-y2KJj54S6WNXD5w",
        "aud": "a97c7538-c285-42b0-b2d5-a9171eae1a28",
        "exp": (dt.datetime.now() + dt.timedelta(hours=1)).timestamp(),
        "iat": dt.datetime.now().timestamp(),
        "iss": "https://proconnect.test/api/v2",
    }


def user_info(user_email):
    return {
        "sub": "abcd-efgh2",
        "email": user_email,
        "given_name": "John",
        "usual_name": "Doe",
        "uid": "123",
        "siret": "567",
        "idp_id": "currasso-idp",
        "custom": {"email_verified": True, "phone_number_verified": False},
        "aud": "a97c7538-c285-42b0-b2d5-a9171eae1a28",
        "exp": (dt.datetime.now() + dt.timedelta(hours=1)).timestamp(),
        "iat": dt.datetime.now().timestamp(),
        "iss": "https://proconnect.test/api/v2",
    }


def test_proconnect_oidc_auth_request(anon_client):
    """Test that the OIDC authentication request redirects to the provider."""
    login_url = reverse("proconnect_oidc_authentication_init")
    response = anon_client.get(login_url)

    assert response.status_code == 302
    assert response["Location"].startswith("https://proconnect.test/api/v2/authorize?response_type=code&scope=openid")


@patch("oidc.backends.ProconnectOidcBackend.get_token")
@patch("oidc.backends.ProconnectOidcBackend.verify_token")
@patch("oidc.backends.ProconnectOidcBackend.get_userinfo")
def test_proconnect_oidc_callback_success_when_user_exists(
    mock_get_userinfo,
    mock_verify_token,
    mock_get_token,
    anon_client,
):
    """Test successful OIDC authentication callback."""

    user = UserFactory(oidc_signup="PROCONNECT", user_category="GENDARMERIE")
    mock_get_token.return_value = token_response

    mock_verify_token.return_value = verify_token_response()
    user_info_value = user_info(user.email)
    mock_get_userinfo.return_value = user_info_value

    session = anon_client.session
    session["oidc_states"] = {
        "state_xyz": {"code_verifier": None, "nonce": "xyz", "added_on": dt.datetime.now().timestamp()}
    }

    session.save()

    callback_url = reverse("proconnect_oidc_authentication_callback")
    response = anon_client.get(callback_url, {"code": "auth_code_123", "state": "state_xyz"})

    assert response.status_code == 302
    assert response["Location"] == reverse("private_home")

    logged_user = auth.get_user(anon_client)
    assert logged_user.is_authenticated

    user = User.objects.get(email=user.email)
    oidc_login = OidcLogin.objects.get(user=user, provider=ProviderChoice.PROCONNECT, account_created=False)
    assert oidc_login.info == user_info_value
    assert user.oidc_connexion == "PROCONNECT"


@pytest.mark.parametrize(
    "user_category", [choice for choice in UserCategoryChoice if choice != UserCategoryChoice.GENDARMERIE]
)
@patch("oidc.backends.ProconnectOidcBackend.get_token")
@patch("oidc.backends.ProconnectOidcBackend.verify_token")
@patch("oidc.backends.ProconnectOidcBackend.get_userinfo")
def test_proconnect_oidc_callback_fails_when_user_is_not_gendarmerie(
    mock_get_userinfo,
    mock_verify_token,
    mock_get_token,
    user_category,
    anon_client,
):
    # A user exists, workflow is correct, but user category is not GENDARME: deny access
    user = UserFactory(oidc_signup="PROCONNECT", user_category=user_category)
    mock_get_token.return_value = token_response

    mock_verify_token.return_value = verify_token_response()

    mock_get_userinfo.return_value = user_info(user.email)

    session = anon_client.session
    session["oidc_states"] = {
        "state_xyz": {"code_verifier": None, "nonce": "xyz", "added_on": dt.datetime.now().timestamp()}
    }

    session.save()

    callback_url = reverse("proconnect_oidc_authentication_callback")
    response = anon_client.get(callback_url, {"code": "auth_code_123", "state": "state_xyz"})

    assert response.status_code == 302
    assert response["Location"] == reverse("proconnect_authent_error")

    logged_user = auth.get_user(anon_client)
    assert not logged_user.is_authenticated

    user = User.objects.get(email=user.email)
    assert not OidcLogin.objects.filter(user=user)

    logged_user = auth.get_user(anon_client)
    assert not logged_user.is_authenticated

    assert not user.oidc_connexion


@patch("oidc.backends.ProconnectOidcBackend.get_token")
@patch("oidc.backends.ProconnectOidcBackend.verify_token")
@patch("oidc.backends.ProconnectOidcBackend.get_userinfo")
def test_proconnect_oidc_callback_creates_user_when_user_does_not_exist(
    mock_get_userinfo,
    mock_verify_token,
    mock_get_token,
    anon_client,
):
    user_email = "newuser@email.test"

    # sanity check
    assert not User.objects.filter(email=user_email).exists()
    mock_get_token.return_value = token_response

    mock_verify_token.return_value = verify_token_response()
    user_info_value = user_info(user_email)
    mock_get_userinfo.return_value = user_info_value

    session = anon_client.session
    session["oidc_states"] = {
        "state_xyz": {"code_verifier": None, "nonce": "xyz", "added_on": dt.datetime.now().timestamp()}
    }
    session.save()

    callback_url = reverse("proconnect_oidc_authentication_callback")
    response = anon_client.get(callback_url, {"code": "auth_code_123", "state": "state_xyz"})

    assert response.status_code == 302
    assert response["Location"] == reverse("private_home")

    logged_user = auth.get_user(anon_client)
    assert logged_user.is_authenticated

    user = User.objects.get(email=user_email)
    oidc_login = OidcLogin.objects.get(user=user, provider=ProviderChoice.PROCONNECT, account_created=True)
    assert oidc_login.info == user_info_value
    assert user.oidc_connexion == "PROCONNECT"


@patch("oidc.backends.ProconnectOidcBackend.get_token")
@patch("oidc.backends.ProconnectOidcBackend.verify_token")
@patch("oidc.backends.ProconnectOidcBackend.get_userinfo")
def test_proconnect_oidc_callback_fails_when_no_idp_id(
    mock_get_userinfo,
    mock_verify_token,
    mock_get_token,
    anon_client,
):
    """Test failed OIDC authentication callback."""

    user = UserFactory(oidc_signup="PROCONNECT")
    mock_get_token.return_value = token_response

    mock_verify_token.return_value = verify_token_response()

    info = user_info(user.email)
    del info["idp_id"]
    mock_get_userinfo.return_value = info

    session = anon_client.session
    session["oidc_states"] = {
        "state_xyz": {"code_verifier": None, "nonce": "xyz", "added_on": dt.datetime.now().timestamp()}
    }
    session.save()

    callback_url = reverse("proconnect_oidc_authentication_callback")
    response = anon_client.get(callback_url, {"code": "auth_code_123", "state": "state_xyz"})

    assert response.status_code == 302
    assert response["Location"] == reverse("proconnect_authent_error")
    logged_user = auth.get_user(anon_client)
    assert not logged_user.is_authenticated

    user = User.objects.get(email=user.email)

    assert not user.oidc_connexion == "PROCONNECT"


@patch("oidc.backends.ProconnectOidcBackend.get_token")
@patch("oidc.backends.ProconnectOidcBackend.verify_token")
@patch("oidc.backends.ProconnectOidcBackend.get_userinfo")
def test_proconnect_oidc_callback_fails_when_idp_id_is_incorrect(
    mock_get_userinfo,
    mock_verify_token,
    mock_get_token,
    anon_client,
):
    """Test failed OIDC authentication callback."""

    user = UserFactory(oidc_signup="PROCONNECT")
    mock_get_token.return_value = token_response

    mock_verify_token.return_value = verify_token_response()

    info = user_info(user.email)

    mock_get_userinfo.return_value = {**info, "idp_id": "plop"}

    session = anon_client.session
    session["oidc_states"] = {"state_xyz": {"code_verifier": None, "nonce": "xyz"}}
    session.save()

    callback_url = reverse("proconnect_oidc_authentication_callback")
    response = anon_client.get(callback_url, {"code": "auth_code_123", "state": "state_xyz"})

    assert response.status_code == 302
    assert response["Location"] == reverse("proconnect_authent_error")
    logged_user = auth.get_user(anon_client)
    assert not logged_user.is_authenticated

    user = User.objects.get(email=user.email)

    assert not user.oidc_connexion == "PROCONNECT"
