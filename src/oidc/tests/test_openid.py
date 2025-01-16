import datetime as dt
from unittest.mock import patch

import pytest
from django.contrib import auth
from django.urls import reverse

from accounts.factories import UserFactory
from accounts.models import User, UserCategoryChoice, UserTypeChoice

from ..models import OidcLogin, ProviderChoice

pytestmark = pytest.mark.django_db

token_response = {
    "access_token": "access_token_123",
    "id_token": "id_token_456",
    "refresh_token": "refresh_token_789",
    "expires_in": 3600,
    "token_type": "Bearer",
}

default_droits = '[{"profil" : "Administrateur", "id_profil" : 2, "application" : "GUNenv", "id_application" : 3, "nature_service" : "D(R)EAL, DRIEE ou DGTM", "id_nature_service" : 1, "etablissement" : null, "code_entite" : "EQ00051", "bassin" : null, "region" : "28", "departement" : null, "commune" : null, "station_epuration" : null, "code_sandre" : null, "perimetre_ic" : "ICPE", "droits_etendus" : null}]'


def verify_token_response(user_email, droits=default_droits):
    return {
        "exp": (dt.datetime.now() + dt.timedelta(hours=1)).timestamp(),
        "iat": dt.datetime.now().timestamp(),
        "auth_time": dt.datetime.now().timestamp(),
        "jti": "ec12e3bd-413f-4e4f-a66e-8f54ab5194bd",
        "iss": "https://lorem.dev",
        "aud": "trackdechets",
        "sub": "f:abcd",
        "typ": "ID",
        "azp": "trackdechets",
        "nonce": "xyz",
        "session_state": "abcded",
        "at_hash": "NrKm5E7vS_6jr9mc8CIOSw",
        "acr": "0",
        "sid": "abcd",
        "email_verified": False,
        "name": "Compte test 1 TrackDechets",
        "droits": droits,
        "preferred_username": user_email,
        "given_name": "Compte test 1",
        "family_name": "TrackDechets",
        "email": user_email,
    }


def user_info(user_email, droits=default_droits):
    return {
        "sub": "f:abcd",
        "email_verified": False,
        "name": "Compte test 1 TrackDechets",
        "droits": droits,
        "preferred_username": user_email,
        "given_name": "Compte test 1",
        "family_name": "TrackDechets",
        "email": user_email,
    }


def test_oidc_auth_request(anon_client):
    """Test that the OIDC authentication request redirects to the provider."""
    login_url = reverse("oidc_authentication_init")
    response = anon_client.get(login_url)

    assert response.status_code == 302
    assert response["Location"].startswith(
        "https://monaiot.test/auth/realms/MonAIOT-integration/protocol/openid-connect/auth?response_type=code"
    )


@patch("mozilla_django_oidc.auth.OIDCAuthenticationBackend.get_token")
@patch("mozilla_django_oidc.auth.OIDCAuthenticationBackend.verify_token")
@patch("mozilla_django_oidc.auth.OIDCAuthenticationBackend.get_userinfo")
def test_oidc_callback_success_when_user_exists(
    mock_get_userinfo,
    mock_verify_token,
    mock_get_token,
    anon_client,
):
    """Test successful OIDC authentication callback."""

    user = UserFactory(monaiot_signup=True)
    mock_get_token.return_value = token_response

    mock_verify_token.return_value = verify_token_response(user.email)

    mock_get_userinfo.return_value = user_info(user.email)

    session = anon_client.session
    session["oidc_states"] = {"state_xyz": {"code_verifier": None, "nonce": "xyz"}}
    session.save()

    callback_url = reverse("oidc_authentication_callback")
    response = anon_client.get(callback_url, {"code": "auth_code_123", "state": "state_xyz"})

    assert response.status_code == 302
    assert response["Location"] == reverse("private_home")  # Default redirect URL

    logged_user = auth.get_user(anon_client)
    assert logged_user.is_authenticated

    user = User.objects.get(email=user.email)
    assert OidcLogin.objects.get(user=user, provider=ProviderChoice.MONAIOT, account_created=False)

    assert user.monaiot_connexion


