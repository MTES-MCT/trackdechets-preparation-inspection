from functools import reduce
from operator import ior

from django.contrib.gis.geos import Point, Polygon
from django.db.models import Q
from django_filters import rest_framework as filters

from .models import CartoCompany


# http://127.0.0.1:8000/map/api/companies/regions?departments=75%2C77%2C78%2C91%2C92%2C93%2C94%2C95&operation_codes=R2&bounds=-7.972541367309162%2C43.99753838987371%2C16.395134413941264%2C47.84706463451829
class BaseCartoCompanyFilter(filters.FilterSet):
    departments = filters.CharFilter(method="filter_departments")
    profils = filters.CharFilter(method="filter_profils")
    profils_collecteur = filters.CharFilter(method="filter_profils_collecteur")
    profils_installation = filters.CharFilter(method="filter_profils_installation")
    bsds = filters.CharFilter(method="filter_bsds")
    bsds_roles = filters.CharFilter(method="filter_bsds_roles")
    operation_codes = filters.CharFilter(method="filter_operation_codes")
    waste_codes = filters.CharFilter(method="filter_waste_codes")

    def __init__(self, data=None, queryset=None, *, request=None, prefix=None):
        super().__init__(data, queryset, request=request, prefix=prefix)
        self.role_types = {
            "bsdd": ["emitter", "transporter", "destination"],
            "bsdnd": ["emitter", "transporter", "destination"],
            "bsda": ["emitter", "transporter", "destination"],
            "bsff": ["emitter", "transporter", "destination"],
            "bsdasri": ["emitter", "transporter", "destination"],
            "bsvhu": ["emitter", "transporter", "destination"],
            "texs_dd": ["emitter", "transporter", "destination"],
            "dnd": ["emitter", "destination"],
            "texs": ["emitter", "destination"],
        }

        self.role_specific_fields = []
        for waste_type, roles in self.role_types.items():
            for role in roles:
                field_name = f"{waste_type}_{role}"
                self.role_specific_fields.append(field_name)

    def filter_departments(self, queryset, _, value):
        return queryset.filter(code_departement_insee__in=value.split(","))

    def filter_profils(self, queryset, _, value):
        return queryset.filter(profils__contains=value.split(","))

    def filter_profils_collecteur(self, queryset, _, value):
        return queryset.filter(profils_collecteur__contains=value.split(","))

    def filter_profils_installation(self, queryset, name, value):
        return queryset.filter(profils_installation__contains=value.split(","))

    def filter_waste_codes(self, queryset, name, value):
        # queryterms = [Q(waste_codes_bordereaux__contains=waste_code) for waste_code in value.split(",")]
        # params = reduce(ior, queryterms)
        #

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
        # to avoid expensive api requests tha could exhaust our db, we compute the bbox diagonal and return
        # an empty queryset if it exceeds  `max_bbox_diagonal`
        p1 = Point(bbox[0], bbox[1], srid=4326)
        p2 = Point(bbox[2], bbox[3], srid=4326)
        dist = p1.distance(p2)

        if dist > self.max_bbox_diagonal:
            return CartoCompany.objects.none()

        bbox_polygon = Polygon.from_bbox(bbox)

        return queryset.filter(coords__within=bbox_polygon)

    def filter_bsds_roles(self, queryset, name, value):
        # Role types to check for each base type

        requested_roles = value.split(",")
        queryterms = []
        for requested_role in requested_roles:
            if requested_role in self.role_specific_fields:
                queryterms.append(Q(**{requested_role: True}))

            # elif "_" in role_request:
            #     parts = role_request.split("_")

            # Pattern: [waste_type]_all or [waste_type]_all_roles
            # if len(parts) >= 2 and parts[0] in self.role_types and parts[1] in ["all", "all_roles"]:
            #     base_type = parts[0]
            #     for role in self.role_types[base_type]:
            #         field_name = f"{base_type}_{role}"
            #         if field_name in self.role_specific_fields:
            #             queryterms.append(Q(**{field_name: True}))

            # Pattern: all_[role] (e.g., all_emitter)
            # if len(parts) >= 2 and parts[0] == "all" and parts[1] in ["emitter", "transporter", "destination"]:
            #     role_type = parts[1]
            #     for base_type, roles in self.role_types.items():
            #         if role_type in roles:
            #             field_name = f"{base_type}_{role_type}"
            #             if field_name in self.role_specific_fields:
            #                 queryterms.append(Q(**{field_name: True}))

        if not queryterms:
            return queryset

        # Combine the queries with OR
        params = reduce(ior, queryterms)

        print(params)
        return queryset.filter(params)

    class Meta:
        model = CartoCompany
        fields = [
            # Base waste types
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
        ]


class RegionCartoCompanyFilter(BaseCartoCompanyFilter):
    max_bbox_diagonal = 500


class DepartmentCartoCompanyFilter(BaseCartoCompanyFilter):
    max_bbox_diagonal = 7


class BasDetailCartoCompanyFilter(BaseCartoCompanyFilter):
    bounds = filters.CharFilter(method="filter_bounds", required=True)

    # class Meta(BaseCartoCompanyFilter.Meta):
    #     fields = ["bsdd", "bsda", "bsff", "bsdasri", "bsvhu", "bsds", "profils", "bounds"]
    #


class ClusterCartoCompanyFilter(BasDetailCartoCompanyFilter):
    max_bbox_diagonal = 2


class DetailCartoCompanyFilter(BasDetailCartoCompanyFilter):
    max_bbox_diagonal = 10
