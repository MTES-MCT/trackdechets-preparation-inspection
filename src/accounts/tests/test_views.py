import pytest
from django.urls import reverse

pytestmark = pytest.mark.django_db


def test_base_view(anon_client):
    res = anon_client.get(reverse("base"))
    assert res.status_code == 200
