from django.urls import path

from .views import ExportDownload, ExportList

urlpatterns = [
    path("", ExportList.as_view(), name="data_export_list"),
    path("download/<uuid:pk>", ExportDownload.as_view(), name="data_export_download"),
]
