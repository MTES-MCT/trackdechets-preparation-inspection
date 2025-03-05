from django.shortcuts import resolve_url
from django.views.generic import TemplateView
from mozilla_django_oidc.utils import import_from_settings
from mozilla_django_oidc.views import OIDCAuthenticationCallbackView, OIDCAuthenticationRequestView

from accounts.constants import MONAIOT, PROCONNECT
from common.mixins import FullyLoggedMixin


class PostMonAiotSignup(FullyLoggedMixin, TemplateView):
    template_name = "post_monaiot_signup.html"
    allowed_user_categories = ["*"]


class MonAiotAuthentError(TemplateView):
    template_name = "oidc/monaiot_authentication_error.html"


class ProconnectAuthentError(TemplateView):
    template_name = "oidc/proconnect_authentication_error.html"


class BaseOIDCAuthenticationRequestView(OIDCAuthenticationRequestView):
    """Base class for OIDC authentication request views with provider-specific settings."""

    provider_name = None

    @classmethod
    def get_settings(cls, attr, *args):
        """Retrieve provider-specific settings using the provider prefix."""
        if not cls.provider_name:
            raise ValueError("provider_name must be defined in subclass")
        prefix = cls.provider_name.upper()
        prefixed_attr = f"{prefix}_{attr}"
        return import_from_settings(prefixed_attr, *args)


class BaseOIDCAuthenticationCallbackView(OIDCAuthenticationCallbackView):
    """Base class for OIDC authentication callback views with provider-specific settings."""

    provider_name = None

    def dispatch(self, request, *args, **kwargs):
        """Set the OIDC provider on the request and dispatch."""

        if not self.provider_name:
            raise ValueError("provider_name must be defined in subclass")
        request.oidc_provider = self.provider_name

        return super().dispatch(request, *args, **kwargs)

    @classmethod
    def get_settings(cls, attr, *args):
        """Retrieve provider-specific settings using the provider prefix."""
        if not cls.provider_name:
            raise ValueError("provider_name must be defined in subclass")
        prefix = cls.provider_name
        prefixed_attr = f"{prefix}_{attr}"
        return import_from_settings(prefixed_attr, *args)

    @property
    def success_url(self):
        """Get the URL to redirect to after successful authentication."""
        next_url = self.request.session.get("oidc_login_next", None)
        return next_url or resolve_url(self.get_settings("OIDC_LOGIN_REDIRECT_URL", "/"))

    @property
    def failure_url(self):
        """Get the URL to redirect to after failed authentication."""
        return self.get_settings("OIDC_LOGIN_REDIRECT_URL_FAILURE", "/")


# MonAiot OIDC Views
class MonaiotOIDCAuthenticationRequestView(BaseOIDCAuthenticationRequestView):
    """MonAiot-specific OIDC authentication request view."""

    provider_name = MONAIOT


class MonaiotOIDCAuthenticationCallbackView(BaseOIDCAuthenticationCallbackView):
    """MonAiot-specific OIDC authentication callback view."""

    provider_name = MONAIOT


# ProConnect OIDC Views
class ProconnectOIDCAuthenticationRequestView(BaseOIDCAuthenticationRequestView):
    """ProConnect-specific OIDC authentication request view."""

    provider_name = PROCONNECT


class ProconnectOIDCAuthenticationCallbackView(BaseOIDCAuthenticationCallbackView):
    """ProConnect-specific OIDC authentication callback view."""

    provider_name = PROCONNECT


class MonAiotAuthenticationError(TemplateView):
    """View for displaying MonAiot authentication errors."""

    template_name = "oidc/monaiot_authentication_error.html"
