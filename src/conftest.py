import pytest
from django_otp import DEVICE_ID_SESSION_KEY

from accounts.factories import DEFAULT_PASSWORD, EmailDeviceFactory, UserFactory


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
