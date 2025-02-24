import uuid

from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _

from .managers import UserManager


class UserCategoryChoice(models.TextChoices):
    STAFF_TD = "STAFF_TD", _("Staff Trackdéchets")
    ADMINISTRATION_CENTRALE = "ADMINISTRATION_CENTRALE", _("Administration centrale")
    INSPECTEUR_ICPE = "INSPECTEUR_ICPE", _("Inspecteur ICPE")
    CTT = "CTT", _("CTT - Contrôleur des transports routiers")
    INSPECTION_TRAVAIL = "INSPECTION_TRAVAIL", _("Inspection du travail")
    GENDARMERIE = "GENDARMERIE", _("Gendarmerie")
    ARS = "ARS", _("ARS")
    DOUANE = "DOUANE", _("Douane")
    OBSERVATOIRE = "OBSERVATOIRE", _("Observatoire")


ALL_BUT_OBSERVATOIRE = [
    UserCategoryChoice.STAFF_TD,
    UserCategoryChoice.ADMINISTRATION_CENTRALE,
    UserCategoryChoice.INSPECTEUR_ICPE,
    UserCategoryChoice.CTT,
    UserCategoryChoice.INSPECTION_TRAVAIL,
    UserCategoryChoice.GENDARMERIE,
    UserCategoryChoice.ARS,
    UserCategoryChoice.DOUANE,
]
OBSERVATOIRE_AND_STAFF = [UserCategoryChoice.STAFF_TD, UserCategoryChoice.OBSERVATOIRE]


ALL_USER_CATEGORIES = ALL_BUT_OBSERVATOIRE + OBSERVATOIRE_AND_STAFF


class UserTypeChoice(models.TextChoices):
    HUMAN = "HUMAN", _("Human")
    API = "API", _("api")


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
        return self.user_type == UserTypeChoice.API

    @property
    def is_observatoire(self):
        return self.user_category == UserCategoryChoice.OBSERVATOIRE
