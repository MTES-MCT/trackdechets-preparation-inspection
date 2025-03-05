import uuid

from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _

from .constants import OIDCTypeChoice, UserCategoryChoice, UserTypeChoice
from .managers import UserManager


class User(AbstractBaseUser, PermissionsMixin):
    """User models."""

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = [
        "username",
    ]
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    email = models.EmailField(_("Email address"), unique=True)
    username = models.CharField(_("User name"), max_length=250)
    is_active = models.BooleanField(_("active"), default=True, help_text=_("Should this user be treated as active."))
    is_staff = models.BooleanField(
        _("staff status"),
        default=False,
        help_text=_("Can the user log into this admin site. ONLY SET THIS FOR SUPERADMINS USERS!"),
    )
    date_joined = models.DateTimeField(_("date joined"), default=timezone.now)

    oidc_connexion = models.CharField(
        _("OIDC connexion"),
        choices=OIDCTypeChoice,
        help_text=_("Did this user already log in with OIDC ?"),
        blank=True,
    )
    oidc_signup = models.CharField(
        _("OIDC inscription"), choices=OIDCTypeChoice, help_text=_("Did this user sign up in with OIDC ?"), blank=True
    )

    user_type = models.CharField(_("User Type"), choices=UserTypeChoice, default=UserTypeChoice.HUMAN, max_length=30)
    user_category = models.CharField(
        _("User Category"), choices=UserCategoryChoice, default=UserCategoryChoice.INSPECTEUR_ICPE, max_length=30
    )
    objects = UserManager()

    class Meta:
        verbose_name = _("User")
        verbose_name_plural = _("Users")
        app_label = "accounts"

    def __str__(self):
        return self.username

    @property
    def is_api(self):
        return self.user_type == UserTypeChoice.API

    @property
    def is_observatoire(self):
        return self.user_category == UserCategoryChoice.OBSERVATOIRE

    @property
    def is_administration_centrale(self):
        return self.user_category == UserCategoryChoice.ADMINISTRATION_CENTRALE

    def is_allowed_to_login_with_password(self):
        return not self.oidc_signup and not self.oidc_connexion
