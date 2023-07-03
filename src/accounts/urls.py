from django.contrib.auth.views import logout_then_login
from django.urls import path

from .views import EmailLoginView, MagicLinkView, my_ip

urlpatterns = [
    path(
        "login/",
        EmailLoginView.as_view(),
        name="login",
    ),
    path("magic/login/", MagicLinkView.as_view(), name="magic_login"),
    path("logout/", logout_then_login, name="logout"),
    path(
        "my_ip/",
        my_ip,
    ),
]
