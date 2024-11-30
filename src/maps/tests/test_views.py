import pytest
from django.contrib.gis.geos import Point
from django.urls import reverse

from ..factories import CartoCompanyFactory

pytestmark = pytest.mark.django_db


def test_map_view_deny_anon(anon_client):
    url = reverse("map_view")
    res = anon_client.get(url)
    assert res.status_code == 302


def test_map_view(verified_user):
    url = reverse("map_view")
    res = verified_user.get(url)
    assert res.status_code == 200


##
def test_map_api_region_companies_deny_anon(api_anon):
    url = reverse("map_api_region_companies")
    res = api_anon.get(url)
    assert res.status_code == 403


def test_map_api_region_companies_deny_not_verified(logged_in_api):
    url = reverse("map_api_region_companies")
    res = logged_in_api.get(url)
    assert res.status_code == 403


def test_map_api_region_companies(verified_api):
    CartoCompanyFactory(code_region_insee="93", coords=Point(x=5.50, y=44.22))
    CartoCompanyFactory(code_region_insee="93", coords=Point(x=5.50, y=44.22))
    CartoCompanyFactory(code_region_insee="84", coords=Point(x=5.50, y=44.22))
    url = reverse("map_api_region_companies")
    res = verified_api.get(f"{url}?bounds=-5.14,42.332,8.2302,51.089")
    assert res.status_code == 200
    assert res.json() == [
        {"name": "Auvergne Rhône-Alpes", "lat": 45.51583333333333, "long": 4.538055555555555, "count": 1},
        {"name": "Provence-Alpes-Côte d'Azur", "lat": 43.955000000000005, "long": 6.053333333333333, "count": 2},
    ]


def test_map_api_department_companies_anon(api_anon):
    url = reverse("map_api_department_companies")
    res = api_anon.get(url)
    assert res.status_code == 403


def test_map_api_department_companies_deny_not_verified(logged_in_api):
    url = reverse("map_api_department_companies")
    res = logged_in_api.get(url)
    assert res.status_code == 403


def test_map_api_department_companies(verified_api):
    CartoCompanyFactory(code_departement_insee="83", coords=Point(x=5.50, y=43.22))
    CartoCompanyFactory(code_departement_insee="83", coords=Point(x=5.50, y=43.22))
    CartoCompanyFactory(code_departement_insee="13", coords=Point(x=5.50, y=43.22))
    url = reverse("map_api_department_companies")
    res = verified_api.get(
        f"{url}?bounds=4.666261723488475%2C42.96291945615462%2C7.741025145703958%2C44.28842293075769"
    )
    assert res.status_code == 200


##
def test_map_api_companies_deny_anon(api_anon):
    url = reverse("map_api_companies")
    res = api_anon.get(url)
    assert res.status_code == 403


def test_map_api_companies_deny_non_verified(logged_in_api):
    url = reverse("map_api_companies")
    res = logged_in_api.get(url)
    assert res.status_code == 403


def test_map_api_companies(verified_api):
    CartoCompanyFactory(coords=Point(x=55.30, y=-21.22))
    company = CartoCompanyFactory(coords=Point(x=55.50, y=-21.22))
    url = reverse("map_api_companies")
    res = verified_api.get(f"{url}?bounds=55.49,-21.23,55.5745,-21.191")
    assert res.status_code == 200
    assert len(res.json()) == 1
    assert res.json()[0]["siret"] == company.siret


def test_map_api_companies_clusters_anon(api_anon):
    url = reverse("map_api_companies_clusters")
    res = api_anon.get(url)
    assert res.status_code == 403


def test_map_api_companies_clusterss_deny_not_verified(logged_in_api):
    url = reverse("map_api_companies_clusters")
    res = logged_in_api.get(url)
    assert res.status_code == 403


def test_map_api_companies_clusters(verified_api):
    url = reverse("map_api_companies_clusters")
    res = verified_api.get(f"{url}?bounds=-3.781178100204727,37.65201444289751,27.600321844690427,50.94157957378454")

    assert res.status_code == 200
