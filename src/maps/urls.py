from django.urls import path

from .api import ApiCompanyExport, ApiObjects
from .views import MapView

urlpatterns = [
    path("", MapView.as_view(), name="map_view"),
    path("api/companies/objects", ApiObjects.as_view(), name="map_api_objects"),
    path("api/companies/export", ApiCompanyExport.as_view(), name="map_api_export"),
]
