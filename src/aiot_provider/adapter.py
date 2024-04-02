import json

from allauth.socialaccount.adapter import get_adapter
from allauth.socialaccount.providers.openid_connect.views import OpenIDConnectAdapter
from allauth.utils import build_absolute_uri
from django.core.exceptions import PermissionDenied
from django.urls import reverse

MANAGER_ID = 4
ADMIN_ID = 2
GUN_ID = 3
ALLOWED_PROFILES = {MANAGER_ID, ADMIN_ID, GUN_ID}


class MonAiotDConnectAdapter(OpenIDConnectAdapter):
    def complete_login(self, request, app, token, response):
        """Ensure userinfo carries relevant permissions to log user in"""
        response = (
            get_adapter()
            .get_requests_session()
            .get(self.profile_url, headers={"Authorization": "Bearer " + str(token)})
        )
        response.raise_for_status()
        extra_data = response.json()
        droits_data = extra_data.get("droits", None)
        if not droits_data:
            raise PermissionDenied

        droits = json.loads(droits_data)
        profiles = [el.get("id_profil") for el in droits]

        if not ALLOWED_PROFILES.intersection(set(profiles)):
            raise PermissionDenied

        return self.get_provider().sociallogin_from_response(request, extra_data)

    def get_callback_url(self, request, app):
        callback_url = reverse("monaiot_callback", kwargs={"provider_id": self.provider_id})
        protocol = self.redirect_uri_protocol
        return build_absolute_uri(request, callback_url, protocol)
