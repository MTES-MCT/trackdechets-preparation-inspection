"""inspection URL Configuration"""
from django.conf import settings
from django.contrib import admin
from django.urls import path

urlpatterns = [
    path(f"{settings.ADMIN_SLUG}/", admin.site.urls),
]
