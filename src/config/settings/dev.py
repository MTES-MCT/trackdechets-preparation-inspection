from .base import *  # noqa

SECRET_KEY = "xyzabcdefghu"

INSTALLED_APPS += [  # noqa F405
    "whitenoise.runserver_nostatic",
    "debug_toolbar",
    "django_extensions",
]

ALLOWED_HOSTS = ["*"]

INTERNAL_IPS = [
    "127.0.0.1",
]

MIDDLEWARE = (
    MIDDLEWARE[:1]  # noqa
    + [
        "debug_toolbar.middleware.DebugToolbarMiddleware",
    ]
    + MIDDLEWARE[1:]  # noqa
)

# Celery config
CELERY_BROKER_URL = "redis://localhost:6379/0"
CELERY_RESULT_BACKEND = "redis"

OTP_EMAIL_TOKEN_VALIDITY = 600
ALLOWED_HOSTS = ["dev.inspection.trackdechets.beta.gouv.fr", "127.0.0.1"]
