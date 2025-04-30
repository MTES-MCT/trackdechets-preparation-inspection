from django.urls import path

from .views import RegistryV2ListContent, RegistryV2ListWrapper, RegistryV2Prepare, RegistryV2Retrieve

urlpatterns = [
    path("registry-v2-prepare/", RegistryV2Prepare.as_view(), name="registry_v2_prepare"),
    path("registry-v2-list/", RegistryV2ListWrapper.as_view(), name="registry_v2_list"),
    path("registry-v2-list-content/", RegistryV2ListContent.as_view(), name="registry_v2_list_content"),
    path("registry-v2-retrieve/<uuid:registry_pk>", RegistryV2Retrieve.as_view(), name="registry_v2_retrieve"),
]
