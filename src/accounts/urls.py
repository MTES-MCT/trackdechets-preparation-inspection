from django.contrib.auth.views import LoginView, logout_then_login
from django.urls import path

from .forms import EmailAuthenticationForm

urlpatterns = [
    path(
        "login/",
        LoginView.as_view(
            template_name="accounts/login.html",
            authentication_form=EmailAuthenticationForm,
            redirect_authenticated_user=True,
        ),
        name="login",
    ),
    path("logout/", logout_then_login, name="logout"),
]
