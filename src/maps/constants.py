ROLES_TYPES = {
    "bsdd": ["emitter", "transporter", "destination"],
    "bsdnd": ["emitter", "transporter", "destination"],
    "bsda": ["emitter", "transporter", "destination", "worker"],
    "bsff": ["emitter", "transporter", "destination"],
    "bsdasri": ["emitter", "transporter", "destination"],
    "bsvhu": ["emitter", "transporter", "destination"],
    "texs_dd": ["emitter", "transporter", "destination"],
    "dnd": ["emitter", "destination"],
    "texs": ["emitter", "destination"],
    "ssd": [],
}


WASTE_NAMES = [
    "Déchets dangereux",
    "Amiante",
    "Fluides Frigorigènes",
    "Dasri",
    "Vehicules hors d'usage",
    "Sortie de statut de déchet",
    "Déchets non dangereux",
    "Terres et sédiments - DD",
    "Terres et sédiments - DND",
]

PROCESSING_OPERATIONS_FIELDS = [
    "processing_operations_bsdd",
    "processing_operations_bsdnd",
    "processing_operations_bsda",
    "processing_operations_bsff",
    "processing_operations_bsdasri",
    "processing_operations_bsvhu",
    "processing_operation_dnd",
    "processing_operation_texs",
]


ANNUAL_ICPE_RUBRIQUES = ["2760-1", "2760-2"]  # unité t/an
DAILY_ICPE_RUBRIQUES = ["2790", "2770", "2791", "2771"]  # unité t/jour

ICPE_RUBRIQUES = ANNUAL_ICPE_RUBRIQUES + DAILY_ICPE_RUBRIQUES
