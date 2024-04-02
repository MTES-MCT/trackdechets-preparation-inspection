from .base import *  # noqa

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql_psycopg2",
        "NAME": "inspection_test",
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

MONAIOT_SERVER_URL = "https://lorem.test"
MONAIOT_REALM = "realm"
MONAIOT_CLIENT_ID = "td"
MONAIOT_SECRET = "xyz"
CSRF_TRUSTED_ORIGINS = ["https://url.test"]
