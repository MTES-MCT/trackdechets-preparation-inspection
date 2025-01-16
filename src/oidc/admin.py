from django.contrib import admin

from .models import OidcLogin


@admin.register(OidcLogin)
class OidcLogintAdmin(admin.ModelAdmin):
    list_display = ["provider", "user", "account_created", "created_at"]
