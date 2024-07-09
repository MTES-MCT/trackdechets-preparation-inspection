import datetime as dt

from django.utils import timezone


def mon_aiot_post_login_callback(*args, **kwargs):
    """Set `monaiot_connexion`  on User model ."""
    try:
        request = kwargs.get("request")
    except KeyError:
        return

    try:
        slg = kwargs["sociallogin"]
    except KeyError:
        return
    ser = slg.serialize()
    try:
        provider = ser["account"]["provider"]

    except KeyError:
        return

    user = request.user
    if provider != "monaiot":
        return
    if not user.monaiot_connexion:
        user.monaiot_connexion = True

        user.save()


def mon_aiot_post_signup_callback(*args, **kwargs):
    """Allauth does not populate session data on signup (as it does on login) so we catch a signal to handle that.
    These session data are useful to tell apart users connected from monAIOT and from email/password login.

    We also mark the user model `monaiot_connexion` field  as True
    """
    try:
        slg = kwargs["sociallogin"]
    except KeyError:
        return
    ser = slg.serialize()

    try:
        extra_data = ser["account"]["extra_data"]
        provider = ser["account"]["provider"]

        sub = extra_data["sub"]
        request = kwargs.get("request")
    except KeyError:
        return
    if provider != "monaiot":
        return
    now = timezone.now()
    ts = dt.datetime.timestamp(now)
    account_authentication_methods = [{"method": "socialaccount", "at": ts, "provider": "monaiot", "uid": sub}]
    session = request.session
    session["account_authentication_methods"] = account_authentication_methods
    user = kwargs.get("user")
    if user:
        user.monaiot_signup = True
        user.save()
