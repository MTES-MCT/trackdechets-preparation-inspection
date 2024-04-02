from allauth.account.signals import user_logged_in, user_signed_up
from django.apps import AppConfig

from .signals import mon_aiot_post_login_callback, mon_aiot_post_signup_callback


class MyAppConfig(AppConfig):
    name = "aiot_provider"

    def ready(self):
        user_signed_up.connect(mon_aiot_post_signup_callback)
        user_logged_in.connect(mon_aiot_post_login_callback)
