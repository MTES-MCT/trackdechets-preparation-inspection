import pytest
from django.urls import reverse

from accounts.models import UserCategoryChoice

pytestmark = pytest.mark.django_db


def test_home(verified_user):
    url = reverse("private_home")
    res = verified_user.get(url)
    assert res.status_code == 200

    assert "Admin équipe" not in res.content.decode()


def test_home_administration_centrale_menu(verified_adm_centrale):
    url = reverse("private_home")
    res = verified_adm_centrale.get(url)
    assert res.status_code == 200

    assert "Préparer une fiche" in res.content.decode()
    assert "Registre" in res.content.decode()
    assert "Bordereau" in res.content.decode()
    assert "Cartographie" not in res.content.decode()
    assert "Admin équipe" not in res.content.decode()
    assert "Observatoires" in res.content.decode()


def test_home_observatoire_menu(verified_observatoire):
    url = reverse("private_home")
    res = verified_observatoire.get(url)
    assert res.status_code == 200

    assert "Préparer une fiche" not in res.content.decode()
    assert "Registre" not in res.content.decode()
    assert "Bordereau" not in res.content.decode()
    assert "Cartographie" not in res.content.decode()
    assert "Admin équipe" not in res.content.decode()
    assert "Observatoires" in res.content.decode()


@pytest.mark.parametrize(
    "get_profile",
    [
        "verified_icpe",
        "verified_ctt",
        "verified_inspection_travail",
        "verified_gendarme",
        "verified_ars",
        "verified_douane",
    ],
    indirect=True,
)
def test_home_menu(get_profile):
    url = reverse("private_home")
    res = get_profile.get(url)
    assert res.status_code == 200

    assert "Préparer une fiche" in res.content.decode()
    assert "Registre" in res.content.decode()
    assert "Bordereau" in res.content.decode()
    assert "Cartographie" not in res.content.decode()
    assert "Admin équipe" not in res.content.decode()
    assert "Observatoires" not in res.content.decode()


@pytest.mark.parametrize("get_client", ["verified_client", "logged_monaiot_client"], indirect=True)
def test_private_home_menu(get_client):
    url = reverse("private_home")
    res = get_client.get(url)
    assert res.status_code == 200

    assert "Établissements" in res.content.decode()
    assert "Préparer une fiche" in res.content.decode()
    assert "Registre" in res.content.decode()
    assert "Contrôle routier" in res.content.decode()
    assert "Bordereau" in res.content.decode()

    assert "Admin équipe" not in res.content.decode()
    assert "Observatoires" not in res.content.decode()
    assert "Cartographie" not in res.content.decode()

    assert "Guide" in res.content.decode()


@pytest.mark.parametrize("get_client", ["verified_client", "logged_monaiot_client"], indirect=True)
def test_private_home_menu_for_observatoire(get_client):
    user = get_client.user
    user.user_category = UserCategoryChoice.OBSERVATOIRE
    user.save()

    user.refresh_from_db()

    assert user.is_observatoire

    url = reverse("private_home")
    res = get_client.get(url)
    assert res.status_code == 200
    assert "Préparer une fiche" not in res.content.decode()

    assert "Bordereau" not in res.content.decode()

    assert "Admin équipe" not in res.content.decode()
    assert "Observatoires" in res.content.decode()
    assert "Contrôle routier" not in res.content.decode()
    assert "Cartographie" not in res.content.decode()
    assert "Bordereau" not in res.content.decode()
    assert "Guide" in res.content.decode()


def test_home_for_staff(verified_staff):
    url = reverse("private_home")
    res = verified_staff.get(url)
    assert res.status_code == 200

    assert "Admin équipe" in res.content.decode()
    assert "Observatoire" in res.content.decode()
