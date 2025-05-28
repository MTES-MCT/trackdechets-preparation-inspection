import pytest
from django.urls import reverse

from common.models import SiteConfiguration

pytestmark = pytest.mark.django_db


def test_home(anon_client):
    config = SiteConfiguration.get_solo()

    url = reverse("public_home")
    res = anon_client.get(url)

    assert "lorem ipsum" not in res.content.decode()

    config.banner_content = "lorem ipsum"
    config.save()
    res = anon_client.get(url)
    assert "lorem ipsum" in res.content.decode()
