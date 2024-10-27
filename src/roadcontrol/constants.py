BSDASRI_HUMAN_WASTE_CODE = "18 01 03*"

ES_TYPE_BSDD = "Form"
ES_TYPE_BSDASRI = "Bsdasri"
ES_TYPE_BSFF = "Bsff"
ES_TYPE_BSDA = "Bsda"
ES_TYPE_BSVHU = "Bsvhu"
ES_TYPE_BSPAOH = "Bspaoh"

TYPE_BSDD = "BSDD"
TYPE_BSDASRI = "BSDASRI"
TYPE_BSFF = "BSFF"
TYPE_BSDA = "BSDA"
TYPE_BSVHU = "BSVHU"
TYPE_BSPAOH = "BSPAOH"


class BsdStatus:
    ACCEPTED = "ACCEPTED"
    # BSD en attente de regroupement
    AWAITING_GROUP = "AWAITING_GROUP"
    AWAITING_CHILD = "AWAITING_CHILD"
    # Bordereau annulé. L'annulation peut être demandée via le processus de révision
    CANCELED = "CANCELED"
    # BSD à l'état de brouillon
    # Des champs obligatoires peuvent manquer
    DRAFT = "DRAFT"
    # BSD dont les déchets ont été traités en dehors de France sans rupture de traçabilité
    FOLLOWED_WITH_PNTTD = "FOLLOWED_WITH_PNTTD"
    # Regroupement effectué
    GROUPED = "GROUPED"
    # Perte de traçabalité
    NO_TRACEABILITY = "NO_TRACEABILITY"
    # BSD dont les déchets ont été traités
    PROCESSED = "PROCESSED"
    # BSD reçu par l'établissement de destination
    RECEIVED = "RECEIVED"
    # Déchet refusé
    REFUSED = "REFUSED"
    # Déchet avec les cadres 14-19 complétées (si besoin), prêt à partir du site d'entreposage ou reconditionnement
    RESEALED = "RESEALED"
    # Déchet envoyé du site d'entreposage ou reconditionnement vers sa destination de traitement
    RESENT = "RESENT"
    # BSD finalisé
    # Les champs sont validés pour détecter des valeurs manquantes ou erronnées
    SEALED = "SEALED"
    # BSD envoyé vers l'établissement de destination
    SENT = "SENT"
    # BSD signé par l'émetteur du bordereau
    SIGNED_BY_PRODUCER = "SIGNED_BY_PRODUCER"
    # BSD signé par l'entreposage provisoire pour enlèvement
    SIGNED_BY_TEMP_STORER = "SIGNED_BY_TEMP_STORER"
    # Déchet arrivé sur le site d'entreposage ou reconditionnement
    TEMP_STORED = "TEMP_STORED"
    # Déchet accepté par le site d'entreposage ou reconditionnement
    TEMP_STORER_ACCEPTED = "TEMP_STORER_ACCEPTED"
    #  Une partie des contenants a été refusée, l'autre partie acceptée. Les contenants acceptés n'ont pas encore été traités.
    PARTIALLY_REFUSED = "PARTIALLY_REFUSED"

    INTERMEDIATELY_PROCESSED = "INTERMEDIATELY_PROCESSED"
    # Signé par l'entreprise de travaux
    SIGNED_BY_WORKER = "SIGNED_BY_WORKER"
