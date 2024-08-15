from django.urls import path

from .views import (
    BundleProcessingView,
    FragmentBundleProcessingView,
    RoadControl,
    RoadControlPdf,
    RoadControlPdfBundle,
    RoadControlPdfBundleResult,
    RoadControlRecentsPdfs,
    RoadControlSearchResult,
)

urlpatterns = [
    path("", RoadControl.as_view(), name="roadcontrol"),
    path("search-result/", RoadControlSearchResult.as_view(), name="roadcontrol_search_result"),
    path("pdf/", RoadControlPdf.as_view(), name="roadcontrol_pdf"),
    path("pdf-bundle-process/", RoadControlPdfBundle.as_view(), name="roadcontrol_pdf_bundle"),
    path(
        "pdf-bundle-processing/<str:task_id>/<uuid:bundle_pk>/",
        BundleProcessingView.as_view(),
        name="roadcontrol_pdf_bundle_processing",
    ),
    path(
        "pdf-bundle-processing-fragment/<str:task_id>/<uuid:bundle_pk>/",
        FragmentBundleProcessingView.as_view(),
        name="pdf_bundle_processing_fragment",
    ),
    path("pdf-bundle-result/<str:pk>/", RoadControlPdfBundleResult.as_view(), name="roadcontrol_pdf_bundle_result"),
    path("recent-pdfs/", RoadControlRecentsPdfs.as_view(), name="roadcontrol_recent_pdfs"),
]
