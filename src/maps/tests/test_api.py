from operator import itemgetter

import pytest
from django.contrib.gis.geos import Point
from django.urls import reverse

from maps.factories import CartoCompanyFactory

pytestmark = pytest.mark.django_db


def test_map_api_objects_deny_anon(api_anon):
    url = reverse("map_api_objects")
    res = api_anon.get(url)
    assert res.status_code == 403


def test_map_api_objects_deny_not_verified(logged_in_api):
    url = reverse("map_api_objects")
    res = logged_in_api.get(url)
    assert res.status_code == 403


def test_map_api_region_companies(verified_api):
    CartoCompanyFactory(code_region_insee="93", coords=Point(x=5.50, y=44.22))
    CartoCompanyFactory(code_region_insee="93", coords=Point(x=5.50, y=44.22))
    CartoCompanyFactory(code_region_insee="84", coords=Point(x=5.50, y=44.22))
    url = reverse("map_api_objects")
    res = verified_api.get(f"{url}?bounds=-5.14,42.332,8.2302,51.089")  # bounds have no filtering effect
    assert res.status_code == 200
    data = res.json()

    assert data["companies"] == []
    assert data["total_count"] == 3

    assert sorted(data["clusters"], key=itemgetter("name")) == sorted(
        [
            {"name": "Provence-Alpes-Côte d'Azur", "lat": 43.955000000000005, "long": 6.053333333333333, "count": 2},
            {"name": "Auvergne Rhône-Alpes", "lat": 45.51583333333333, "long": 4.538055555555555, "count": 1},
        ],
        key=itemgetter("name"),
    )


def test_map_api_department_companies(verified_api):
    CartoCompanyFactory(code_departement_insee="83", coords=Point(x=5.50, y=43.22))
    CartoCompanyFactory(code_departement_insee="83", coords=Point(x=5.50, y=43.22))
    CartoCompanyFactory(code_departement_insee="13", coords=Point(x=5.50, y=43.22))
    url = reverse("map_api_objects")

    res = verified_api.get(
        f"{url}?bounds=4.666261723488475%2C42.96291945615462%2C7.741025145703958%2C44.28842293075769"
    )
    assert res.status_code == 200
    data = res.json()

    assert data["companies"] == []
    assert data["total_count"] == 3

    assert sorted(data["clusters"], key=itemgetter("name")) == sorted(
        [
            {"name": "Bouches-du-Rhône", "lat": 43.54333333333333, "long": 5.086388888888888, "count": 1},
            {"name": "Var", "lat": 43.46055555555556, "long": 6.218055555555556, "count": 2},
        ],
        key=itemgetter("name"),
    )


def test_map_api_companies(verified_api):
    CartoCompanyFactory(coords=Point(x=55.30, y=-21.22))
    company = CartoCompanyFactory(coords=Point(x=55.50, y=-21.22))
    url = reverse("map_api_objects")
    res = verified_api.get(f"{url}?bounds=55.49,-21.23,55.5745,-21.191")
    assert res.status_code == 200
    data = res.json()
    assert data["clusters"] == []
    assert data["total_count"] == 2
    companies = data["companies"]
    assert len(companies) == 1
    assert companies[0]["siret"] == company.siret
