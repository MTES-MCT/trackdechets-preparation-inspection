from django.urls import path

from .views import ApilSheetDetail, ApiSheetCreate, ApiSheetPdfRetrieve

urlpatterns = [
    path("create/", ApiSheetCreate.as_view(), name="api_sheet_create"),
    path("sheet/<uuid:pk>", ApilSheetDetail.as_view(), name="api_sheet_detail"),
    path("pdf/<uuid:pk>", ApiSheetPdfRetrieve.as_view(), name="api_sheet_pdf_retrieve"),
]
