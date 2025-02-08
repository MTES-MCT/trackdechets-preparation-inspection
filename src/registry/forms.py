from django.forms import ChoiceField

from sheets.forms import SiretForm

from .constants import (
    REGISTRY_FORMAT_CSV,
    REGISTRY_FORMAT_XLS,
    REGISTRY_TYPE_ALL,
    REGISTRY_TYPE_INCOMING,
    REGISTRY_TYPE_OUTGOING,
    REGISTRY_TYPE_TRANSPORTED,
)


class RegistryPrepareForm(SiretForm):
    is_registry = True

    registry_type = ChoiceField(
        label="Type de registre",
        choices=(
            (REGISTRY_TYPE_ALL, "Exhaustif"),
            (REGISTRY_TYPE_INCOMING, "Entrant"),
            (REGISTRY_TYPE_OUTGOING, "Sortant"),
            (REGISTRY_TYPE_TRANSPORTED, "Transporté"),
        ),
    )
    registry_format = ChoiceField(
        label="Format",
        choices=((REGISTRY_FORMAT_CSV, ".csv (données tabulées)"), (REGISTRY_FORMAT_XLS, ".xls (Excel)")),
    )
