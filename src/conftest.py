import pytest

from accounts.factories import DEFAULT_PASSWORD, UserFactory


@pytest.fixture()
def anon_client(db):
    """A Django anonymous client."""
    from django.test.client import Client

    return Client()


@pytest.fixture()
def logged_in_user(db):
    """A Django test client logged in as a base user."""
    from django.test.client import Client

    user = UserFactory()
    client = Client()
    client.login(email=user.email, password=DEFAULT_PASSWORD)
    return client
