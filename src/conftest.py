import datetime as dt

import pytest
from allauth.socialaccount.models import SocialAccount
from django.utils import timezone
from django_otp import DEVICE_ID_SESSION_KEY
from rest_framework.authtoken.models import Token
from rest_framework.test import APIClient

from accounts.factories import DEFAULT_PASSWORD, ApiUserFactory, EmailDeviceFactory, UserFactory


@pytest.fixture()
def anon_client(db):
    """A Django anonymous client."""
    from django.test.client import Client

    return Client()


@pytest.fixture()
def logged_in_user(db):
    """A Django test client logged in as a base user (second factor not yet performed)."""
    from django.test.client import Client

    user = UserFactory()

    client = Client()
    client.login(email=user.email, password=DEFAULT_PASSWORD)

    setattr(client, "user", user)
    return client


@pytest.fixture()
def verified_user(logged_in_user):
    """A Django test client (basic user) who completed the second factor."""

    client = logged_in_user

    device = EmailDeviceFactory(user=client.user)
    session = client.session
    session[DEVICE_ID_SESSION_KEY] = device.persistent_id
    session.save()

    return client


@pytest.fixture()
def logged_in_staff(db):
    """A Django test client logged in as a staff user."""
    from django.test.client import Client

    user = UserFactory(is_staff=True)
    client = Client()
    client.login(email=user.email, password=DEFAULT_PASSWORD)

    setattr(client, "user", user)
    return client


@pytest.fixture()
def verified_staff(logged_in_staff):
    """A Django test client (staff) user) who completed the second factor."""

    client = logged_in_staff

    device = EmailDeviceFactory(user=client.user)
    session = client.session
    session[DEVICE_ID_SESSION_KEY] = device.persistent_id
    session.save()

    return client


@pytest.fixture()
def token_auth_api():
    """Return a DRF api client with token auth credentials"""
    user = ApiUserFactory()
    api = APIClient()
    token = Token.objects.create(user=user)

    api.credentials(HTTP_AUTHORIZATION=f"Token {token.key}")
    setattr(api, "user", user)
    return api


@pytest.fixture()
def monaiot_logged_in_user(db):
    """A Django test client logged in as a base user (second factor not yet performed)."""
    from django.test.client import Client

    user = UserFactory(monaiot_connexion=True)
    uid = f"xyz-{user.pk}"
    SocialAccount.objects.create(provider="monaiot", user=user, uid=uid)
    client = Client()
    client.login(email=user.email, password=DEFAULT_PASSWORD)

    now = timezone.now()
    ts = dt.datetime.timestamp(now)
    account_authentication_methods = [{"method": "socialaccount", "at": ts, "provider": "monaiot", "uid": uid}]
    session = client.session
    session["account_authentication_methods"] = account_authentication_methods
    session.save()

    setattr(client, "user", user)
    return client


@pytest.fixture()
def get_client(
    monaiot_logged_in_user,
    verified_user,
    request,
):
    """This fixture allows to easily run test with multiple clients.

    Just decorate your test with
    `@pytest.mark.parametrize('get_client', ['verified_client', 'logged_monaiot_user'], indirect=True)`
    """
    clients = {
        "verified_client": verified_user,
        "logged_monaiot_client": monaiot_logged_in_user,
    }
    return clients.get(request.param)


@pytest.fixture()
def api_anon():
    """Return a DRF api client."""
    api = APIClient()
    return api


@pytest.fixture()
def logged_in_api():
    """Return a DRF api client with an already logged in (not verified)  user."""

    user = UserFactory()

    api = APIClient()
    api.login(email=user.email, password=DEFAULT_PASSWORD)

    setattr(api, "user", user)
    return api


@pytest.fixture()
def verified_api(logged_in_api):
    """Return a DRF api client with an already verified user."""

    client = logged_in_api

    device = EmailDeviceFactory(user=client.user)
    session = client.session
    session[DEVICE_ID_SESSION_KEY] = device.persistent_id
    session.save()

    return client
