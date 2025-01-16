from django.urls import path

from .views import MonAiotAuthenttError, PostMonAiotSignup

urlpatterns = [
    path("post-signup/", PostMonAiotSignup.as_view(), name="post_monaiot_signup"),
    path(
        "oidc-error/",
        MonAiotAuthenttError.as_view(),
        name="mon_aiot_authent_error",
    ),
]
