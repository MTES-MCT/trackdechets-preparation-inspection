import json

from django.core.exceptions import PermissionDenied
from mozilla_django_oidc.auth import OIDCAuthenticationBackend

from .models import OidcLogin, ProviderChoice

MANAGER_ID = 4
ADMIN_ID = 2
GUN_ID = 3
GUN_READER_ID = 6  # administration centrale
GUN_READER_ALLOWED_APPLICATION_ID = 3
GUN_READER_ALLOWED_SERVICE_ID = 59

ALLOWED_PROFILES = {MANAGER_ID, ADMIN_ID, GUN_ID, GUN_READER_ID}
ALLOWED_PERIMETER = "ICPE"


class MonAiotOidcBackend(OIDCAuthenticationBackend):
    def create_user(self, claims):
        """Return object for a newly created user account."""
        email = claims.get("email")

        user = self.UserModel.objects.create_user(username=email, email=email, password="", monaiot_signup=True)

        OidcLogin.objects.create(user=user, provider=ProviderChoice.MONAIOT, info=claims, account_created=True)
        return user

    def update_user(self, user, claims):
        user = super().update_user(user, claims)
        if not user.monaiot_connexion:
            user.monaiot_connexion = True
            user.save()

        OidcLogin.objects.create(user=user, info=claims, provider=ProviderChoice.MONAIOT)
        return user

    def verify_claims(self, claims):
        access_granted = False
        verified = super().verify_claims(claims)
        droits_data = claims.get("droits", None)

        if not droits_data:
            raise PermissionDenied

        droits = json.loads(droits_data)
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
        return verified
