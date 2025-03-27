from django import template
from django.urls import reverse

from config.settings.base import PROCONNECT_BACKEND

register = template.Library()


@register.simple_tag(takes_context=True)
def logout_url(context):
    """
    Return the appropriate logout URL based on the authentication backend used.

    If the user is authenticated via ProConnect, returns the ProConnect logout URL.
    Otherwise, returns the standard Django logout URL.
    """
    request = context.get("request")

    if not request:
        return reverse("logout")

    auth_backend = request.session.get("_auth_user_backend")

    if auth_backend == PROCONNECT_BACKEND:
        return reverse("proconnect_oidc_logout")

    return reverse("logout")
