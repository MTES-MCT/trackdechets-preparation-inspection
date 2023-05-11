"""Inspection URL Configuration"""
from django.conf import settings
from django.contrib import admin
from django.contrib.staticfiles.storage import staticfiles_storage
from django.urls import include, path
from django.views.generic.base import RedirectView

from sheets.views import HomeView

# Admin config
admin.site.index_title = "Administration de l'outil de fiche d'inspection"


urlpatterns = [
    path(
        "favicon.ico",
        RedirectView.as_view(
            permanent=True, url=staticfiles_storage.url("img/favicon.ico")
        ),
    ),
    path("grappelli/", include("grappelli.urls")),  # grappelli URLS
    path(f"{settings.ADMIN_SLUG}/", admin.site.urls),
    path("", HomeView.as_view(), name="home"),
    path("accounts/", include("accounts.urls")),
    path("content/", include("content.urls")),
    path("sheets/", include("sheets.urls")),
]

if settings.DEBUG:
    urlpatterns += [
        path("__debug__/", include("debug_toolbar.urls")),
    ]
