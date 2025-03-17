from django.contrib import admin
from django.db.models import Q

from .models import CartoCompany


class ProfilsFilter(admin.SimpleListFilter):
    title = "profils"
    parameter_name = "profil"

    def lookups(self, request, model_admin):
        return [
            ("PRODUCER", "Producteur"),
            ("COLLECTOR", "Collecteur"),
            ("TRANSPORTER", "Transporteur"),
            ("TRADER", "Négociant"),
            ("BROKER", "Courtier"),
            ("WASTEPROCESSOR", "Installation de traitement"),
            ("ECO_ORGANISME", "Éco-organisme"),
        ]

    def queryset(self, request, queryset):
        if self.value():
            return queryset.filter(profils__contains=[self.value()])
        return queryset


PROCESSING_CODES = [
    ("R1", "R1 - Utilisation principale comme combustible"),
    ("R2", "R2 - Récupération des solvants"),
    ("R3", "R3 - Recyclage des substances organiques"),
    ("R4", "R4 - Recyclage des métaux"),
    ("R5", "R5 - Recyclage matières inorganiques"),
    ("R6", "R6 - Régénération des acides ou des bases"),
    ("R7", "R7 - Récupération des produits captant polluants"),
    ("R8", "R8 - Récupération des produits des catalyseurs"),
    ("R9", "R9 - Régénération des huiles"),
    ("R10", "R10 - Épandage au profit de l'agriculture"),
    ("R11", "R11 - Utilisation de déchets résiduels"),
    ("R12", "R12 - Échange de déchets"),
    ("R13", "R13 - Stockage préalable aux opérations R1-R12"),
    ("D1", "D1 - Dépôt sur ou dans le sol"),
    ("D2", "D2 - Traitement en milieu terrestre"),
    ("D3", "D3 - Injection en profondeur"),
    ("D4", "D4 - Lagunage"),
    ("D5", "D5 - Mise en décharge aménagée"),
    ("D6", "D6 - Rejet dans le milieu aquatique"),
    ("D7", "D7 - Immersion"),
    ("D8", "D8 - Traitement biologique"),
    ("D9", "D9 - Traitement physico-chimique"),
    ("D9F", "D9F - Traitement physico-chimique"),
    ("D10", "D10 - Incinération à terre"),
    ("D12", "D12 - Stockage permanent"),
    ("D13", "D13 - Regroupement préalable"),
    ("D14", "D14 - Reconditionnement préalable"),
    ("D15", "D15 - Stockage préalable aux opérations D1-D14"),
]


class ProcessingOperationsFilter(admin.SimpleListFilter):
    title = "opérations de traitement"
    parameter_name = "operation"

    def lookups(self, request, model_admin):
        return PROCESSING_CODES

    def queryset(self, request, queryset):
        if self.value():
            return queryset.filter(
                Q(processing_operations_bsdd__contains=[self.value()])
                | Q(processing_operations_bsda__contains=[self.value()])
                | Q(processing_operations_bsff__contains=[self.value()])
                | Q(processing_operations_bsdasri__contains=[self.value()])
                | Q(processing_operations_bsvhu__contains=[self.value()])
                | Q(processing_operation_dnd__contains=[self.value()])
                | Q(processing_operation_texs__contains=[self.value()])
            )
        return queryset


class BsdTypeFilter(admin.SimpleListFilter):
    title = "Type de bordereau"
    parameter_name = "bsd_type"

    def lookups(self, request, model_admin):
        return [
            ("bsdd", "BSDD - Déchets dangereux"),
            ("bsda", "BSDA - Amiante"),
            ("bsff", "BSFF - Fluides frigorigènes"),
            ("bsvhu", "BSVHU - Véhicules hors d'usage"),
            ("bsdasri", "BSDASRI - Déchets d'activités de soins"),
            ("bsdnd", "BSDND - Déchets non dangereux"),
            ("dnd", "DND - Déclarations"),
            ("texs", "TEXS - Terres excavées"),
            ("texs_dd", "TEXS DD - Terres excavées dangereuses"),
        ]

    def queryset(self, request, queryset):
        if self.value():
            return queryset.filter(**{self.value(): True})
        return queryset


class RoleFilter(admin.SimpleListFilter):
    title = "Rôle"
    parameter_name = "role"

    def lookups(self, request, model_admin):
        return [
            ("emitter", "Producteur"),
            ("transporter", "Transporteur"),
            ("destination", "Destination"),
            ("worker", "Entreprise de travaux"),
        ]

    def queryset(self, request, queryset):
        bsd_type = self.used_parameters.get("bsd_type", None)

        if not self.value():
            return queryset

        if bsd_type and self.value():
            field_name = f"{bsd_type}_{self.value()}"
            # Check if the field exists in the model
            if field_name in [f.name for f in CartoCompany._meta.get_fields()]:
                return queryset.filter(**{field_name: True})

        # If no document type is selected or the field doesn't exist, use a generic role filtering
        if self.value() == "emitter":
            return queryset.filter(
                Q(bsdd_emitter=True)
                | Q(bsda_emitter=True)
                | Q(bsff_emitter=True)
                | Q(bsvhu_emitter=True)
                | Q(bsdasri_emitter=True)
                | Q(bsdnd_emitter=True)
                | Q(dnd_emitter=True)
                | Q(texs_emitter=True)
                | Q(texs_dd_emitter=True)
            )
        elif self.value() == "transporter":
            return queryset.filter(
                Q(bsdd_transporter=True)
                | Q(bsda_transporter=True)
                | Q(bsff_transporter=True)
                | Q(bsvhu_transporter=True)
                | Q(bsdasri_transporter=True)
                | Q(bsdnd_transporter=True)
                | Q(texs_dd_transporter=True)
            )
        elif self.value() == "destination":
            return queryset.filter(
                Q(bsdd_destination=True)
                | Q(bsda_destination=True)
                | Q(bsff_destination=True)
                | Q(bsvhu_destination=True)
                | Q(bsdasri_destination=True)
                | Q(bsdnd_destination=True)
                | Q(dnd_destination=True)
                | Q(texs_destination=True)
                | Q(texs_dd_destination=True)
            )
        elif self.value() == "worker":
            return queryset.filter(bsda_worker=True)
        return queryset


