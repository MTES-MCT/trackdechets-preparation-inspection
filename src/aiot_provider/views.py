from allauth.socialaccount.providers.oauth2.views import OAuth2CallbackView, OAuth2LoginView
from django.shortcuts import render
from django.views.generic import TemplateView

from common.mixins import FullyLoggedMixin

from .adapter import MonAiotDConnectAdapter


def login(request, provider_id):
    view = OAuth2LoginView.adapter_view(MonAiotDConnectAdapter(request, provider_id))

    return view(request)


def callback(request, provider_id):
    view = OAuth2CallbackView.adapter_view(MonAiotDConnectAdapter(request, provider_id))

    res = view(request)
    user = request.user
    if user.is_anonymous:
        return res

    if not user.monaiot_connexion:
        user.monaiot_connexion = True
        user.save()
    return res


def temp_aiot_login_page(request):
    return render(request, "temp_aiot_login_page.html")


class PostMonAiotSignup(FullyLoggedMixin, TemplateView):
    template_name = "post_monaiot_signup.html"
