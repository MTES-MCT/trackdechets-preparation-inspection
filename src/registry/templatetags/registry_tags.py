from typing import TypedDict

from django import template

from ..constants import RegistryV2ExportState
from ..models import RegistryV2Export


class ResultDict(TypedDict):
    css_class: str
    verbose_state: str


register = template.Library()


@register.inclusion_tag("registry/templatetags/badge.html")
def registry_badge_class(export: RegistryV2Export) -> ResultDict:
    css_classes = {
        RegistryV2ExportState.PENDING: "fr-badge--new",
        RegistryV2ExportState.STARTED: "fr-badge--info",
        RegistryV2ExportState.FAILED: "fr-badge--error",
        RegistryV2ExportState.CANCELED: "fr-badge--error",
        RegistryV2ExportState.SUCCESSFUL: "fr-badge--success",
    }
    if export.is_timeout and export.state != RegistryV2ExportState.SUCCESSFUL:
        return {"css_class": "fr-badge--error", "verbose_state": RegistryV2ExportState.FAILED.label}
    return {"css_class": css_classes.get(export.state, ""), "verbose_state": export.get_state_display()}
