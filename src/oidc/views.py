from django.shortcuts import resolve_url
from django.views.generic import TemplateView
from mozilla_django_oidc.views import OIDCAuthenticationCallbackView

from common.mixins import FullyLoggedMixin


class PostMonAiotSignup(FullyLoggedMixin, TemplateView):
    template_name = "post_monaiot_signup.html"
    allowed_user_categories = ["*"]


class MonaiotOIDCAuthenticationCallbackView(OIDCAuthenticationCallbackView):
    @property
    def success_url(self):
        # Pull the next url from the session or settings--we don't need to
        # sanitize here because it should already have been sanitized.
        next_url = self.request.session.get("oidc_login_next", None)
        return next_url or resolve_url(self.get_settings("OIDC_LOGIN_REDIRECT_URL", "/"))

    @property
    def failure_url(self):
        return self.get_settings("OIDC_LOGIN_REDIRECT_URL_FAILURE", "/")


class MonAiotAuthenttError(TemplateView):
    template_name = "oidc/authentication_error.html"
