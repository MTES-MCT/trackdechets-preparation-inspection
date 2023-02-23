from django.conf import settings
from django.urls import path

from .views import (
    FragmentResultView,
    Prepare,
    ResultView,
    Sheet,
    SheetPdf,
    SheetPdfHtml,
)

urlpatterns = [
    path("prepare/", Prepare.as_view(), name="prepare"),
    path("sheet/<uuid:pk>", Sheet.as_view(), name="sheet"),
    path("pdf/<uuid:pk>", SheetPdf.as_view(), name="sheet_pdf"),
    path(
        "compute/<str:task_id>/<uuid:compute_pk>/",
        ResultView.as_view(),
        name="pollable_result",
    ),
    path(
        "compute-fragment/<str:task_id>/<uuid:compute_pk>/",
        FragmentResultView.as_view(),
        name="pollable_result_fragment",
    ),
]

if settings.DEBUG:
    urlpatterns += [
        path("pdf-debug/<uuid:pk>", SheetPdfHtml.as_view(), name="sheet_pdf_debug"),
    ]
