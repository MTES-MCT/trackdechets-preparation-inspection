from django.urls import path

from .views import (
    BsdRecentPdfs,
    BsdSearch,
    BsdSearchResult,
    BundleProcessingView,
    FragmentBundleProcessingView,
    RoadControlPdf,
    RoadControlPdfBundle,
    RoadControlPdfBundleResult,
    RoadControlRecentPdfs,
    RoadControlSearch,
    RoadControlSearchResult,
)

urlpatterns = [
    path("", RoadControlSearch.as_view(), name="roadcontrol"),
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
    path("recent-road-control-pdfs/", RoadControlRecentPdfs.as_view(), name="roadcontrol_recent_pdfs"),
    path("recent-bsd-pdfs/", BsdRecentPdfs.as_view(), name="bsd_recent_pdfs"),
    path("bsd-search/", BsdSearch.as_view(), name="roadcontrol_bsd_search"),
    path("bsd-search-result/", BsdSearchResult.as_view(), name="roadcontrol_bsd_search_result"),
]
