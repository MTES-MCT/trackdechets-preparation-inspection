from functools import reduce
from operator import ior

from django.contrib.gis.geos import Point, Polygon
from django.db.models import Q
from django_filters import rest_framework as filters

from .models import CartoCompany


def prepare_role_specific_fields():
    role_types = {
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

    role_specific_fields = []
    for waste_type, roles in role_types.items():
        for role in roles:
            field_name = f"{waste_type}_{role}"
            role_specific_fields.append(field_name)
        role_specific_fields.append(waste_type)
    return role_specific_fields


ROLE_SPECIFIC_FIELDS = prepare_role_specific_fields()


class CartoCompanyFilter(filters.FilterSet):
    departments = filters.CharFilter(method="filter_departments")
    profils = filters.CharFilter(method="filter_profils")
    profils_collecteur = filters.CharFilter(method="filter_profils_collecteur")
    profils_installation = filters.CharFilter(method="filter_profils_installation")
    bsds = filters.CharFilter(method="filter_bsds")
    bsds_roles = filters.CharFilter(method="filter_bsds_roles")
    operation_codes = filters.CharFilter(method="filter_operation_codes")
    waste_codes = filters.CharFilter(method="filter_waste_codes")
    bounds = filters.CharFilter(method="filter_bounds", required=True)

    def filter_departments(self, queryset, _, value):
        return queryset.filter(code_departement_insee__in=value.split(","))

    def filter_profils(self, queryset, _, value):
        return queryset.filter(profils__contains=value.split(","))

    def filter_profils_collecteur(self, queryset, _, value):
        return queryset.filter(profils_collecteur__contains=value.split(","))

    def filter_profils_installation(self, queryset, name, value):
        return queryset.filter(profils_installation__contains=value.split(","))

    def filter_waste_codes(self, queryset, name, value):
        return queryset.filter(waste_codes_bordereaux__overlap=value.split(","))

    def filter_operation_codes(self, queryset, name, value):
        values = value.split(",")
        fields = ["bsdd", "bsda", "bsff", "bsdasri", "bsvhu"]

        queryterms = [Q(**{f"processing_operations_{field}__overlap": values}) for field in fields]
        if not queryterms:
            return queryset
        params = reduce(ior, queryterms)

        return queryset.filter(params)

    def filter_bsds(self, queryset, name, value):
        allowed_params = ["bsdd", "bsda", "bsff", "bsdasri", "bsvhu"]
        queryterms = [Q(**{bsd: True}) for bsd in value.split(",") if bsd in allowed_params]
        if not queryterms:
            return queryset
        params = reduce(ior, queryterms)

        return queryset.filter(params)

    def filter_bounds(self, queryset, name, value):
        bbox = [float(v) for v in value.split(",")]

        p1 = Point(bbox[0], bbox[1], srid=4326)
        p2 = Point(bbox[2], bbox[3], srid=4326)
        diagonal = p1.distance(p2)
        if diagonal >= 2:  # explain
            return queryset
        #
        bbox_polygon = Polygon.from_bbox(bbox)

        return queryset.filter(coords__within=bbox_polygon)

    def filter_bsds_roles(self, queryset, name, value):
        # Role types to check for each base type

        requested_roles = value.split(",")
        queryterms = []

        for requested_role in requested_roles:
            if requested_role in ROLE_SPECIFIC_FIELDS:
                queryterms.append(Q(**{requested_role: True}))
        if not queryterms:
            return queryset

        params = reduce(ior, queryterms)

        return queryset.filter(params)

    class Meta:
        model = CartoCompany
        fields = [
            "bsdd",
            "bsdnd",
            "bsda",
            "bsff",
            "bsdasri",
            "bsvhu",
            "texs_dd",
            "dnd",
            "texs",
            "bsds",
            "bsds_roles",
            "profils",
            # BSDD roles
            "bsdd_emitter",
            "bsdd_transporter",
            "bsdd_destination",
            # BSDND roles
            "bsdnd_emitter",
            "bsdnd_transporter",
            "bsdnd_destination",
            # BSDA roles
            "bsda_emitter",
            "bsda_transporter",
            "bsda_destination",
            # BSFF roles
            "bsff_emitter",
            "bsff_transporter",
            "bsff_destination",
            # BSDASRI roles
            "bsdasri_emitter",
            "bsdasri_transporter",
            "bsdasri_destination",
            # BSVHU roles
            "bsvhu_emitter",
            "bsvhu_transporter",
            "bsvhu_destination",
            # TEXS_DD roles
            "texs_dd_emitter",
            "texs_dd_transporter",
            "texs_dd_destination",
            # DND roles
            "dnd_emitter",
            "dnd_destination",
            # TEXS roles
            "texs_emitter",
            "texs_destination",
            # ssd
            "ssd",
        ]
