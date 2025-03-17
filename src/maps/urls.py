from django.urls import path

from .api import ApiObjects
from .views import MapView

urlpatterns = [
    path("", MapView.as_view(), name="map_view"),
    path("api/companies/objects", ApiObjects.as_view(), name="map_api_objects"),
]
