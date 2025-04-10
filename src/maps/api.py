from django.contrib.gis.geos import Point
from django.db.models import Count
from django_filters import rest_framework as filters
from rest_framework.authentication import SessionAuthentication
from rest_framework.generics import ListAPIView
from rest_framework.response import Response

from .centroids import DEPARTMENTS_CENTROIDS, REGIONS_CENTROIDS
from .filters import CartoCompanyFilter
from .models import CartoCompany
from .permissions import UserIsVerifedPermission
from .serializers import CompanySerializer, DepartmentCompanySerializer, RegionCompanySerializer


class BaseApiCompanies(ListAPIView):
    authentication_classes = [SessionAuthentication]
    permission_classes = [UserIsVerifedPermission]


empty_response_data = {"companies": [], "clusters": [], "total_count": 0}

available_departments_code = DEPARTMENTS_CENTROIDS.keys()
available_regions_code = REGIONS_CENTROIDS.keys()


class ApiObjects(BaseApiCompanies):
    filter_backends = [filters.DjangoFilterBackend]
    filterset_class = CartoCompanyFilter
    serializer_class = None

    def get_total_count(self, queryset):
        """
        Count total companies matching filter criteria without bounds filter
        """
        # Create a copy of request.GET without the bounds parameter
        filter_params = self.request.GET.copy()
        if "bounds" in filter_params:
            filter_params.pop("bounds")

        # Apply all filters except bounds
        filterset = self.filterset_class(filter_params, CartoCompany.objects.exclude(coords__isnull=True))
        return filterset.qs.count()

    def get_queryset(self):
        DIAGONAL_REGIONS = 10
        DIAGONAL_DEPARTMENTS = 2
        if self.diagonal >= DIAGONAL_REGIONS:
            return self.get_regions()
        if self.diagonal >= DIAGONAL_DEPARTMENTS:
            return self.get_departments()
        return CartoCompany.objects.exclude(coords__isnull=True)

    def get_regions(self):
        return (
            CartoCompany.objects.filter(code_region_insee__in=available_regions_code)
            .values("code_region_insee")
            .annotate(cnt=Count("code_region_insee"))
            .order_by()
        )

    def get_departments(self):
        return (
            CartoCompany.objects.filter(code_departement_insee__in=available_departments_code)
            .values("code_departement_insee")
            .annotate(cnt=Count("code_departement_insee"))
            .order_by()
        )

    def get_serializer(self, *args, **kwargs):
        if self.diagonal >= 10:
            return RegionCompanySerializer
        if self.diagonal >= 2:
            return DepartmentCompanySerializer
        return CompanySerializer

    def list(self, request, *args, **kwargs):
        bounds = self.request.GET.get("bounds")
        if not bounds:
            return Response(empty_response_data)

        bbox = [float(v) for v in bounds.split(",")]
        p1 = Point(bbox[0], bbox[1], srid=4326)
        p2 = Point(bbox[2], bbox[3], srid=4326)
        self.diagonal = p1.distance(p2)
        queryset = self.get_queryset()
        filtered_queryset = self.filter_queryset(queryset)

        total_count = self.get_total_count(queryset)

        serializer = self.get_serializer()

        if self.diagonal >= 2:
            clusters = serializer(filtered_queryset, many=True).data
            response_data = {
                "companies": [],
                "clusters": clusters,  # Empty clusters when showing individual companies
                "total_count": total_count,
            }
            return Response(response_data)

        companies = serializer(filtered_queryset, many=True).data
        response_data = {
            "companies": companies,
            "clusters": [],  # Empty clusters when showing individual companies
            "total_count": total_count,
        }
        return Response(response_data)
