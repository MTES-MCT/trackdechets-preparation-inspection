import pytest

from ..factories import ApiUserFactory, EmailDeviceFactory, UserFactory
from ..models import User

pytestmark = pytest.mark.django_db


def test_user_factory():
    user = UserFactory()
    assert user.pk
    assert user.username
    assert user.email
    assert user.is_active
    assert user.password
    assert not user.is_staff
    assert not user.is_superuser
    assert not user.is_api


def test_create_super_user():
    superuser = User.objects.create_superuser(
        email="superuser@trackdechets.test",
        username="Le boss",
        password="tressupersecret",
    )
    assert superuser.is_active
    assert superuser.password
    assert superuser.is_staff
    assert superuser.is_superuser
    assert superuser.check_password("tressupersecret")


def test_email_device_factories():
    device = EmailDeviceFactory()
    assert device.pk
    assert device.user.pk


def test_api_user_factory():
    user = ApiUserFactory()
    assert user.pk
    assert user.username
    assert user.email
    assert user.is_active
    assert user.password
    assert not user.is_staff
    assert not user.is_superuser
    assert user.is_api
