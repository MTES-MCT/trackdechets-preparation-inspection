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

    return {"status": status, "verbose": verbose}


"""

  switch (status) {
    case BsdStatusCode.Draft:
      return BROUILLON;
    case BsdStatusCode.Sealed:
      return INITIAL;
    case BsdStatusCode.Sent:
      if (bsdType && transporters && transporters.length > 1) {
        // Le code qui suit permet d'afficher "Signé par le transporteur N"
        // en cas de transport multi-modal
        let lastTransporterNumero: Maybe<number> = null;
        if (isBsdd(bsdType)) {
          lastTransporterNumero = (transporters as Transporter[]).filter(t =>
            Boolean(t.takenOverAt)
          ).length;
        } else if (isBsda(bsdType) || isBsff(bsdType)) {
          lastTransporterNumero = (transporters as BsdaTransporter[]).filter(
            t => Boolean(t.transport?.signature?.date)
          ).length;
        }
        if (lastTransporterNumero)
          return SIGNE_PAR_TRANSPORTEUR_N(lastTransporterNumero);
      }
      return SIGNE_PAR_TRANSPORTEUR;
    case BsdStatusCode.Received:
      if (bsdType === BsdType.Bsdasri) {
        return ACCEPTE;
      }
      if (bsdType === BsdType.Bspaoh) {
        return ACCEPTE;
      }
      return RECU;
    case BsdStatusCode.Accepted:
      return ACCEPTE;
    case BsdStatusCode.Processed:
      return TRAITE;
    case BsdStatusCode.AwaitingChild:
    case BsdStatusCode.Grouped:
      if (bsdType === BsdType.Bsff) {
        return EN_ATTENTE_TRAITEMENT;
      }
      if (bsdType === BsdType.Bsda) {
        if (bsdaAnnexed) {
          return ANNEXE_BORDEREAU_SUITE;
        }
        return EN_ATTENTE_BSD_SUITE;
      }
      return ANNEXE_BORDEREAU_SUITE;
    case BsdStatusCode.NoTraceability:
      return TRAITE_AVEC_RUPTURE_TRACABILITE;
    case BsdStatusCode.Refused:
      return REFUSE;
    case BsdStatusCode.TempStored:
      return ARRIVE_ENTREPOS_PROVISOIRE;
    case BsdStatusCode.TempStorerAccepted:
      return ENTREPOS_TEMPORAIREMENT;
    case BsdStatusCode.Resealed:
      return BSD_SUITE_PREPARE;
    case BsdStatusCode.Resent:
      return SIGNE_PAR_TRANSPORTEUR;
    case BsdStatusCode.SignedByProducer:
      return SIGNE_PAR_EMETTEUR;
    case BsdStatusCode.Initial:
      if (isDraft) {
        return BROUILLON;
      } else {
        return INITIAL;
      }
    case BsdStatusCode.SignedByEmitter:
      return SIGNE_PAR_EMETTEUR;
    case BsdStatusCode.SignedByTempStorer:
      return SIGNER_PAR_ENTREPOS_PROVISOIRE;
    case BsdStatusCode.PartiallyRefused:
      return PARTIELLEMENT_REFUSE;
    case BsdStatusCode.FollowedWithPnttd:
      return SUIVI_PAR_PNTTD;
    case BsdStatusCode.SignedByWorker:
      return SIGNER_PAR_ENTREPRISE_TRAVAUX;
    case BsdStatusCode.AwaitingGroup:
      if (bsdType === BsdType.Bsdasri) {
        if (operationCode === "R12" || operationCode === "D13") {
          return EN_ATTENTE_BSD_SUITE;
        }
        return ANNEXE_BORDEREAU_SUITE;
      }
      return EN_ATTENTE_BSD_SUITE;
    case BsdStatusCode.IntermediatelyProcessed:
      if (bsdType === BsdType.Bsff) {
        return EN_ATTENTE_TRAITEMENT;
      }
      if (bsdType === BsdType.Bsdasri) {
        return ANNEXE_BORDEREAU_SUITE;
      }
      return EN_ATTENTE_BSD_SUITE;
    case BsdStatusCode.Canceled:
      return ANNULE;

    default:
      return "unknown status";
  }

"""
