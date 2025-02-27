# MonAIOT constants
from django.db import models
from django.utils.translation import gettext_lazy as _

from accounts.constants import MONAIOT, PROCONNECT

MANAGER_ID = 4
ADMIN_ID = 2
GUN_ID = 3
GUN_READER_ID = 6  # administration centrale
GUN_READER_ALLOWED_APPLICATION_ID = 3
GUN_READER_ALLOWED_SERVICE_ID = 59
ALLOWED_PROFILES = {MANAGER_ID, ADMIN_ID, GUN_ID, GUN_READER_ID}
ALLOWED_PERIMETER = "ICPE"


class ProviderChoice(models.TextChoices):
    MONAIOT = MONAIOT, _("MonAIOT")
    PROCONNECT = PROCONNECT, _("Proconnect")
