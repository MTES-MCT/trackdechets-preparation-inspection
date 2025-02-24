from .base import *  # noqa

DATABASES = {
    "default": {
        "ENGINE": "django.contrib.gis.db.backends.postgis",
        "NAME": "plop",
        "USER": "postgres",
        "PASSWORD": "admin",
        "HOST": "localhost",
        "PORT": 5432,
    }
}

PASSWORD_HASHERS = ["django.contrib.auth.hashers.MD5PasswordHasher"]  # faster hashes

SECRET_KEY = "xyz12345"

CELERY_ALWAYS_EAGER = True

MESSAGE_RECIPIENTS = ["lorem@ipsum.lol"]

OTP_EMAIL_TOKEN_VALIDITY = 600


CSRF_TRUSTED_ORIGINS = ["http://url.test"]


OIDC_RP_CLIENT_SECRET = "azer"
MONAIOT_OIDC_OP_SERVER_URL = "https://monaiot.test/auth/realms/MonAIOT-integration/protocol/openid-connect"
OIDC_OP_AUTHORIZATION_ENDPOINT = f"{MONAIOT_OIDC_OP_SERVER_URL}/auth"
OIDC_OP_TOKEN_ENDPOINT = f"{MONAIOT_OIDC_OP_SERVER_URL}/token"
OIDC_OP_USER_ENDPOINT = f"{MONAIOT_OIDC_OP_SERVER_URL}/userinfo"
OIDC_OP_JWKS_ENDPOINT = f"{MONAIOT_OIDC_OP_SERVER_URL}/certs"

DJANGO_VITE = {"default": {"dev_mode": True}}
SKIP_SIRET_CHECK = True
