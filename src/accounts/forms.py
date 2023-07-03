from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserChangeForm, UserCreationForm
from simplemathcaptcha.fields import MathCaptchaField

UserModel = get_user_model()


class EmailLoginForm(forms.Form):
    email = forms.EmailField()
    captcha = MathCaptchaField(label="Test anti robots")


class AdminCustomUserCreationForm(UserCreationForm):
    class Meta:
        model = UserModel
        fields = ("username", "email")


class AdminCustomUserChangeForm(UserChangeForm):
    class Meta:
        model = UserModel
        fields = ("username", "email")
