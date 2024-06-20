import base64
import datetime as dt

from celery import chain
from django.http import HttpResponse
from django.utils import timezone
from rest_framework import permissions, status
from rest_framework.generics import CreateAPIView, RetrieveAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from sheets.models import ComputedInspectionData

from .serializers import ComputedInspectionDataCreateSerializer, ComputedInspectionDataSerializer
from .task import prepare_sheet_api, send_webhook


class IsApiUserPermission(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user.is_api


class ApiOnlyUserMixin:
    """Restrict api call to `api` users"""

    permission_classes = [IsAuthenticated, IsApiUserPermission]


class ApiSheetCreate(ApiOnlyUserMixin, CreateAPIView):
    """Create a sheet and db and launch process and webhook calls"""

    queryset = ComputedInspectionData.objects.all()
    serializer_class = ComputedInspectionDataCreateSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        inspection = self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        serialized = ComputedInspectionDataSerializer(inspection).data
        return Response(serialized, status=status.HTTP_201_CREATED, headers=headers)

    def perform_create(self, serializer):
        org_id = serializer.validated_data["orgId"]
        year = serializer.validated_data["year"]
        now = timezone.now()
        current_year = now.year
        if year == current_year:
            data_end_date = timezone.now()
        if year == current_year - 1:
            data_end_date = dt.datetime(year=year, month=12, day=31)

        data_start_date = dt.datetime(year=year, month=1, day=1)

        # check if already generated
        existing = ComputedInspectionData.objects.filter(
            org_id=org_id,
            data_start_date=data_start_date,
            data_end_date=data_end_date,
            created__date=now.date(),
            state=ComputedInspectionData.StateChoice.GRAPH_RENDERED,
            creation_mode=ComputedInspectionData.CreationModeChoice.API,
        ).first()
        if existing:
            return existing

        inspection = ComputedInspectionData.objects.create(
            org_id=org_id,
            data_start_date=data_start_date,
            data_end_date=data_end_date,
            created_by=self.request.user,
            creation_mode=ComputedInspectionData.CreationModeChoice.API,
        )

        chain(prepare_sheet_api.s(inspection.pk), send_webhook.s()).apply_async()
        return inspection


class ApilSheetDetail(ApiOnlyUserMixin, RetrieveAPIView):
    """Retrieve sheet detail"""

    queryset = ComputedInspectionData.objects.by_api()
    serializer_class = ComputedInspectionDataSerializer


class ApiSheetPdfRetrieve(ApiOnlyUserMixin, RetrieveAPIView):
    """Download a pdf through api"""

    queryset = ComputedInspectionData.objects.by_api().filter(state=ComputedInspectionData.StateChoice.GRAPH_RENDERED)

    def retrieve(self, request, *args, **kwargs):
        sheet = self.get_object()

        decoded = base64.b64decode(sheet.pdf)
        response = HttpResponse(content_type="application/pdf")
        response["Content-Disposition"] = f'attachment; filename="{sheet.pdf_filename}.pdf"'
        response.write(decoded)
        return response
