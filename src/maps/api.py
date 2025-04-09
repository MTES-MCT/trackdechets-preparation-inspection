import csv
import io

import pandas as pd
from django.contrib.gis.geos import Point
from django.db.models import Count
from django.http import FileResponse, HttpResponse
from django.utils import timezone
from django_filters import rest_framework as filters
from rest_framework.authentication import SessionAuthentication
from rest_framework.generics import ListAPIView
from rest_framework.response import Response
from rest_framework.views import APIView

from .centroids import DEPARTMENTS_CENTROIDS, REGIONS_CENTROIDS
from .filters import CartoCompanyFilter
from .models import CartoCompany
from .permissions import UserIsVerifedPermission
from .serializers import (
    CompanyExportSerializer,
    CompanySerializer,
    DepartmentCompanySerializer,
    RegionCompanySerializer,
)

empty_response_data = {"companies": [], "clusters": [], "total_count": 0}

available_departments_code = DEPARTMENTS_CENTROIDS.keys()
available_regions_code = REGIONS_CENTROIDS.keys()

MAX_EXPORT_ROWS = 1500


class ApiObjects(ListAPIView):
    filter_backends = [filters.DjangoFilterBackend]
    filterset_class = CartoCompanyFilter
    authentication_classes = [SessionAuthentication]
    permission_classes = [UserIsVerifedPermission]
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


class ApiCompanyExport(APIView):
    """
    API endpoint to export filtered companies data as CSV or Excel

    Query parameters:
    - format: 'csv' or 'xlsx' (default: 'csv')
    - any company filter parameters (see CartoCompanyFilter class)

    """

    authentication_classes = [SessionAuthentication]
    permission_classes = [UserIsVerifedPermission]

    def post(self, request, *args, **kwargs):
        return self._process_export_request(request)

    def _process_export_request(self, request):
        # Apply the same filtering as in the existing API
        queryset = CartoCompany.objects.exclude(coords__isnull=True)
        filterset = CartoCompanyFilter(request.query_params, queryset)

        filtered_companies = filterset.qs
        if len(filtered_companies) > MAX_EXPORT_ROWS:
            return Response(
                {
                    "error": "Too many results",
                    "detail": f"Export limité à {MAX_EXPORT_ROWS} établissments.",
                },
                status=400,
            )

        serializer = CompanyExportSerializer(filtered_companies, many=True)
        data = serializer.data
        # Determine the export format (default to XLSX)
        export_format = request.query_params.get("export_format", "xlsx")

        if export_format == "xlsx":
            return self._export_excel(data)
        else:  # default to CSV
            return self._export_csv(data)

    def get_filename(self):
        dt = timezone.now()
        return f"export-{dt.strftime('%Y-%m-%d_%H%M%S')}"

    def _export_csv(self, data):
        response = HttpResponse(content_type="text/csv")
        filename = self.get_filename()
        response["Content-Disposition"] = f'attachment; filename="{filename}.csv"'

        if not data:
            # Handle empty data case
            response.write("")
            return response

        fieldnames = data[0].keys()

        writer = csv.DictWriter(response, fieldnames=fieldnames)
        writer.writeheader()

        for row in data:
            writer.writerow(row)

        return response

    def _export_excel(self, data):
        filename = self.get_filename()
        output = io.BytesIO()

        df = pd.DataFrame(data if data else [])
        with pd.ExcelWriter(output, engine="openpyxl") as writer:
            df.to_excel(writer, sheet_name="Companies", index=False)

        # Set up the response
        output.seek(0)
        response = FileResponse(
            output, content_type="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
        )
        response["Content-Disposition"] = f'attachment; filename="{filename}.xlsx"'

        return response
