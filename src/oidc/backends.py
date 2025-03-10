import json
import logging

import requests
from django.conf import settings
from django.core.exceptions import PermissionDenied
from mozilla_django_oidc.auth import OIDCAuthenticationBackend
from mozilla_django_oidc.utils import import_from_settings

from accounts.constants import MONAIOT, PROCONNECT

from .constants import (
    ALLOWED_PERIMETER,
    ALLOWED_PROFILES,
    GUN_READER_ALLOWED_APPLICATION_ID,
    GUN_READER_ALLOWED_SERVICE_ID,
    GUN_READER_ID,
)
from .models import OidcLogin

logger = logging.getLogger(__name__)


class BaseOidcBackend(OIDCAuthenticationBackend):
    """Base class for OIDC authentication backends with common functionality."""

    provider_name = None  # To be defined by subclasses

    @classmethod
    def get_settings(cls, attr, *args):
        """Retrieve settings with the appropriate prefix."""
        if not cls.provider_name:
            raise NotImplementedError("provider_name must be defined in subclass")

        prefixed_attr = f"{cls.provider_name}_{attr}"
        return import_from_settings(prefixed_attr, *args)

    def update_user_login_info(self, user, claims, account_created=False):
        """Record login information and update user attributes."""
        if user.oidc_connexion != self.provider_name:
            user.oidc_connexion = self.provider_name
            user.save()

        OidcLogin.objects.create(user=user, info=claims, provider=self.provider_name, account_created=account_created)
        return user

    def authenticate(self, request, **kwargs):
        """Only process authentication for the appropriate provider."""

        if request and getattr(request, "oidc_provider", None) != self.get_provider_name():
            return None

        return super().authenticate(request, **kwargs)

    def get_provider_name(self):
        """Return the lowercase provider name for request matching."""
        if not self.provider_name:
            raise NotImplementedError("PROVIDER_PREFIX must be defined in subclass")

        return self.provider_name  # .lower()

    def update_user(self, user, claims):
        """Update existing user with new claims data."""
        user = super().update_user(user, claims)
        return self.update_user_login_info(user, claims)


class MonAiotOidcBackend(BaseOidcBackend):
    """Authentication backend for MonAiot OIDC provider."""

    provider_name = MONAIOT

    def create_user(self, claims):
        """Create a new user account based on OIDC claims."""
        email = claims.get("email")
        if not email:
            logger.error("No email found in claims, cannot create user")
            raise PermissionDenied("No email provided in authentication data")

        user = self.UserModel.objects.create_user(
            username=email,
            email=email,
            password="",  # Empty password as auth is handled by OIDC
            oidc_signup=self.provider_name,
        )

        return self.update_user_login_info(user, claims, account_created=True)

    def verify_claims(self, claims):
        """Verify user has appropriate access rights based on claims."""
        verified = super().verify_claims(claims)
        droits_data = claims.get("droits")

        if not droits_data:
            logger.warning("No 'droits' data found in claims")
            raise PermissionDenied("Missing required authorization data")

        try:
            droits = json.loads(droits_data)
        except json.JSONDecodeError:
            logger.error("Failed to parse 'droits' JSON data")
            raise PermissionDenied("Invalid authorization data format")

        access_granted = False
        matching_profile = None

        for droit in droits:
            id_profil = droit.get("id_profil")
            perimetre_ic = droit.get("perimetre_ic")

            if id_profil in ALLOWED_PROFILES and perimetre_ic == ALLOWED_PERIMETER:
                access_granted = True
                matching_profile = id_profil

                # Gun readers require extra verification
                if matching_profile == GUN_READER_ID:
                    id_application = droit.get("id_application")
                    id_nature_service = droit.get("id_nature_service")

                    if (
                        id_application != GUN_READER_ALLOWED_APPLICATION_ID
                        or id_nature_service != GUN_READER_ALLOWED_SERVICE_ID
                    ):
                        access_granted = False

        if not access_granted:
            logger.warning(f"Access denied for user with claims: {claims}")
            raise PermissionDenied("Insufficient permissions for access")

        return verified


class ProconnectOidcBackend(BaseOidcBackend):
    """Authentication backend for Proconnect OIDC provider."""

    provider_name = PROCONNECT

    def get_userinfo(self, access_token, id_token, payload):
        """Retrieve and verify user information from the OIDC provider."""
        user_response = requests.get(
            self.OIDC_OP_USER_ENDPOINT,
            headers={"Authorization": f"Bearer {access_token}"},
            verify=self.get_settings("OIDC_VERIFY_SSL", True),
            timeout=self.get_settings("OIDC_TIMEOUT", None),
            proxies=self.get_settings("OIDC_PROXY", None),
        )
        user_response.raise_for_status()

        # Handle JWT response for Proconnect
        content_type = user_response.headers.get("Content-Type", "")
        if "application/jwt" in content_type:
            return self.verify_token(user_response.text)
        return user_response.json()

    def create_user(self, claims):
        """Proconnect doesn't create new users."""
        logger.info("User creation not supported for Proconnect authentication")
        return None

    def verify_claims(self, claims):
        """Verify user has appropriate access rights based on claims."""
        idp_id = claims.get("idp_id")

        if not idp_id:
            logger.warning("No 'idp_id' found in claims")
            raise PermissionDenied("Missing identity provider information")

        # Ensure identity provider matches allowed list
        if idp_id not in settings.PROCONNECT_ALLOWED_IDP_IDS:
            logger.warning(f"Unauthorized identity provider: {idp_id}")
            raise PermissionDenied("Unauthorized identity provider")

        return True

    def filter_users_by_claims(self, claims):
        """Filter users eligible for Proconnect authentication."""
        users = super().filter_users_by_claims(claims)

        return users.allowed_for_proconnect()
