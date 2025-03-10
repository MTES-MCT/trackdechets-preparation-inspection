from django.contrib.auth import get_user_model
from django.contrib.auth.backends import ModelBackend
from django.core.exceptions import PermissionDenied

UserModel = get_user_model()


class RestrictedLoginBackend(ModelBackend):
    """Restrict email/password login to non oidc users"""

    def authenticate(self, request, username=None, password=None, **kwargs):
        user = super().authenticate(request, username, password, **kwargs)
        if not user:
            return user

        if user.oidc_connexion or user.oidc_signup:
            raise PermissionDenied("Vous n'êtes pas autorisé à vous connecter par email et mot de passe.")

        return user
