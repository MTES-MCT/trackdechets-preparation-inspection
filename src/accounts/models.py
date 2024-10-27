import uuid

from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _

from .managers import UserManager


class User(AbstractBaseUser, PermissionsMixin):
    """User models."""

    class UserTypeChoice(models.TextChoices):
        HUMAN = "HUMAN", _("Human")
        API = "API", _("api")

    class UserCategoryChoice(models.TextChoices):
        STAFF_TD = "STAFF_TD", _("Staff Trackdéchets")
        ADMINISTRATION_CENTRALE = "ADMINISTRATION_CENTRALE", _("Administration centrale")
        INSPECTEUR_ICPE = "INSPECTEUR_ICPE", _("Inspecteur ICPE")
        CTT = "CTT", _("CTT - contrôleur des transports routiers")
        INSPECTION_TRAVAIL = "INSPECTION_TRAVAIL", _("Inspection du travail")
        GENDARMERIE = "GENDARMERIE", _("Gendarmerie")
        ARS = "ARS", _("ARS")

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
    monaiot_connexion = models.BooleanField(
        _("MonAIOT connexion"), help_text=_("Did this user already log in with MonAIOT ?"), default=False
    )
    monaiot_signup = models.BooleanField(
        _("MonAIOT inscription"), help_text=_("Did this user sign up in with MonAIOT ?"), default=False
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
        return self.user_type == self.UserTypeChoice.API
