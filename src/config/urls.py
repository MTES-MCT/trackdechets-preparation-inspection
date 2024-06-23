"""Inspection URL Configuration"""

from django.conf import settings
from django.contrib import admin
from django.contrib.staticfiles.storage import staticfiles_storage
from django.http import HttpResponseNotFound
from django.urls import include, path
from django.views.generic.base import RedirectView
from django_otp.admin import OTPAdminSite

from aiot_provider.views import temp_aiot_login_page
from sheets.views import PrivateHomeView, PublicHomeView

# Admin config
admin.site.index_title = "Administration de l'outil de fiche d'inspection"
admin.site.__class__ = OTPAdminSite

urlpatterns = [
    path(
        "favicon.ico",
        RedirectView.as_view(permanent=True, url=staticfiles_storage.url("img/favicon.ico")),
    ),
    path(f"{settings.ADMIN_SLUG}/login/", HttpResponseNotFound),  # disable admin logout
    path("grappelli/", include("grappelli.urls")),  # grappelli URLS
    path(f"{settings.API_SLUG}/api/v1/", include("api.urls")),
    path(f"{settings.ADMIN_SLUG}/", admin.site.urls),
    path("", PublicHomeView.as_view(), name="public_home"),
    path("home/", PrivateHomeView.as_view(), name="private_home"),
    path("local-accounts/", include("accounts.urls")),
    path("accounts/signup/", HttpResponseNotFound),
    path("accounts/login/", HttpResponseNotFound),
    path("accounts/reauthenticate/", HttpResponseNotFound),
    path("accounts/password/change/", HttpResponseNotFound),
    path("accounts/password/reset/", HttpResponseNotFound),
    path("accounts/", include("allauth.urls")),
    path("content/", include("content.urls")),
    path("sheets/", include("sheets.urls")),
    path("monaiot-login/", temp_aiot_login_page),
]

if settings.DEBUG:
    urlpatterns += [
        path("__debug__/", include("debug_toolbar.urls")),
    ]
