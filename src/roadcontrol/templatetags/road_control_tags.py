from django import template
from django.templatetags.static import static

from ..constants import TYPE_BSDA, TYPE_BSDASRI, TYPE_BSDD, TYPE_BSFF, TYPE_BSPAOH, TYPE_BSVHU, BsdStatus

register = template.Library()


@register.simple_tag
def weight_unit(bsd_type: str) -> str:
    if bsd_type in [TYPE_BSPAOH, TYPE_BSDASRI]:
        return "kg"
    return "t"


@register.simple_tag
def bsd_icon(bsd_type: str) -> str:
    icons = {
        TYPE_BSDD: "custom-icons/icon-bsdd.svg",
        TYPE_BSPAOH: "custom-icons/icon-bspaoh.svg",
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
        TYPE_BSPAOH: "Icône bspaoh",
        TYPE_BSDASRI: "Icône bsdasri",
        TYPE_BSFF: "Icône bsff",
        TYPE_BSDA: "Icône bsda",
        TYPE_BSVHU: "Icône bsvhu",
    }
    return alts[bsd_type]


accepted = "ACCEPTED"
awaiting_group = "AWAITING_GROUP"
canceled = "CANCELED"
draft = "DRAFT"
followed_with_pnttd = "FOLLOWED_WITH_PNTTD"
grouped = "GROUPED"
no_traceability = "NO_TRACEABILITY"
processed = "PROCESSED"
received = "RECEIVED"
refused = "REFUSED"
resealed = "RESEALED"
resent = "RESENT"
sealed = "SEALED"
sent = "SENT"
signed_by_producer = "SIGNED_BY_PRODUCER"
signed_by_temp_storer = "SIGNED_BY_TEMP_STORER"
temp_stored = "TEMP_STORED"
temp_storer_accepted = "TEMP_STORER_ACCEPTED"

BROUILLON = "Brouillon"
RECU = "Reçu, en attente d'acceptation"
ACCEPTE = "ACCEPTÉ, EN ATTENTE DE TRAITEMENT"
TRAITE = "Traité"
ANNEXE_BORDEREAU_SUITE = "Annexé à un bordereau suite"
TRAITE_AVEC_RUPTURE_TRACABILITE = "Traité (avec rupture de traçabilité)"
REFUSE = "REFUSÉ"
ARRIVE_ENTREPOS_PROVISOIRE = "ARRIVÉ À L’ENTREPOSAGE PROVISOIRE, EN ATTENTE D’ACCEPTATION"
ENTREPOS_TEMPORAIREMENT = "entreposé temporairement ou en reconditionnement"
BSD_SUITE_PREPARE = "BSD suite préparé"
SIGNE_PAR_TRANSPORTEUR = "signé par le transporteur"

INITIAL = "publié"
SIGNE_PAR_EMETTEUR = "signé par l’émetteur"
SIGNER_PAR_ENTREPOS_PROVISOIRE = "Signé par l'installation d'entreposage provisoire"
PARTIELLEMENT_REFUSE = "Partiellement refusé"
SUIVI_PAR_PNTTD = "Suivi via PNTTD"
SIGNER_PAR_ENTREPRISE_TRAVAUX = "Signé par l'entreprise de travaux"
EN_ATTENTE_BSD_SUITE = "En attente d'un bordereau suite"
ANNULE = "Annulé"
EN_ATTENTE_TRAITEMENT = "En attente de traitement"


@register.inclusion_tag("roadcontrol/tags/status_badge.html")
def status_badge(status: str, bsd_type: str) -> dict:
    # a few matches are missing, but should not appear in results
    verbose = status
    match status:
        case BsdStatus.DRAFT:
            verbose = BROUILLON
        case BsdStatus.SEALED:
            verbose = INITIAL
        case BsdStatus.SENT:
            verbose = SIGNE_PAR_TRANSPORTEUR
        case BsdStatus.RECEIVED:
            if bsd_type in [TYPE_BSDASRI, TYPE_BSPAOH]:
                verbose = ACCEPTE
            else:
                verbose = RECU
        case BsdStatus.ACCEPTED:
            verbose = ACCEPTE
        case BsdStatus.PROCESSED:
            verbose = TRAITE
        case BsdStatus.AWAITING_CHILD:
            verbose = TRAITE
        case BsdStatus.GROUPED:
            if bsd_type == TYPE_BSFF:
                verbose = EN_ATTENTE_TRAITEMENT
            if bsd_type == TYPE_BSDA:
                verbose = ANNEXE_BORDEREAU_SUITE
        case BsdStatus.NO_TRACEABILITY:
            verbose = TRAITE_AVEC_RUPTURE_TRACABILITE
        case BsdStatus.REFUSED:
            verbose = REFUSE
        case BsdStatus.TEMP_STORED:
            verbose = ARRIVE_ENTREPOS_PROVISOIRE
        case BsdStatus.TEMP_STORER_ACCEPTED:
            verbose = ENTREPOS_TEMPORAIREMENT
        case BsdStatus.RESEALED:
            verbose = BSD_SUITE_PREPARE
        case BsdStatus.RESENT:
            verbose = SIGNE_PAR_TRANSPORTEUR
        case BsdStatus.SIGNED_BY_PRODUCER:
            verbose = SIGNE_PAR_EMETTEUR
        case BsdStatus.SIGNED_BY_TEMP_STORER:
            verbose = SIGNER_PAR_ENTREPOS_PROVISOIRE
        case BsdStatus.PARTIALLY_REFUSED:
            verbose = PARTIELLEMENT_REFUSE
        case BsdStatus.FOLLOWED_WITH_PNTTD:
            verbose = SUIVI_PAR_PNTTD
        case BsdStatus.AWAITING_GROUP:
            verbose = EN_ATTENTE_BSD_SUITE
        case BsdStatus.INTERMEDIATELY_PROCESSED:
            verbose = EN_ATTENTE_TRAITEMENT

    return {"status": status, "verbose": verbose}
