from django.conf import settings
from django.contrib.auth import get_user_model
from django.core.mail import EmailMessage
from django.http import HttpResponse
from django.shortcuts import render
from django.urls import reverse
from django.utils.decorators import method_decorator
from django.views.generic import FormView
from django_ratelimit.decorators import ratelimit
from ipware import get_client_ip
from sesame.utils import get_query_string
from sesame.views import LoginView as SesameLoginView

from .forms import EmailLoginForm


def url_join(*args):
    """
    Joins given arguments into an url. Trailing but not leading slashes are
    stripped for each argument.
    """

    return "/".join(map(lambda x: str(x).strip("/"), args))


User = get_user_model()


class EmailLoginView(FormView):
    template_name = "accounts/login.html"
    form_class = EmailLoginForm

    @method_decorator(ratelimit(key="user_or_ip", rate="3/m"))
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)

    def form_valid(self, form):
        email = form.cleaned_data["email"]
        user = None
        try:
            user = User.objects.get(email=email)

        except User.DoesNotExist:
            pass
        # send mail if user found
        if user:
            link = url_join(
                settings.BASE_URL, reverse("magic_login"), get_query_string(user)
            )

            subject = "Trackdéchets fiche d'inspection"
            body = f"""\
                    Bonjour,

                    Pour vous connecter à la fiche d'inspection:

                        {link}

                    Merci!
                    """

            message = EmailMessage(
                subject=subject,
                body=body,
                from_email=settings.DEFAULT_FROM_EMAIL,
                to=[user.email],
            )
            message.send()
        # user found or not, render success
        return render(self.request, "accounts/login_success.html")


class MagicLinkView(SesameLoginView):
    @method_decorator(ratelimit(key="user_or_ip", rate="3/m"))
    def get(self, request):
        return super().get(request)


def lockout_view(request, *args):
    return render(request, "accounts/lockout.html")


def my_ip(request, *args):
    ip, _ = get_client_ip(request)
    return HttpResponse(ip)
