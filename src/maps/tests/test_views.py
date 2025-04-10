import pytest
from django.urls import reverse

pytestmark = pytest.mark.django_db


def test_map_view_deny_anon(anon_client):
    url = reverse("map_view")
    res = anon_client.get(url)
    assert res.status_code == 302


def test_map_view_deny_user(verified_user):
    url = reverse("map_view")
    res = verified_user.get(url)
    assert res.status_code == 403


def test_map_view(verified_staff):
    url = reverse("map_view")
    res = verified_staff.get(url)
    assert res.status_code == 200
