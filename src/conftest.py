import pytest

from accounts.factories import DEFAULT_PASSWORD, UserFactory


@pytest.fixture()
def anon_client(db):
    """A Django anonymous client."""
    from django.test.client import Client

    return Client()


@pytest.fixture()
def logged_in_superadmin(db):
    """A Django test client logged in as a superadmin."""
    from django.test.client import Client

    user = UserFactory()
    client = Client()
    client.login(email=user.email, password="passpass")
    return client
