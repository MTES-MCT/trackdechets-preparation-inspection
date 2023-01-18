import uuid

from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _

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
    is_active = models.BooleanField(
        _("active"), default=True, help_text=_("Should this user be treated as active.")
    )
    is_staff = models.BooleanField(
        _("staff status"),
        default=False,
        help_text=_(
            "Can the user log into this admin site. ONLY SET THIS FOR SUPERADMINS USERS!"
        ),
    )
    date_joined = models.DateTimeField(_("date joined"), default=timezone.now)
    objects = UserManager()

    class Meta:
        verbose_name = _("User")
        verbose_name_plural = _("Users")
        app_label = "accounts"

    def __str__(self):
        return self.username
