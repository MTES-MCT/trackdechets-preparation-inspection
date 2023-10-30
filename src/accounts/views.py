from braces.views import LoginRequiredMixin
from django.conf import settings
from django.contrib import messages
from django.contrib.auth.views import LoginView as BaseLoginView
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.views.generic import FormView
from django_otp import login as otp_login
from django_otp.plugins.otp_email.models import EmailDevice

from accounts.forms import ResendTokenEmailForm, SecondFactorTokenForm
from common.redis import gen_otp_email_key, redis_client


def create_email_device(user):
    device = EmailDevice.objects.create(email=user.email, user=user, name="email_device")
    return device


class SendSecondFactorMailMixin:
    def process(self):
        user = self.request.user
        devices = EmailDevice.objects.devices_for_user(user)
        if not devices:
            device = create_email_device(user)
        else:
            device = devices[0]
        device.generate_challenge()


class LoginView(SendSecondFactorMailMixin, BaseLoginView):
    def form_valid(self, form):
        res = super().form_valid(form)
        self.process()
        return res


class VerifyView(LoginRequiredMixin, FormView):
    form_class = SecondFactorTokenForm
    template_name = "accounts/second_factor.html"
    success_url = reverse_lazy("private_home")

    def get_form_kwargs(self):
        kw = super().get_form_kwargs()
        kw.update({"user": self.request.user})

        return kw

    def form_valid(self, form):
        otp_login(self.request, self.request.user.otp_device)
        return super().form_valid(form)


class ResendTokenEmail(SendSecondFactorMailMixin, LoginRequiredMixin, FormView):
    """
    Request a new email contianing token.
    Throttled every OTP_EMAIL_THROTTLE_DELAY seconds.
    """

    form_class = ResendTokenEmailForm
    template_name = "accounts/second_factor.html"  # not used but required
    success_url = reverse_lazy("second_factor")

    def get(self, request, *args, **kwargs):
        return HttpResponseRedirect(self.get_success_url())

    def form_invalid(self, form):
        messages.error(self.request, form.errors.get("__all__"))
        return HttpResponseRedirect(self.get_success_url())

    def form_valid(self, form):
        self.process()
        redis_key = gen_otp_email_key(self.request.user)
        redis_client.set(redis_key, "_", ex=settings.OTP_EMAIL_THROTTLE_DELAY)
        return super().form_valid(form)

    def get_form_kwargs(self):
        kw = super().get_form_kwargs()
        kw.update({"user": self.request.user})
        return kw
