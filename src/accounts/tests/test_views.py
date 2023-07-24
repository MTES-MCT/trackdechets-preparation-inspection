from unittest import mock

import pytest
from django.conf import settings as dj_settings
from django.urls import reverse
from sesame.settings import load as load_sesame_settings
from sesame.utils import get_query_string
from simplemathcaptcha.utils import hash_answer

from ..factories import UserFactory

pytestmark = pytest.mark.django_db

login_url = reverse("login")


def test_base_view_redirects_to_login(anon_client):
    res = anon_client.get(reverse("home"))
    assert res.status_code == 302
    assert res.url == reverse("login")


def test_login_view_get(anon_client):
    res = anon_client.get(login_url)
    assert res.status_code == 200


def ops_gen():
    while True:
        yield "-"


def int_gen():
    count = 1
    while True:
        count += 1
        if count % 2:
            yield 3
        else:
            yield 10


@mock.patch("simplemathcaptcha.widgets.get_operator")
@mock.patch("simplemathcaptcha.utils.randint")
def test_login_view_fails_with_wrong_captcha(
    mock_randint, mock_get_operator, anon_client, mailoutbox
):
    user = UserFactory()
    ops = ops_gen()
    ints = int_gen()
    correct_captcha = 7
    hashed_answer = hash_answer(correct_captcha)
    mock_get_operator.side_effect = lambda: next(ops)
    mock_randint.side_effect = lambda x, y: next(ints)

    assert len(mailoutbox) == 0
    res = anon_client.get(login_url)

    assert res.context["question_html"] == "Combien font 10 - 3?"
    assert hashed_answer in res.content.decode()
    # wrong captcha
    res = anon_client.post(
        login_url,
        {
            "email": user.email,
            "captcha_0": correct_captcha + 1,
            "captcha_1": hashed_answer,
        },
        follow=True,
    )
    assert res.status_code == 200
    assert res.context["form"].errors == {"captcha": ["Merci de réviser vos maths."]}
    assert len(mailoutbox) == 0


@mock.patch("simplemathcaptcha.widgets.get_operator")
@mock.patch("simplemathcaptcha.utils.randint")
def test_login_view_fails_with_wrong_email(
    mock_randint, mock_get_operator, anon_client, mailoutbox
):
    UserFactory()
    ops = ops_gen()
    ints = int_gen()
    correct_captcha = 7
    hashed_answer = hash_answer(correct_captcha)
    mock_get_operator.side_effect = lambda: next(ops)
    mock_randint.side_effect = lambda x, y: next(ints)

    assert len(mailoutbox) == 0
    res = anon_client.get(login_url)

    assert res.context["question_html"] == "Combien font 10 - 3?"
    assert hashed_answer in res.content.decode()
    # inexistant email
    res = anon_client.post(
        login_url,
        {
            "email": "doesnotexist@lorem.com",
            "captcha_0": correct_captcha,
            "captcha_1": hashed_answer,
        },
        follow=True,
    )
    assert res.status_code == 200
    assert (
        "un email contenant un lien de connexion vous a été envoyé."
        in res.content.decode()
    )

    assert len(mailoutbox) == 0


@mock.patch("simplemathcaptcha.widgets.get_operator")
@mock.patch("simplemathcaptcha.utils.randint")
def test_login_view_fails_with_inactive_user(
    mock_randint, mock_get_operator, anon_client, mailoutbox
):
    user = UserFactory(is_active=False)
    ops = ops_gen()
    ints = int_gen()

    correct_captcha = 7
    hashed_answer = hash_answer(correct_captcha)
    mock_get_operator.side_effect = lambda: next(ops)
    mock_randint.side_effect = lambda x, y: next(ints)

    assert len(mailoutbox) == 0
    res = anon_client.get(login_url)

    assert res.context["question_html"] == "Combien font 10 - 3?"
    assert hashed_answer in res.content.decode()

    # inexistant email
    res = anon_client.post(
        login_url,
        {"email": user.email, "captcha_0": correct_captcha, "captcha_1": hashed_answer},
        follow=True,
    )
    assert res.status_code == 200
    assert (
        "un email contenant un lien de connexion vous a été envoyé."
        in res.content.decode()
    )

    assert len(mailoutbox) == 0


@mock.patch("simplemathcaptcha.widgets.get_operator")
@mock.patch("simplemathcaptcha.utils.randint")
def test_login_view_sends_magic_link_email(
    mock_randint, mock_get_operator, anon_client, mailoutbox
):
    user = UserFactory()
    ops = ops_gen()
    ints = int_gen()
    hashed_answer = hash_answer(7)
    mock_get_operator.side_effect = lambda: next(ops)
    mock_randint.side_effect = lambda x, y: next(ints)

    assert len(mailoutbox) == 0
    res = anon_client.get(login_url)

    assert res.context["question_html"] == "Combien font 10 - 3?"
    assert hashed_answer in res.content.decode()

    res = anon_client.post(
        login_url,
        {"email": user.email, "captcha_0": 7, "captcha_1": hashed_answer},
        follow=True,
    )
    assert res.status_code == 200

    assert (
        "un email contenant un lien de connexion vous a été envoyé."
        in res.content.decode()
    )
    assert len(mailoutbox) == 1
    message = mailoutbox[0]

    assert message.to == [user.email]
    assert "Pour vous connecter à la fiche d'inspection:" in message.body


def test_magic_link_success(anon_client):
    user = UserFactory()
    magic_link = f"{reverse('magic_login')}{get_query_string(user)}"
    res = anon_client.get(magic_link, follow=True)

    assert res.status_code == 200
    assert reverse("home") in res.redirect_chain[-1][0]
    assert res.redirect_chain[-1][1] == 302
    assert "_auth_user_id" in anon_client.session.keys()


def test_magic_link_fails_on_incorrect_qs(anon_client):
    user = UserFactory()
    # truncate query string
    magic_link = f"{reverse('magic_login')}{get_query_string(user)[:-2]}"
    res = anon_client.get(magic_link)

    assert res.status_code == 403

    assert "_auth_user_id" not in anon_client.session.keys()


def test_magic_link_fails_on_missing_qs(anon_client):
    UserFactory()
    # truncate query string
    magic_link = f"{reverse('magic_login')}"
    res = anon_client.get(magic_link)

    assert res.status_code == 403

    assert "_auth_user_id" not in anon_client.session.keys()


def test_magic_link_fails_on_old_magic_links(anon_client, settings):
    user = UserFactory()

    settings.SESAME_MAX_AGE = -100
    load_sesame_settings()

    # truncate query string
    magic_link = f"{reverse('magic_login')}{get_query_string(user)}"

    res = anon_client.get(magic_link)
    assert "_auth_user_id" not in anon_client.session.keys()

    assert res.status_code == 403


def test_logout_view(logged_in_user):
    logout_url = reverse("logout")
    res = logged_in_user.get(logout_url, follow=True)
    assert res.status_code == 200
    assert reverse("login") in res.redirect_chain[-1][0]
    assert res.redirect_chain[-1][1] == 302
    assert "_auth_user_id" not in logged_in_user.session.keys()


def test_admin_url_redirects_to_home(anon_client):
    res = anon_client.get(f"/{dj_settings.ADMIN_SLUG}/login/", follow=True)
    assert res.status_code == 200
    assert reverse("home") in res.redirect_chain[-1][0]
    assert res.redirect_chain[-1][1] == 302
