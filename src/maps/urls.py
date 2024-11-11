from django.urls import path

from .views import ApiCLusterCompanies, ApiCompanies, DepartmentsApiCompanies, MapView, RegionApiCompanies

urlpatterns = [
    path("", MapView.as_view(), name="map_view"),
    path("api/companies/regions", RegionApiCompanies.as_view(), name="map_api_region_companies"),
    path("api/companies/departments", DepartmentsApiCompanies.as_view(), name="map_api_department_companies"),
    path("api/companies/companies", ApiCompanies.as_view(), name="map_api_companies"),
    path("api/companies/clusters", ApiCLusterCompanies.as_view(), name="map_api_companies_clusters"),
]
