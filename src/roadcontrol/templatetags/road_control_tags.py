from django import template
from django.templatetags.static import static

from ..constants import TYPE_BPAOH, TYPE_BSDA, TYPE_BSDASRI, TYPE_BSDD, TYPE_BSFF, TYPE_BSVHU

register = template.Library()


@register.simple_tag
def weight_unit(bsd_type: str) -> str:
    if bsd_type in [TYPE_BPAOH, TYPE_BSDASRI]:
        return "kg"
    return "t"


@register.simple_tag
def bsd_icon(bsd_type: str) -> str:
    icons = {
        TYPE_BSDD: "custom-icons/icon-bsdd.svg",
        TYPE_BPAOH: "custom-icons/icon-bspaoh.svg",
        TYPE_BSDASRI: "custom-icons/icon-bsdasri.svg",
        TYPE_BSFF: "custom-icons/icon-bsff.svg",
        TYPE_BSDA: "custom-icons/icon-bsda.svg",
        TYPE_BSVHU: "custom-icons/icon-bsvhu.svg",
    }
    icon = icons[bsd_type]
    return static(icon)


@register.simple_tag
def bsd_icon_alt(bsd_type: str) -> str:
    alts = {
        TYPE_BSDD: "Icône bsdd",
        TYPE_BPAOH: "Icône bspaoh",
        TYPE_BSDASRI: "Icône bsdasri",
        TYPE_BSFF: "Icône bsff",
        TYPE_BSDA: "Icône bsda",
        TYPE_BSVHU: "Icône bsvhu",
    }
    return alts[bsd_type]
