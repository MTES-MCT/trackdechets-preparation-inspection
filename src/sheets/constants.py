COMPANY_TYPES = {
    "COLLECTOR": "Tri Transit Regroupement (TTR)",
    "WASTEPROCESSOR": "Usine de traitement",
    "WASTE_CENTER": "Déchetterie",
    "BROKER": "Courtier",
    "TRADER": "Négociant",
    "TRANSPORTER": "Transporteur",
    "ECO_ORGANISM": "Éco-organisme",
    "ECO_ORGANISME": "Éco-organisme",
    "PRODUCER": "Producteur",
    "WASTE_VEHICLES": "Centre Véhicules Hors d'Usage",
    "CREMATORIUM": "Crématorium",
}

BSDD = "bsdd"
BSDD_NON_DANGEROUS = "bsdd_non_dangerous"
BSDA = "bsda"
BSDASRI = "bsdasri"
BSFF = "bsff"
BSVHU = "bsvhu"


PLOTLY_GRAPHS_TO_RENDER_IN_PDF = [
    "bsdd_created_rectified",
    "bsdd_stock",
    "bsdd_non_dangerous_created_rectified",
    "bsdd_non_dangerous_stock",
    "bsda_created_rectified",
    "bsda_stock",
    "bsdasri_created_rectified",
    "bsdasri_stock",
    "bsff_created_rectified",
    "bsff_stock",
    "bsvhu_created_rectified",
    "bsvhu_stock",
    "waste_origin",
    "waste_origin_map",
    "icpe_2770",
    "icpe_2790",
    "icpe_2760",
    "bsda_worker_quantity",
    "transporter_bordereaux_stats_graph",
    "quantities_transported_stats_graph",
    "non_dangerous_waste_statements_graph",
    "non_dangerous_waste_quantities_graph",
]


REGISTRY_TYPE_ALL = "ALL"
REGISTRY_TYPE_INCOMING = "INCOMING"
REGISTRY_TYPE_OUTGOING = "OUTGOING"
REGISTRY_TYPE_TRANSPORTED = "TRANSPORTED"
REGISTRY_FORMAT_CSV = "csv"
REGISTRY_FORMAT_XLS = "xls"
