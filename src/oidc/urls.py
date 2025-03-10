from django.urls import path

from .views import (
    MonAiotAuthentError,
    MonaiotOIDCAuthenticationCallbackView,
    MonaiotOIDCAuthenticationRequestView,
    PostMonAiotSignup,
    ProconnectAuthentError,
    ProconnectOIDCAuthenticationCallbackView,
    ProconnectOIDCAuthenticationRequestView,
)

urlpatterns = [
    path("post-signup/", PostMonAiotSignup.as_view(), name="post_monaiot_signup"),
    path(
        "monaiot-oidc-error/",
        MonAiotAuthentError.as_view(),
        name="mon_aiot_authent_error",
    ),
    path(
        "proconnect-oidc-error/",
        ProconnectAuthentError.as_view(),
        name="proconnect_authent_error",
    ),
    path(
        "monaiot-authenticate/",
        MonaiotOIDCAuthenticationRequestView.as_view(),
        name="monaiot_oidc_authentication_init",
    ),
    path(
        "proconnect-authenticate/",
        ProconnectOIDCAuthenticationRequestView.as_view(),
        name="proconnect_oidc_authentication_init",
    ),
    path(
        "monaiot-callback/",
        MonaiotOIDCAuthenticationCallbackView.as_view(),
        name="monaiot_oidc_authentication_callback",
    ),
    path(
        "proconnect-callback/",
        ProconnectOIDCAuthenticationCallbackView.as_view(),
        name="proconnect_oidc_authentication_callback",
    ),
]