@patch("mozilla_django_oidc.auth.OIDCAuthenticationBackend.get_token")
@patch("mozilla_django_oidc.auth.OIDCAuthenticationBackend.verify_token")
@patch("mozilla_django_oidc.auth.OIDCAuthenticationBackend.get_userinfo")
def test_oidc_callback_success_when_user_does_not_exist(
    mock_get_userinfo,
    mock_verify_token,
    mock_get_token,
    anon_client,
):
    """Test successful OIDC authentication callback."""
    user_email = "newuser@email.test"
    mock_get_token.return_value = token_response

    mock_verify_token.return_value = verify_token_response(user_email)

    mock_get_userinfo.return_value = user_info(user_email)

    session = anon_client.session
    session["oidc_states"] = {"state_xyz": {"code_verifier": None, "nonce": "xyz"}}
    session.save()

    callback_url = reverse("oidc_authentication_callback")
    response = anon_client.get(callback_url, {"code": "auth_code_123", "state": "state_xyz"})

    assert response.status_code == 302
    assert response["Location"] == reverse("private_home")  # Default redirect URL

    # Verify user was created
    user = User.objects.get(email=user_email)
    assert user
    assert user.monaiot_signup
    assert user.is_active
    assert not user.is_staff
    assert not user.is_superuser
    assert user.user_type == UserTypeChoice.HUMAN
    assert user.user_category == UserCategoryChoice.INSPECTEUR_ICPE


# fails


@patch("mozilla_django_oidc.auth.OIDCAuthenticationBackend.get_token")
@patch("mozilla_django_oidc.auth.OIDCAuthenticationBackend.verify_token")
@patch("mozilla_django_oidc.auth.OIDCAuthenticationBackend.get_userinfo")
def test_oidc_callback_fails_when_no_droits(
    mock_get_userinfo,
    mock_verify_token,
    mock_get_token,
    anon_client,
):
    """Test failed OIDC authentication callback."""

    user = UserFactory(monaiot_signup=True)
    mock_get_token.return_value = token_response

    mock_verify_token.return_value = verify_token_response(user.email, droits="")

    mock_get_userinfo.return_value = user_info(user.email, droits="")

    session = anon_client.session
    session["oidc_states"] = {"state_xyz": {"code_verifier": None, "nonce": "xyz"}}
    session.save()

    callback_url = reverse("oidc_authentication_callback")
    response = anon_client.get(callback_url, {"code": "auth_code_123", "state": "state_xyz"})

    assert response.status_code == 302
    assert response["Location"] == reverse("mon_aiot_authent_error")  # Default redirect URL
    logged_user = auth.get_user(anon_client)
    assert not logged_user.is_authenticated

    user = User.objects.get(email=user.email)

    assert not user.monaiot_connexion


@patch("mozilla_django_oidc.auth.OIDCAuthenticationBackend.get_token")
@patch("mozilla_django_oidc.auth.OIDCAuthenticationBackend.verify_token")
@patch("mozilla_django_oidc.auth.OIDCAuthenticationBackend.get_userinfo")
def test_oidc_callback_fails_when_wrong_id_profile(
    mock_get_userinfo,
    mock_verify_token,
    mock_get_token,
    anon_client,
):
    """Test failed OIDC authentication callback."""

    user = UserFactory(monaiot_signup=True)
    mock_get_token.return_value = token_response
    droits = '[{"profil" : "Gestionnaire", "id_profil" : 1, "application" : "GUNenv", "id_application" : 2, "nature_service" : "D(R)EAL, DRIEE ou DGTM", "id_nature_service" : 1, "etablissement" : null, "service_s3ic" : null, "code_entite" : null, "bassin" : null, "region" : "75", "departement" : null, "commune" : null, "station_epuration" : null, "code_sandre" : null, "perimetre_ic" : "ICPE", "droits_etendus" : null}]'

    mock_verify_token.return_value = verify_token_response(user.email, droits=droits)

    mock_get_userinfo.return_value = user_info(user.email, droits=droits)

    session = anon_client.session
    session["oidc_states"] = {"state_xyz": {"code_verifier": None, "nonce": "xyz"}}
    session.save()

    callback_url = reverse("oidc_authentication_callback")
    response = anon_client.get(callback_url, {"code": "auth_code_123", "state": "state_xyz"})

    assert response.status_code == 302
    assert response["Location"] == reverse("mon_aiot_authent_error")  # Default redirect URL
    logged_user = auth.get_user(anon_client)
    assert not logged_user.is_authenticated

    user = User.objects.get(email=user.email)

    assert not user.monaiot_connexion


