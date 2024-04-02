from django.urls import include, path, re_path

from .views import PostMonAiotSignup, callback, login

app = "aiot_provider"


urlpatterns = [
    path("post-signup/", PostMonAiotSignup.as_view(), name="post_monaiot_signup"),
    re_path(
        r"^(?P<provider_id>[^/]+)/",
        include(
            [
                path(
                    "login/",
                    login,
                    name="monaiot_login",
                ),
                path(
                    "login/callback/",
                    callback,
                    name="monaiot_callback",
                ),
            ]
        ),
    ),
]
