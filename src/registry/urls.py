from django.urls import path

from .views import RegistryPrepare, RegistryView

urlpatterns = [
    path("registry-prepare/", RegistryPrepare.as_view(), name="registry_prepare"),
    path("registry/", RegistryView.as_view(), name="registry"),
]