@patch("mozilla_django_oidc.auth.OIDCAuthenticationBackend.get_token")
@patch("mozilla_django_oidc.auth.OIDCAuthenticationBackend.verify_token")
@patch("mozilla_django_oidc.auth.OIDCAuthenticationBackend.get_userinfo")
def test_oidc_callback_fails_when_invalid_perimeter(
    mock_get_userinfo,
    mock_verify_token,
    mock_get_token,
    anon_client,
):
    """Test failed OIDC authentication callback."""

    user = UserFactory(monaiot_signup=True)
    mock_get_token.return_value = token_response
    # invalid perimetre_ic
    droits = '[{"profil" : "Administrateur", "id_profil" : 2, "application" : "GUNenv", "id_application" : 3, "nature_service" : "D(R)EAL, DRIEE ou DGTM", "id_nature_service" : 1, "etablissement" : null, "code_entite" : "EQ00051", "bassin" : null, "region" : "28", "departement" : null, "commune" : null, "station_epuration" : null, "code_sandre" : null, "perimetre_ic" : "INVALID", "droits_etendus" : null}  ]'

    mock_verify_token.return_value = verify_token_response(user.email, droits=droits)

    mock_get_userinfo.return_value = user_info(user.email, droits=droits)

    session = anon_client.session
    session["oidc_states"] = {"state_xyz": {"code_verifier": None, "nonce": "xyz"}}
    session.save()

    callback_url = reverse("oidc_authentication_callback")
    response = anon_client.get(callback_url, {"code": "auth_code_123", "state": "state_xyz"})

    assert response.status_code == 302
    assert response["Location"] == reverse("mon_aiot_authent_error")  # Default redirect URL
    logged_user = auth.get_user(anon_client)
    assert not logged_user.is_authenticated

    user = User.objects.get(email=user.email)

    assert not user.monaiot_connexion


@patch("mozilla_django_oidc.auth.OIDCAuthenticationBackend.get_token")
@patch("mozilla_django_oidc.auth.OIDCAuthenticationBackend.verify_token")
@patch("mozilla_django_oidc.auth.OIDCAuthenticationBackend.get_userinfo")
def test_oidc_callback_fails_when_gun_reader_and_wrong_id_applications(
    mock_get_userinfo,
    mock_verify_token,
    mock_get_token,
    anon_client,
):
    user = UserFactory(monaiot_signup=True)
    mock_get_token.return_value = token_response
    # id_profil : 6,
    # id_application : 2 (wrong)
    # id_nature_service : 59
    droits = '[{"profil" : "Gestionnaire", "id_profil" : 6, "application" : "GUNenv", "id_application" : 2, "nature_service" : "D(R)EAL, DRIEE ou DGTM", "id_nature_service" : 1, "etablissement" : null, "service_s3ic" : null, "code_entite" : null, "bassin" : null, "region" : "75", "departement" : null, "commune" : null, "station_epuration" : null, "code_sandre" : null, "perimetre_ic" : "ICPE", "droits_etendus" : null}]'

    mock_verify_token.return_value = verify_token_response(user.email, droits=droits)

    mock_get_userinfo.return_value = user_info(user.email, droits=droits)

    session = anon_client.session
    session["oidc_states"] = {"state_xyz": {"code_verifier": None, "nonce": "xyz"}}
    session.save()

    callback_url = reverse("oidc_authentication_callback")
    response = anon_client.get(callback_url, {"code": "auth_code_123", "state": "state_xyz"})

    assert response.status_code == 302
    assert response["Location"] == reverse("mon_aiot_authent_error")  # Default redirect URL
    logged_user = auth.get_user(anon_client)
    assert not logged_user.is_authenticated

    user = User.objects.get(email=user.email)

    assert not user.monaiot_connexion


