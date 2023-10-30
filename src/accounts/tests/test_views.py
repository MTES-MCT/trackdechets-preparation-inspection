import pytest
from django.core import mail
from django.urls import reverse
from django.utils import timezone
from django_otp.plugins.otp_email.models import EmailDevice

from ..factories import DEFAULT_PASSWORD, EmailDeviceFactory, UserFactory

pytestmark = pytest.mark.django_db

login_url = reverse("login")
second_factor_url = reverse("second_factor")


def test_private_home_view_redirects_anon_user_to_login(anon_client):
    private_home = reverse("private_home")
    res = anon_client.get(private_home)
    assert res.status_code == 302
    assert res.url == f"{reverse('login')}?next={private_home}"


def test_private_home_view_redirects_logged_in_user_to_second_factor(logged_in_user):
    private_home = reverse("private_home")
    res = logged_in_user.get(private_home)
    assert res.status_code == 302
    assert res.url == f"{reverse('second_factor')}"


def test_private_home_view(verified_user):
    private_home = reverse("private_home")
    res = verified_user.get(private_home)
    assert res.status_code == 200


def test_login_view_get(anon_client):
    res = anon_client.get(login_url)
    assert res.status_code == 200


def test_login_view_denies_bad_password(anon_client):
    user = UserFactory()

    anon_client.post(login_url, {"email": user.email, "password": "JUNK"})
    assert "_auth_user_id" not in anon_client.session.keys()

    assert len(mail.outbox) == 0


def test_login_view_denies_inactive_user(anon_client):
    user = UserFactory(is_active=False)

    anon_client.post(login_url, {"email": user.email, "password": DEFAULT_PASSWORD})
    assert "_auth_user_id" not in anon_client.session.keys()
    assert len(mail.outbox) == 0


def test_login_view_accepts_good_password_and_sends_email(anon_client):
    user = UserFactory()

    # Good password
    res = anon_client.post(login_url, {"email": user.email, "password": DEFAULT_PASSWORD})
    assert res.status_code == 302
    assert res.url == second_factor_url

    assert "_auth_user_id" in anon_client.session.keys()

    assert len(mail.outbox) == 1
    email_sent = mail.outbox[0]
    assert user.email in email_sent.to

    # a device is created and the token is sent by email
    devices = EmailDevice.objects.devices_for_user(user)
    assert len(devices) == 1
    device = devices[0]
    token = device.token
    assert len(token) == 6
    assert token in email_sent.body


def test_login_view_redirects_logged_in_user(logged_in_user):
    res = logged_in_user.get(login_url, follow=True)
    assert res.status_code == 200
    assert reverse("second_factor") == res.redirect_chain[-1][0]
    assert res.redirect_chain[-1][1] == 302


def test_logout_view(verified_user):
    logout_url = reverse("logout")
    res = verified_user.get(logout_url, follow=True)
    assert res.status_code == 200
    assert reverse("login") in res.redirect_chain[-1][0]
    assert res.redirect_chain[-1][1] == 302
    assert "_auth_user_id" not in verified_user.session.keys()
    assert "otp_device_id" not in verified_user.session.keys()


def test_second_factor_view_deny_anon_user(anon_client):
    res = anon_client.get(second_factor_url, follow=True)
    assert res.status_code == 200
    assert reverse("login") in res.redirect_chain[-1][0]
    assert res.redirect_chain[-1][1] == 302


def test_second_factor_view_get(logged_in_user):
    res = logged_in_user.get(second_factor_url)
    assert res.status_code == 200


def test_second_factor_view_denies_wrong_token(logged_in_user):
    res = logged_in_user.get(second_factor_url)
    assert res.status_code == 200

    device = EmailDeviceFactory(user=logged_in_user.user)

    device.generate_challenge()

    res = logged_in_user.post(second_factor_url, {"otp_token": "56789"})

    assert res.status_code == 200
    assert res.context["form"].errors == {
        "__all__": ["Jeton non valable ou trop ancien. Assurez-vous de bien l’avoir saisi correctement."]
    }

    # user still logged in
    assert "_auth_user_id" in logged_in_user.session.keys()
    # but not verified
    assert "otp_device_id" not in logged_in_user.session.keys()


def test_second_factor_view_denies_expired_token(logged_in_user):
    res = logged_in_user.get(second_factor_url)
    assert res.status_code == 200

    device = EmailDeviceFactory(user=logged_in_user.user)

    device.generate_challenge()
    # edit token expiration
    device.valid_until = timezone.now()
    device.save()

    res = logged_in_user.post(second_factor_url, {"otp_token": device.token})

    assert res.status_code == 200
    assert res.context["form"].errors == {
        "__all__": ["Jeton non valable ou trop ancien. Assurez-vous de bien l’avoir saisi correctement."]
    }

    # user still logged in
    assert "_auth_user_id" in logged_in_user.session.keys()
    # but not verified
    assert "otp_device_id" not in logged_in_user.session.keys()


def test_second_factor_view_accepts_good_token(logged_in_user):
    res = logged_in_user.get(second_factor_url)
    assert res.status_code == 200

    device = EmailDeviceFactory(user=logged_in_user.user)

    device.generate_challenge()

    res = logged_in_user.post(second_factor_url, {"otp_token": device.token})

    assert res.status_code == 302
    assert res.url == reverse("private_home")

    assert logged_in_user.session["otp_device_id"] == device.persistent_id


def test_resend_token_email(logged_in_user):
    user = logged_in_user.user
    res = logged_in_user.post(reverse("resend_token"), {})
    assert res.status_code == 302
    assert res.url == second_factor_url

    assert len(mail.outbox) == 1
    email_sent = mail.outbox[0]
    assert user.email in email_sent.to

    # a device is created and the token is sent by email
    devices = EmailDevice.objects.devices_for_user(user)
    assert len(devices) == 1
    device = devices[0]
    token = device.token
    assert len(token) == 6
    assert token in email_sent.body


def test_resend_token_email_is_throttled(logged_in_user):
    user = logged_in_user.user
    # first time
    res = logged_in_user.post(reverse("resend_token"), {})
    assert res.url == second_factor_url

    # second time
    res = logged_in_user.post(reverse("resend_token"), {})
    assert res.url == second_factor_url
    # third time
    res = logged_in_user.post(reverse("resend_token"), {})
    assert res.url == second_factor_url

    # only 1 mail is sent
    assert len(mail.outbox) == 1
    email_sent = mail.outbox[0]
    assert user.email in email_sent.to


def test_django_admin_denies_logged_in_user(logged_in_user):
    res = logged_in_user.get(reverse("admin:index"))
    assert res.status_code == 302


def test_django_admin_denies_verified_user(verified_user):
    res = verified_user.get(reverse("admin:index"))
    assert res.status_code == 302


def test_django_admin_denies_logged_staff_user(logged_in_staff):
    res = logged_in_staff.get(reverse("admin:index"))
    assert res.status_code == 302


def test_django_admin_grants_verifed_staff_user(verified_staff):
    res = verified_staff.get(reverse("admin:index"))
    assert res.status_code == 200
