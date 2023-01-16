from .base import *  # noqa
from .base import env

DEBUG = True

SECRET_KEY = "xyzabcdefghu"

INSTALLED_APPS = ["whitenoise.runserver_nostatic"] + INSTALLED_APPS  # noqa F405

EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"
MESSAGE_RECIPIENT = env("MESSAGE_RECIPIENT")

ALLOWED_HOSTS = ["*"]