@patch("mozilla_django_oidc.auth.OIDCAuthenticationBackend.get_token")
@patch("mozilla_django_oidc.auth.OIDCAuthenticationBackend.verify_token")
@patch("mozilla_django_oidc.auth.OIDCAuthenticationBackend.get_userinfo")
def test_oidc_callback_fails_when_gun_reader_and_wrong_id_nature_service(
    mock_get_userinfo,
    mock_verify_token,
    mock_get_token,
    anon_client,
):
    user = UserFactory(monaiot_signup=True)
    mock_get_token.return_value = token_response
    # id_profil : 6,
    # id_application : 3
    # id_nature_service : 51 (wrong)
    droits = '[{"profil" : "Gestionnaire", "id_profil" : 6, "application" : "GUNenv", "id_application" : 59, "nature_service" : "D(R)EAL, DRIEE ou DGTM", "id_nature_service" : 1, "etablissement" : null, "service_s3ic" : null, "code_entite" : null, "bassin" : null, "region" : "75", "departement" : null, "commune" : null, "station_epuration" : null, "code_sandre" : null, "perimetre_ic" : "ICPE", "droits_etendus" : null}]'

    mock_verify_token.return_value = verify_token_response(user.email, droits=droits)

    mock_get_userinfo.return_value = user_info(user.email, droits=droits)

    session = anon_client.session
    session["oidc_states"] = {"state_xyz": {"code_verifier": None, "nonce": "xyz"}}
    session.save()

    callback_url = reverse("oidc_authentication_callback")
    response = anon_client.get(callback_url, {"code": "auth_code_123", "state": "state_xyz"})

    assert response.status_code == 302
    assert response["Location"] == reverse("mon_aiot_authent_error")  # Default redirect URL
    logged_user = auth.get_user(anon_client)
    assert not logged_user.is_authenticated

    user = User.objects.get(email=user.email)

    assert not user.monaiot_connexion


@patch("mozilla_django_oidc.auth.OIDCAuthenticationBackend.get_token")
@patch("mozilla_django_oidc.auth.OIDCAuthenticationBackend.verify_token")
@patch("mozilla_django_oidc.auth.OIDCAuthenticationBackend.get_userinfo")
def test_oidc_callback_success_when_gun_reader_and_correct_parameters(
    mock_get_userinfo,
    mock_verify_token,
    mock_get_token,
    anon_client,
):
    """Test successful OIDC authentication callback."""

    user = UserFactory(monaiot_signup=True)
    mock_get_token.return_value = token_response

    # id_profil : 6,
    # id_application : 3
    # id_nature_service : 59
    droits = '[{"profil" : "Gestionnaire", "id_profil" : 6, "application" : "GUNenv", "id_application" : 3, "nature_service" : "D(R)EAL, DRIEE ou DGTM", "id_nature_service" : 59, "etablissement" : null, "service_s3ic" : null, "code_entite" : null, "bassin" : null, "region" : "75", "departement" : null, "commune" : null, "station_epuration" : null, "code_sandre" : null, "perimetre_ic" : "ICPE", "droits_etendus" : null}]'

    mock_verify_token.return_value = verify_token_response(user.email, droits=droits)

    mock_get_userinfo.return_value = user_info(user.email, droits=droits)

    session = anon_client.session
    session["oidc_states"] = {"state_xyz": {"code_verifier": None, "nonce": "xyz"}}
    session.save()

    callback_url = reverse("oidc_authentication_callback")
    response = anon_client.get(callback_url, {"code": "auth_code_123", "state": "state_xyz"})

    assert response.status_code == 302
    assert response["Location"] == reverse("private_home")  # Default redirect URL

    logged_user = auth.get_user(anon_client)
    assert logged_user.is_authenticated

    user = User.objects.get(email=user.email)

    assert user.monaiot_connexion
