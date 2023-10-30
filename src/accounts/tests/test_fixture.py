import pytest
from django.urls import reverse

pytestmark = pytest.mark.django_db

login_url = reverse("login")
second_factor_url = reverse("second_factor")


def test_logged_in_user(logged_in_user):
    assert "_auth_user_id" in logged_in_user.session.keys()
    assert "otp_device_id" not in logged_in_user.session.keys()


def test_verified_user(verified_user):
    assert "_auth_user_id" in verified_user.session.keys()
    assert "otp_device_id" in verified_user.session.keys()
