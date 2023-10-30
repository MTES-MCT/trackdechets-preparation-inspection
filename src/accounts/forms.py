from django import forms
from django.conf import settings
from django.contrib.auth import authenticate, get_user_model
from django.contrib.auth.forms import UserChangeForm, UserCreationForm
from django.core.exceptions import ValidationError
from django.utils.text import capfirst
from django.utils.translation import gettext_lazy as _
from django_otp.forms import OTPAuthenticationFormMixin
from django_otp.plugins.otp_email.models import EmailDevice

from common.redis import gen_otp_email_key, redis_client

UserModel = get_user_model()


class EmailAuthenticationForm(forms.Form):
    """
    Base class for authenticating users. Extend this to get a form that accepts
    username/password logins.
    """

    email = forms.EmailField(max_length=254, widget=forms.TextInput(attrs={"autofocus": True}))
    password = forms.CharField(label=_("Password"), strip=False, widget=forms.PasswordInput)

    error_messages = {
        "invalid_login": _(
            "Please enter a correct %(username)s and password. Note that both " "fields may be case-sensitive."
        ),
        "inactive": _("This account is inactive."),
    }

    def __init__(self, request=None, *args, **kwargs):
        """
        The 'request' parameter is set for custom auth use by subclasses.
        The form data comes in via the standard 'data' kwarg.
        """
        self.request = request
        self.user_cache = None
        super(EmailAuthenticationForm, self).__init__(*args, **kwargs)

        # Set the label for the "username" field.
        self.username_field = UserModel._meta.get_field(UserModel.USERNAME_FIELD)
        if self.fields["email"].label is None:
            self.fields["email"].label = capfirst(self.username_field.verbose_name)

    def clean(self):
        email = self.cleaned_data.get("email")
        password = self.cleaned_data.get("password")

        if email is not None and password:
            self.user_cache = authenticate(self.request, email=email, password=password)
            if self.user_cache is None:
                raise forms.ValidationError(
                    self.error_messages["invalid_login"],
                    code="invalid_login",
                    params={"username": self.username_field.verbose_name},
                )
            else:
                self.confirm_login_allowed(self.user_cache)

        return self.cleaned_data

    def confirm_login_allowed(self, user):
        """
        Controls whether the given User may log in. This is a policy setting,
        independent of end-user authentication. This default behavior is to
        allow login by active users, and reject login by inactive users.

        If the given user cannot log in, this method should raise a
        ``forms.ValidationError``.

        If the given user may log in, this method should return None.
        """
        if not user.is_active:
            raise forms.ValidationError(self.error_messages["inactive"], code="inactive")

    def get_user_id(self):
        if self.user_cache:
            return self.user_cache.id
        return None

    def get_user(self):
        return self.user_cache


class AdminCustomUserCreationForm(UserCreationForm):
    class Meta:
        model = UserModel
        fields = ("username", "email")


class AdminCustomUserChangeForm(UserChangeForm):
    class Meta:
        model = UserModel
        fields = ("username", "email")


class SecondFactorTokenForm(OTPAuthenticationFormMixin, forms.Form):
    otp_error_messages = {
        **OTPAuthenticationFormMixin.otp_error_messages,
        "invalid_token": "Jeton non valable ou trop ancien. Assurez-vous de bien l’avoir saisi correctement.",
    }
    otp_token = forms.CharField(
        max_length=6,
        label="Copiez votre code de vérification reçu par email",
        widget=forms.TextInput(attrs={"autocomplete": "off"}),
    )

    def __init__(self, user, request=None, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.user = user

    def _chosen_device(self, user):
        devices = EmailDevice.objects.devices_for_user(user)

        return devices[0]

    def clean(self):
        super().clean()

        self.clean_otp(self.user)

        return self.cleaned_data

    def get_user(self):
        return self.user


class VerifyForm(forms.Form):
    code = forms.CharField()


class ResendTokenEmailForm(forms.Form):
    def __init__(self, user, request=None, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.user = user

    def clean(self):
        redis_key = gen_otp_email_key(self.user)
        last_email_sent = redis_client.get(redis_key)
        if last_email_sent:
            raise ValidationError(
                f"Veuillez attendre {int(settings.OTP_EMAIL_THROTTLE_DELAY / 60)} minutes entre chaque demande d'email "
            )
        return super().clean()
