from django import template

from ..constants import RegistryV2ExportState

register = template.Library()


@register.simple_tag
def registry_badge_class(state: str) -> str:
    css_classes = {
        RegistryV2ExportState.PENDING: "fr-badge--new",
        RegistryV2ExportState.STARTED: "fr-badge--info",
        RegistryV2ExportState.FAILED: "fr-badge--error",
        RegistryV2ExportState.CANCELED: "fr-badge--error",
        RegistryV2ExportState.SUCCESSFUL: "fr-badge--success",
    }

    return css_classes.get(state, "")
