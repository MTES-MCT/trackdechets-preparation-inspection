from allauth.socialaccount import providers
from allauth.socialaccount.providers.openid_connect.provider import OpenIDConnectProvider


class MonaiotLoginProvider(OpenIDConnectProvider):
    id = "monaiot"
    slug = "monaiot"
    name = "monaiot Login (OpenID Connect)"
    scopes = ("openid", "email", "phone", "profile")


# https://django-allauth.readthedocs.io/en/latest/advanced.html#customizing-providers
provider_classes = [MonaiotLoginProvider]
providers.registry.register(MonaiotLoginProvider)
