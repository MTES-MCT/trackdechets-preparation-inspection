import json

from allauth.socialaccount.adapter import get_adapter
from allauth.socialaccount.providers.openid_connect.views import OpenIDConnectAdapter
from allauth.utils import build_absolute_uri
from django.core.exceptions import PermissionDenied
from django.urls import reverse

MANAGER_ID = 4
ADMIN_ID = 2
GUN_ID = 3
GUN_READER_ID = 6  # administration centrale
GUN_READER_ALLOWED_APPLICATION_ID = 3
GUN_READER_ALLOWED_SERVICE_ID = 59

ALLOWED_PROFILES = {MANAGER_ID, ADMIN_ID, GUN_ID, GUN_READER_ID}
ALLOWED_PERIMETER = "ICPE"


class MonAiotDConnectAdapter(OpenIDConnectAdapter):
    def complete_login(self, request, app, token, response):
        """Ensure userinfo carries relevant permissions to log user in or create their account"""

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

        access_granted = False
        for droit in droits:
            id_profil = droit.get("id_profil")
            perimetre_ic = droit.get("perimetre_ic")
            id_application = droit.get("id_application")
            id_nature_service = droit.get("id_nature_service")
            if id_profil in ALLOWED_PROFILES and perimetre_ic == ALLOWED_PERIMETER:
                access_granted = True
                matching_profile = id_profil
            else:
                continue

            # Gun readers require extra verification
            if matching_profile == GUN_READER_ID:
                if id_application != GUN_READER_ALLOWED_APPLICATION_ID:
                    access_granted = False
                if id_nature_service != GUN_READER_ALLOWED_SERVICE_ID:
                    access_granted = False

        if not access_granted:
            raise PermissionDenied

        # Gun readers require extra verification

        return self.get_provider().sociallogin_from_response(request, extra_data)

    def get_callback_url(self, request, app):
        callback_url = reverse("monaiot_callback", kwargs={"provider_id": self.provider_id})
        protocol = self.redirect_uri_protocol
        return build_absolute_uri(request, callback_url, protocol)
