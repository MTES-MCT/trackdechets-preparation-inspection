"""Inspection URL Configuration"""
from django.conf import settings
from django.contrib import admin
from django.urls import include, path
from django.views.defaults import page_not_found

from sheets.views import HomeView

urlpatterns = [
    # path(f"{settings.ADMIN_SLUG}/login/", page_not_found, {"exception": "Page not found"}, name="disabled_login"),
    path(f"{settings.ADMIN_SLUG}/", admin.site.urls),
    # path(f"{settings.ADMIN_SLUG}/login", page_not_found, {"exception": "Page not found"}, name="disabled_login"),
    path("", HomeView.as_view(), name="home"),
    path("accounts/", include("accounts.urls")),
    path("sheets/", include("sheets.urls")),
]

if settings.DEBUG:
    urlpatterns += [
        path("__debug__/", include("debug_toolbar.urls")),
    ]
