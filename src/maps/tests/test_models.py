import pytest

from ..factories import CartoCompanyFactory

pytestmark = pytest.mark.django_db


def test_carto_company_factory():
    company = CartoCompanyFactory()
    assert company.pk
    assert company.siret
    assert company.nom_etablissement
    assert company.coords.x
    assert company.coords.y
