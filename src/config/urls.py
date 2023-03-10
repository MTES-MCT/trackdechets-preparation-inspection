"""inspection URL Configuration"""
from django.conf import settings
from django.contrib import admin
from django.urls import include, path

from sheets.views import HomeView

urlpatterns = [
    path(f"{settings.ADMIN_SLUG}/", admin.site.urls),
    path("", HomeView.as_view(), name="home"),
    path("accounts/", include("accounts.urls")),
    path("sheets/", include("sheets.urls")),
]

if settings.DEBUG:
    urlpatterns += [
        path("__debug__/", include("debug_toolbar.urls")),
    ]
