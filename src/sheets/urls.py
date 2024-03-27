from django.conf import settings
from django.urls import path

from .views import (
    ComputingView,
    FragmentResultView,
    Prepare,
    PrepareSheetPdf,
    RegistryView,
    RenderingView,
    Sheet,
    SheetPdf,
    SheetPdfHtml,
)

urlpatterns = [
    path("prepare/", Prepare.as_view(), name="prepare"),
    path("registry/", RegistryView.as_view(), name="registry"),
    path(
        "compute/<str:task_id>/<uuid:compute_pk>/",
        ComputingView.as_view(),
        name="pollable_result",
    ),
    path(
        "render/<str:task_id>/<uuid:compute_pk>/",
        RenderingView.as_view(),
        name="pollable_result_pdf",
    ),
    path(
        "compute-fragment/<str:task_id>/<uuid:compute_pk>/",
        FragmentResultView.as_view(),
        name="pollable_result_fragment",
    ),
    path("sheet/<uuid:pk>", Sheet.as_view(), name="sheet"),
    path("prepare-pdf/<uuid:pk>", PrepareSheetPdf.as_view(), name="prepare_pdf"),
    path("pdf/<uuid:pk>", SheetPdf.as_view(), name="sheet_pdf"),
]
if settings.DEBUG:
    urlpatterns += [
        path("pdf-debug/<uuid:pk>", SheetPdfHtml.as_view(), name="sheet_pdf_debug"),
    ]
