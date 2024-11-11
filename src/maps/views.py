from functools import reduce
from operator import ior

from django.contrib.gis.geos import Point, Polygon
from django.db import connection
from django.db.models import Count, Q
from django.views.generic import TemplateView
from django_filters import rest_framework as filters
from rest_framework.authentication import SessionAuthentication
from rest_framework.generics import ListAPIView
from rest_framework.response import Response

from common.mixins import FullyLoggedMixin

from .centroids import DEPARTMENTS_CENTROIDS, REGIONS_CENTROIDS
from .models import CartoCompany
from .serializers import ClusterSerializer, CompanySerializer, DepartmentCompanySerializer, RegionCompanySerializer


class MapView(FullyLoggedMixin, TemplateView):
    template_name = "maps/map.html"


class CartoCompanyFilter(filters.FilterSet):
    profils = filters.CharFilter(method="filter_profils")
    bsds = filters.CharFilter(method="filter_bsds")
    operationcodes = filters.CharFilter(method="filter_operation_codes")
    bounds = filters.CharFilter(method="filter_bounds")

    def filter_profils(self, queryset, name, value):
        return queryset.filter(profils__contains=value.split(","))

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

        bbox_polygon = Polygon.from_bbox(bbox)

        return queryset.filter(coords__within=bbox_polygon)

    class Meta:
        model = CartoCompany
        fields = ["bsdd", "bsda", "bsff", "bsdasri", "bsvhu", "bsds", "profils", "bounds"]


class BaseApiCompanies(ListAPIView):
    authentication_classes = [SessionAuthentication]


class RegionApiCompanies(BaseApiCompanies):
    filter_backends = [filters.DjangoFilterBackend]
    filterset_class = CartoCompanyFilter
    serializer_class = RegionCompanySerializer

    def get_queryset(self):
        available_regions_code = REGIONS_CENTROIDS.keys()
        return (
            CartoCompany.objects.filter(code_region_insee__in=available_regions_code)
            .values("code_region_insee")
            .annotate(cnt=Count("code_region_insee"))
            .order_by()
        )


class DepartmentsApiCompanies(BaseApiCompanies):
    filter_backends = [filters.DjangoFilterBackend]
    filterset_class = CartoCompanyFilter
    serializer_class = DepartmentCompanySerializer

    def get_queryset(self):
        available_departments_code = DEPARTMENTS_CENTROIDS.keys()

        return (
            CartoCompany.objects.filter(code_departement_insee__in=available_departments_code)
            .values("code_departement_insee")
            .annotate(cnt=Count("code_departement_insee"))
            .order_by()
        )


class ApiCompanies(BaseApiCompanies):
    filter_backends = [filters.DjangoFilterBackend]
    filterset_class = CartoCompanyFilter
    serializer_class = CompanySerializer

    def get_queryset(self):
        return CartoCompany.objects.exclude(coords__isnull=True)


class ApiCLusterCompanies(BaseApiCompanies):
    serializer_class = ClusterSerializer
    filter_backends = [filters.DjangoFilterBackend]
    filterset_class = CartoCompanyFilter

    def get_queryset_kmeans(self, companies_ids):
        q = """
            WITH
            bounded_points AS (
            SELECT
            *
            FROM
            maps_cartocompany
            WHERE
             id in %s
            )
            SELECT
            cluster_id,
            COUNT(*) AS cnt,
            ST_X(ST_Centroid (ST_Collect (coords))) AS lon,
            ST_Y(ST_Centroid (ST_Collect (coords))) AS lat
            FROM
            (
            SELECT
            coords,
            ST_ClusterKMeans (coords, 10) OVER () AS cluster_id
            FROM
            bounded_points
            ) clusters
            GROUP BY
            cluster_id
            ORDER BY
            cluster_id;
        """
        with connection.cursor() as cursor:
            cursor.execute(q, [tuple(companies_ids)])
            columns = [col[0] for col in cursor.description]
            data = []
            for row in cursor.fetchall():
                data_item = dict(zip(columns, row))
                data_item["location"] = Point(
                    data_item.pop("lon"),
                    data_item.pop("lat"),
                )
                data.append(data_item)
        return data

    def get_queryset_dbscan(self, companies_ids):
        query = """
            WITH clustered_points AS (
            SELECT 
            ST_ClusterDBSCAN(coords, eps := 0.02, minpoints := 2) OVER () AS cluster_id,
            siret,
            coords
            FROM 
            maps_cartocompany
            WHERE 
            id in %s
            )
            SELECT 
            cluster_id,
            COUNT(*) AS cnt,
            ST_Centroid(ST_Collect(coords)) AS cluster_centroid,
                ST_X(ST_Centroid (ST_Collect (coords))) AS lon,
            ST_Y(ST_Centroid (ST_Collect (coords))) AS lat
            FROM 
            clustered_points
            WHERE 
            cluster_id IS NOT NULL
            GROUP BY 
            cluster_id
            ;
        """
        with connection.cursor() as cursor:
            cursor.execute(query, [tuple(companies_ids)])
            columns = [col[0] for col in cursor.description]
            data = []

            for row in cursor.fetchall():
                data_item = dict(zip(columns, row))
                data_item["location"] = Point(
                    data_item.pop("lon"),
                    data_item.pop("lat"),
                )
                data.append(data_item)
        return data

    def get_queryset(self):
        return self.get_queryset_dbscan()

    def get_base_queryset(self):
        return CartoCompany.objects.exclude(coords__isnull=True)

    def list(self, request, *args, **kwargs):
        # as we want to filter with CartoCompanyFilter, we proceed in 2 steps
        # First we retrieve companies ids in the bounding box
        companies_ids = self.filter_queryset(self.get_base_queryset()).values_list("id", flat=True)
        count = len(companies_ids)
        # Then given that clustering algorithms are costly, if we have a lot of companies, we cheat and return the
        # middle of the bounding box
        if count > 1000:  # empirical steps values
            bounds = self.request.GET.get("bounds")
            if not bounds:
                return []
            bounds = bounds.split(",")
            lon = (float(bounds[0]) + float(bounds[2])) / 2
            lat = (float(bounds[1]) + float(bounds[3])) / 2
            queryset = [{"cnt": count, "location": Point(lon, lat)}]
        # else we use kmeans or db scan
        elif count > 300:
            # kmeans is faster and cheaper
            queryset = self.get_queryset_kmeans(companies_ids)
        else:
            # dbscan provides a better geographical accuracy bus is way slower
            queryset = self.get_queryset_dbscan(companies_ids)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)