@admin.register(CartoCompany)
class CartoCompanyAdmin(admin.ModelAdmin):
    list_display = (
        "siret",
        "nom_etablissement",
        "code_departement_insee",
        "has_bsdd",
        "has_bsda",
        "has_bsff",
        "has_bsvhu",
        "has_bsdasri",
        "is_emitter",
        "is_transporter",
        "is_destination",
        "is_worker",
        "waste_codes_bordereaux",
    )

    search_fields = (
        "siret",
        "nom_etablissement",
        "adresse_td",
        "adresse_insee",
    )

    list_filter = (
        "code_departement_insee",
        "code_region_insee",
        BsdTypeFilter,
        RoleFilter,
        ProfilsFilter,
        ProcessingOperationsFilter,
    )

    # Method to create virtual fields for display
    def has_bsdd(self, obj):
        return bool(obj.bsdd)

    has_bsdd.short_description = "BSDD"
    has_bsdd.boolean = True

    def has_bsda(self, obj):
        return bool(obj.bsda)

    has_bsda.short_description = "BSDA"
    has_bsda.boolean = True

    def has_bsff(self, obj):
        return bool(obj.bsff)

    has_bsff.short_description = "BSFF"
    has_bsff.boolean = True

    def has_bsvhu(self, obj):
        return bool(obj.bsvhu)

    has_bsvhu.short_description = "BSVHU"
    has_bsvhu.boolean = True

    def has_bsdasri(self, obj):
        return bool(obj.bsdasri)

    has_bsdasri.short_description = "BSDASRI"
    has_bsdasri.boolean = True

    def is_emitter(self, obj):
        return any(
            [
                obj.bsdd_emitter,
                obj.bsda_emitter,
                obj.bsff_emitter,
                obj.bsvhu_emitter,
                obj.bsdasri_emitter,
                obj.bsdnd_emitter,
                obj.dnd_emitter,
                obj.texs_emitter,
                obj.texs_dd_emitter,
            ]
        )

    is_emitter.short_description = "Producteur"
    is_emitter.boolean = True

    def is_transporter(self, obj):
        return any(
            [
                obj.bsdd_transporter,
                obj.bsda_transporter,
                obj.bsff_transporter,
                obj.bsvhu_transporter,
                obj.bsdasri_transporter,
                obj.bsdnd_transporter,
                obj.texs_dd_transporter,
            ]
        )

    is_transporter.short_description = "Transporteur"
    is_transporter.boolean = True

    def is_destination(self, obj):
        return any(
            [
                obj.bsdd_destination,
                obj.bsda_destination,
                obj.bsff_destination,
                obj.bsvhu_destination,
                obj.bsdasri_destination,
                obj.bsdnd_destination,
                obj.dnd_destination,
                obj.texs_destination,
                obj.texs_dd_destination,
            ]
        )

    is_destination.short_description = "Destination"
    is_destination.boolean = True

    def is_worker(self, obj):
        return obj.bsda_worker

    is_worker.short_description = "Entreprise de travaux"
    is_worker.boolean = True

    def get_search_results(self, request, queryset, search_term):
        queryset, use_distinct = super().get_search_results(request, queryset, search_term)

        # Advanced filtering is now handled by the RoleFilter that works in conjunction with BsdTypeFilter

        return queryset, use_distinct

    actions = ["filter_by_role_combination"]

    def filter_by_role_combination(self, request, queryset):
        bsd_type = request.POST.get("bsd_type")
        role = request.POST.get("role")

        if not bsd_type or not role:
            return queryset

        field_name = f"{bsd_type}_{role}"

        # Check if the field exists in the model
        if field_name in [f.name for f in CartoCompany._meta.get_fields()]:
            filtered = queryset.filter(**{field_name: True})
            self.message_user(
                request, f"{filtered.count()} établissements trouvés avec le rôle {role} pour {bsd_type.upper()}"
            )
            return filtered
        else:
            self.message_user(request, f"Combinaison invalide: {bsd_type} - {role}", level="ERROR")
            return queryset

    filter_by_role_combination.short_description = "Filtrer par combinaison type/rôle"

    # Optimize queries with prefetch_related for array fields
    def get_queryset(self, request):
        queryset = super().get_queryset(request)
        return queryset.defer("waste_codes_bordereaux", "waste_codes_processed")
