from allauth.socialaccount import providers
from allauth.socialaccount.providers.openid_connect.provider import OpenIDConnectProvider
from django.conf import settings

from .adapter import MonAiotDConnectAdapter


class MonaiotLoginProvider(OpenIDConnectProvider):
    id = "monaiot"
    slug = "monaiot"
    oauth2_adapter_class = MonAiotDConnectAdapter
    name = "monaiot Login (OpenID Connect)"
    scopes = settings.MONAIOT_SCOPES


# https://django-allauth.readthedocs.io/en/latest/advanced.html#customizing-providers
provider_classes = [MonaiotLoginProvider]
providers.registry.register(MonaiotLoginProvider)
