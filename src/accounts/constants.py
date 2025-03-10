from django.db import models
from django.utils.translation import gettext_lazy as _


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
ADMIN_CENTRALE_OBSERVATOIRE_AND_STAFF = [
    UserCategoryChoice.STAFF_TD,
    UserCategoryChoice.OBSERVATOIRE,
    UserCategoryChoice.ADMINISTRATION_CENTRALE,
]


class UserTypeChoice(models.TextChoices):
    HUMAN = "HUMAN", _("Human")
    API = "API", _("api")


MONAIOT = "MONAIOT"
PROCONNECT = "PROCONNECT"


class OIDCTypeChoice(models.TextChoices):
    MONAIOT = MONAIOT, _("MonAIOT")
    PROCONNECT = PROCONNECT, _("Proconnect")
