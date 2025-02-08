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

MONAIOT_SERVER_URL = "http://lorem.test"
MONAIOT_REALM = "realm"
MONAIOT_CLIENT_ID = "td"
MONAIOT_SECRET = "xyz"
CSRF_TRUSTED_ORIGINS = ["http://url.test"]

WELL_KNOWN_URL = f"{MONAIOT_SERVER_URL}/auth/realms/{MONAIOT_REALM}/.well-known/openid-configuration"
SOCIALACCOUNT_PROVIDERS = {
    "monaiot": {
        "APPS": [
            {
                "provider_id": "monaiot",
                "name": "monaiot",
                "client_id": MONAIOT_CLIENT_ID,
                "secret": MONAIOT_SECRET,
                "settings": {"server_url": WELL_KNOWN_URL, "token_auth_method": "client_secret_jwt"},
            }
        ],
        "SCOPE": ["openid"],
    }
}
DJANGO_VITE = {"default": {"dev_mode": True}}
SKIP_SIRET_CHECK = True
