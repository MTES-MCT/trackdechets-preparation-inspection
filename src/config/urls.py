"""Inspection URL Configuration"""
from django.conf import settings
from django.contrib import admin
from django.contrib.staticfiles.storage import staticfiles_storage
from django.http import HttpResponseNotFound
from django.urls import include, path
from django.views.generic.base import RedirectView
from django_otp.admin import OTPAdminSite

from sheets.views import PrivateHomeView, PublicHomeView

# Admin config
admin.site.index_title = "Administration de l'outil de fiche d'inspection"
admin.site.__class__ = OTPAdminSite

urlpatterns = [
    path(
        "favicon.ico",
        RedirectView.as_view(permanent=True, url=staticfiles_storage.url("img/favicon.ico")),
    ),
    path(f"{settings.ADMIN_SLUG}/login/", HttpResponseNotFound),
    path("grappelli/", include("grappelli.urls")),  # grappelli URLS
    path(f"{settings.ADMIN_SLUG}/", admin.site.urls),
    path("", PublicHomeView.as_view(), name="public_home"),
    path("home/", PrivateHomeView.as_view(), name="private_home"),
    path("accounts/", include("accounts.urls")),
    path("content/", include("content.urls")),
    path("sheets/", include("sheets.urls")),
]

if settings.DEBUG:
    urlpatterns += [
        path("__debug__/", include("debug_toolbar.urls")),
    ]
