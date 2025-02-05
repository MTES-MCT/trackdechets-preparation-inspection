import json
import warnings

from allauth.socialaccount.models import SocialAccount
from allauth.socialaccount.tests import OpenIDConnectTests, setup_app
from allauth.tests import TestCase
from django.contrib import auth
from django.test import RequestFactory
from django.urls import reverse

from accounts.factories import UserFactory
from accounts.models import User, UserTypeChoice
from aiot_provider.provider import MonaiotLoginProvider


class AiotOpenIDConnectTests(OpenIDConnectTests, TestCase):
    provider_id = "monaiot"
    default_userinfo_content = {
        "picture": "https://secure.gravatar.com/avatar/123",
        "email": "ness@some.oidc.server.onett.example",
        "sub": 2187,
        "identities": [],
        "name": "Ness",
    }

    def test_login_auto_signup(self):
        """Replaced by test_login_auto_signup_* methods"""
        pass

    def test_login_auto_signup_fails_when_no_droits(self):
        self.userinfo_content = self.default_userinfo_content

        self.get_mocked_response()
        resp = self.login()

        self.assertEqual(resp.status_code, 200)

        self.assertContains(resp, "Échec de connexion", html=True)

        sa_count = SocialAccount.objects.filter(provider=self.app.provider_id).count()
        self.assertEqual(sa_count, 0)
        self.assertEqual(User.objects.count(), 0)

    def test_login_auto_signup_fails_when_wrong_id_profile(self):
        self.userinfo_content = {
            "sub": "f:9f5e9937-1de6-4edc-bc5a-5e69c84b797f:xxxx",
            "name": "Jean VALJEAN",
            "email": "jean.valjean@developpement-durable.gouv.fr",
            "droits": '[{"profil" : "Gestionnaire", "id_profil" : 1, "application" : "GUNenv", "id_application" : 2, "nature_service" : "D(R)EAL, DRIEE ou DGTM", "id_nature_service" : 1, "etablissement" : null, "service_s3ic" : null, "code_entite" : null, "bassin" : null, "region" : "75", "departement" : null, "commune" : null, "station_epuration" : null, "code_sandre" : null, "perimetre_ic" : "ICPE", "droits_etendus" : null}]',
            "given_name": "Jean",
            "family_name": "VALJEAN",
            "email_verified": False,
            "preferred_username": "jean.valjean@developpement-durable.gouv.fr",
        }
        resp = self.login()

        self.assertEqual(resp.status_code, 200)

        self.assertContains(resp, "Échec de connexion", html=True)

        sa_count = SocialAccount.objects.filter(provider=self.app.provider_id).count()
        self.assertEqual(sa_count, 0)
        self.assertEqual(User.objects.count(), 0)

    def test_login_auto_signup_fails_when_wrong_perimeter(self):
        self.userinfo_content = {
            "sub": "f:9f5e9937-1de6-4edc-bc5a-5e69c84b797f:xxxx",
            "name": "Jean VALJEAN",
            "email": "jean.valjean@developpement-durable.gouv.fr",
            "droits": '[{"profil" : "Gestionnaire", "id_profil" : 1, "application" : "GUNenv", "id_application" : 2, "nature_service" : "D(R)EAL, DRIEE ou DGTM", "id_nature_service" : 1, "etablissement" : null, "service_s3ic" : null, "code_entite" : null, "bassin" : null, "region" : "75", "departement" : null, "commune" : null, "station_epuration" : null, "code_sandre" : null, "perimetre_ic" : "PLOP", "droits_etendus" : null}]',
            "given_name": "Jean",
            "family_name": "VALJEAN",
            "email_verified": False,
            "preferred_username": "jean.valjean@developpement-durable.gouv.fr",
        }
        resp = self.login()

        self.assertEqual(resp.status_code, 200)

        self.assertContains(resp, "Échec de connexion", html=True)

        sa_count = SocialAccount.objects.filter(provider=self.app.provider_id).count()
        self.assertEqual(sa_count, 0)
        self.assertEqual(User.objects.count(), 0)

    def test_login_auto_signup_fails_when_gun_reader_and_wrong_id_applicationsr(self):
        # id_profil : 6,
        # id_application : 2 (wrong)
        # id_nature_service : 59
        self.userinfo_content = {
            "sub": "f:9f5e9937-1de6-4edc-bc5a-5e69c84b797f:xxxx",
            "name": "Jean VALJEAN",
            "email": "jean.valjean@developpement-durable.gouv.fr",
            "droits": '[{"profil" : "Gestionnaire", "id_profil" : 6, "application" : "GUNenv", "id_application" : 2, "nature_service" : "D(R)EAL, DRIEE ou DGTM", "id_nature_service" : 1, "etablissement" : null, "service_s3ic" : null, "code_entite" : null, "bassin" : null, "region" : "75", "departement" : null, "commune" : null, "station_epuration" : null, "code_sandre" : null, "perimetre_ic" : "ICPE", "droits_etendus" : null}]',
            "given_name": "Jean",
            "family_name": "VALJEAN",
            "email_verified": False,
            "preferred_username": "jean.valjean@developpement-durable.gouv.fr",
        }
        resp = self.login()

        self.assertEqual(resp.status_code, 200)

        self.assertContains(resp, "Échec de connexion", html=True)

        sa_count = SocialAccount.objects.filter(provider=self.app.provider_id).count()
        self.assertEqual(sa_count, 0)
        self.assertEqual(User.objects.count(), 0)

    def test_login_auto_signup_fails_when_gun_reader_and_wrong_id_nature_service(self):
        # id_profil : 6,
        # id_application : 3
        # id_nature_service : 51 (wrong)
        self.userinfo_content = {
            "sub": "f:9f5e9937-1de6-4edc-bc5a-5e69c84b797f:xxxx",
            "name": "Jean VALJEAN",
            "email": "jean.valjean@developpement-durable.gouv.fr",
            "droits": '[{"profil" : "Gestionnaire", "id_profil" : 6, "application" : "GUNenv", "id_application" : 59, "nature_service" : "D(R)EAL, DRIEE ou DGTM", "id_nature_service" : 1, "etablissement" : null, "service_s3ic" : null, "code_entite" : null, "bassin" : null, "region" : "75", "departement" : null, "commune" : null, "station_epuration" : null, "code_sandre" : null, "perimetre_ic" : "ICPE", "droits_etendus" : null}]',
            "given_name": "Jean",
            "family_name": "VALJEAN",
            "email_verified": False,
            "preferred_username": "jean.valjean@developpement-durable.gouv.fr",
        }
        resp = self.login()

        self.assertEqual(resp.status_code, 200)

        self.assertContains(resp, "Échec de connexion", html=True)

        sa_count = SocialAccount.objects.filter(provider=self.app.provider_id).count()
        self.assertEqual(sa_count, 0)
        self.assertEqual(User.objects.count(), 0)

    def test_login_auto_signup_succeeds(self):
        self.userinfo_content = {
            "sub": "f:9f5e9937-1de6-4edc-bc5a-5e69c84b797f:xxxx",
            "name": "Jean VALJEAN",
            "email": "jean.valjean@developpement-durable.gouv.fr",
            "droits": '[{"profil" : "Gestionnaire", "id_profil" : 4, "application" : "GUNenv", "id_application" : 2, "nature_service" : "D(R)EAL, DRIEE ou DGTM", "id_nature_service" : 1, "etablissement" : null, "service_s3ic" : null, "code_entite" : null, "bassin" : null, "region" : "75", "departement" : null, "commune" : null, "station_epuration" : null, "code_sandre" : null, "perimetre_ic" : "ICPE", "droits_etendus" : null}]',
            "given_name": "Jean",
            "family_name": "VALJEAN",
            "email_verified": False,
            "preferred_username": "jean.valjean@developpement-durable.gouv.fr",
        }
        resp = self.login()

        self.assertRedirects(resp, reverse("post_monaiot_signup"))

        sa = SocialAccount.objects.get(provider=self.app.provider_id)
        user = sa.user
        self.assertEqual(user.email, "jean.valjean@developpement-durable.gouv.fr")
        self.assertEqual(user.user_type, UserTypeChoice.HUMAN)
        self.assertTrue(user.is_active)
        self.assertTrue(user.monaiot_signup)
        self.assertFalse(user.is_staff)
        self.assertFalse(user.is_superuser)

        logged_user = auth.get_user(self.client)

        self.assertTrue(logged_user.is_authenticated)

    def test_login_auto_signup_suceeds_when_gun_reader_and_correct_parameters(self):
        # id_profil : 6,
        # id_application : 3
        # id_nature_service : 59
        self.userinfo_content = {
            "sub": "f:9f5e9937-1de6-4edc-bc5a-5e69c84b797f:xxxx",
            "name": "Jean VALJEAN",
            "email": "jean.valjean@developpement-durable.gouv.fr",
            "droits": '[{"profil" : "Gestionnaire", "id_profil" : 6, "application" : "GUNenv", "id_application" : 3, "nature_service" : "D(R)EAL, DRIEE ou DGTM", "id_nature_service" : 59, "etablissement" : null, "service_s3ic" : null, "code_entite" : null, "bassin" : null, "region" : "75", "departement" : null, "commune" : null, "station_epuration" : null, "code_sandre" : null, "perimetre_ic" : "ICPE", "droits_etendus" : null}]',
            "given_name": "Jean",
            "family_name": "VALJEAN",
            "email_verified": False,
            "preferred_username": "jean.valjean@developpement-durable.gouv.fr",
        }
        resp = self.login()

        self.assertRedirects(resp, reverse("post_monaiot_signup"))

        sa = SocialAccount.objects.get(provider=self.app.provider_id)
        user = sa.user
        self.assertEqual(user.email, "jean.valjean@developpement-durable.gouv.fr")
        self.assertEqual(user.user_type, UserTypeChoice.HUMAN)
        self.assertTrue(user.is_active)
        self.assertTrue(user.monaiot_signup)
        self.assertFalse(user.is_staff)
        self.assertFalse(user.is_superuser)

        logged_user = auth.get_user(self.client)

        self.assertTrue(logged_user.is_authenticated)

    def test_account_refresh_token_saved_next_login(self):
        pass

    def test_login_with_pkce_enabled(self):
        pass

    def test_login_with_pkce_disabled(self):
        pass

    def test_provider_has_pkce_params(self):
        pass

    def setup_provider(self):
        self.app = setup_app(self.provider_id)
        self.app.provider_id = self.provider_id
        self.app.provider = self.provider_id
        self.app.settings = {
            "server_url": "https://unittest.example.com",
        }
        # self.app.save()
        self.request = RequestFactory().get("/")
        self.provider = MonaiotLoginProvider(self.request, app=self.app)

    def test_login(self):
        self.userinfo_content = {
            "sub": "f:9f5e9937-1de6-4edc-bc5a-5e69c84b797f:XYZTA",
            "name": "Diego DELLAVEGA",
            "email": "jean.valjean@developpement-durable.gouv.fr",
            "droits": '[{"profil" : "Gestionnaire", "id_profil" : 4, "application" : "GUNenv", "id_application" : 2, "nature_service" : "D(R)EAL, DRIEE ou DGTM", "id_nature_service" : 1, "etablissement" : null, "service_s3ic" : null, "code_entite" : null, "bassin" : null, "region" : "75", "departement" : null, "commune" : null, "station_epuration" : null, "code_sandre" : null, "perimetre_ic" : "ICPE", "droits_etendus" : null}]',
            "given_name": "Diego",
            "family_name": "DELLAVEGA",
            "email_verified": False,
            "preferred_username": "diego.dellavega@developpement-durable.gouv.fr",
        }
        user = UserFactory(email="diego.dellavega@developpement-durable.gouv.fr")
        SocialAccount.objects.create(provider="monaiot", user=user, uid="f:9f5e9937-1de6-4edc-bc5a-5e69c84b797f:XYZTA")
        resp_mock = self.get_mocked_response()
        if not resp_mock:
            warnings.warn("Cannot test provider %s, no oauth mock" % self.provider.id)
            return
        resp = self.login(
            resp_mock,
        )

        self.assertRedirects(resp, reverse("prepare"))

        user.refresh_from_db()
        self.assertTrue(user.monaiot_connexion)

        account_authentication_methods = self.client.session["account_authentication_methods"]
        self.assertEqual(len(account_authentication_methods), 1)
        account_authentication_method = account_authentication_methods[0]
        self.assertEqual(account_authentication_method["method"], "socialaccount")
        self.assertEqual(account_authentication_method["provider"], "monaiot")
        self.assertEqual(account_authentication_method["uid"], "f:9f5e9937-1de6-4edc-bc5a-5e69c84b797f:XYZTA")

    def test_login_fail(self):
        # wrong id_profil
        self.userinfo_content = {
            "sub": "f:9f5e9937-1de6-4edc-bc5a-5e69c84b797f:XYZTA",
            "name": "Diego DELLAVEGA",
            "email": "jean.valjean@developpement-durable.gouv.fr",
            "droits": '[{"profil" : "Gestionnaire", "id_profil" : 24, "application" : "GUNenv", "id_application" : 2, "nature_service" : "D(R)EAL, DRIEE ou DGTM", "id_nature_service" : 1, "etablissement" : null, "service_s3ic" : null, "code_entite" : null, "bassin" : null, "region" : "75", "departement" : null, "commune" : null, "station_epuration" : null, "code_sandre" : null, "perimetre_ic" : "ICPE", "droits_etendus" : null}]',
            "given_name": "Diego",
            "family_name": "DELLAVEGA",
            "email_verified": False,
            "preferred_username": "diego.dellavega@developpement-durable.gouv.fr",
        }
        user = UserFactory(email="diego.dellavega@developpement-durable.gouv.fr")
        SocialAccount.objects.create(provider="monaiot", user=user, uid="f:9f5e9937-1de6-4edc-bc5a-5e69c84b797f:XYZTA")
        resp_mock = self.get_mocked_response()
        if not resp_mock:
            warnings.warn("Cannot test provider %s, no oauth mock" % self.provider.id)
            return
        resp = self.login(
            resp_mock,
        )

        self.assertEqual(resp.status_code, 200)

        self.assertContains(resp, "Échec de connexion", html=True)

        logged_user = auth.get_user(self.client)

        self.assertFalse(logged_user.is_authenticated)
        user.refresh_from_db()

        self.assertFalse(user.monaiot_connexion)

    def test_account_tokens(self, multiple_login=False):
        self.userinfo_content = {
            "sub": "f:9f5e9937-1de6-4edc-bc5a-5e69c84b797f:XYZTA",
            "name": "Jean VALJEAN",
            "email": "jean.valjean@developpement-durable.gouv.fr",
            "droits": '[{"profil" : "Gestionnaire", "id_profil" : 4, "application" : "GUNenv", "id_application" : 2, "nature_service" : "D(R)EAL, DRIEE ou DGTM", "id_nature_service" : 1, "etablissement" : null, "service_s3ic" : null, "code_entite" : null, "bassin" : null, "region" : "75", "departement" : null, "commune" : null, "station_epuration" : null, "code_sandre" : null, "perimetre_ic" : "ICPE", "droits_etendus" : null}]',
            "given_name": "Jean",
            "family_name": "VALJEAN",
            "email_verified": False,
            "preferred_username": "jean.valjean@developpement-durable.gouv.fr",
        }
        user = UserFactory()

        SocialAccount.objects.create(provider="monaiot", user=user, uid="f:9f5e9937-1de6-4edc-bc5a-5e69c84b797f:XYZTA")

        self.login(self.get_mocked_response())

        # get account
        sa = SocialAccount.objects.filter(user=user, provider=self.provider.app.provider_id or self.provider.id).get()

        # get token
        if self.app:
            t = sa.socialtoken_set.get()
            # verify access_token and refresh_token
            self.assertEqual("testac", t.token)
            resp = json.loads(self.get_login_response_json(with_refresh_token=True))
            if "refresh_token" in resp:
                refresh_token = resp.get("refresh_token")
            elif "refreshToken" in resp:
                refresh_token = resp.get("refreshToken")
            else:
                refresh_token = ""
            self.assertEqual(t.token_secret, refresh_token)
