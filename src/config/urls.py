"""Inspection URL Configuration"""

from django.conf import settings
from django.contrib import admin
from django.contrib.staticfiles.storage import staticfiles_storage
from django.http import Http404
from django.urls import include, path
from django.views.generic.base import RedirectView
from django_otp.admin import OTPAdminSite

from aiot_provider.views import temp_aiot_login_page
from sheets.views import PrivateHomeView, PublicHomeView

# Admin config
admin.site.index_title = "Administration de l'outil de fiche d'inspection"
admin.site.__class__ = OTPAdminSite


def not_found(request):
    raise Http404()


urlpatterns = [
    path(
        "favicon.ico",
        RedirectView.as_view(permanent=True, url=staticfiles_storage.url("img/favicon.ico")),
    ),
    path(f"{settings.ADMIN_SLUG}/login/", not_found),  # disable admin logout
    path("grappelli/", include("grappelli.urls")),  # grappelli URLS
    path(f"{settings.API_SLUG}/api/v1/", include("api.urls")),
    path(f"{settings.ADMIN_SLUG}/", admin.site.urls),
    path("", PublicHomeView.as_view(), name="public_home"),
    path("home/", PrivateHomeView.as_view(), name="private_home"),
    path("local-accounts/", include("accounts.urls")),
    # path("accounts/signup/", HttpResponseNotFound, name="allauth_signup"),
    path("accounts/login/", not_found),
    path("accounts/logout/", not_found),
    path("accounts/inactive/", not_found),
    # path("accounts/3rdparty/signup/", not_found),
    path("accounts/", include("allauth.urls")),
    path("content/", include("content.urls")),
    path("sheets/", include("sheets.urls")),
    path("registry/", include("registry.urls")),
    path("roadcontrol/", include("roadcontrol.urls")),
    path("map/", include("maps.urls")),
    path("data-exports/", include("data_exports.urls")),
    path("monaiot-login/", temp_aiot_login_page),
]

if settings.DEBUG:
    urlpatterns += [
        path("__debug__/", include("debug_toolbar.urls")),
    ]
