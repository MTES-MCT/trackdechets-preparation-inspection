from django.conf import settings
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.sites.shortcuts import get_current_site
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.utils.translation import gettext_lazy as _

from .forms import AdminCustomUserChangeForm, AdminCustomUserCreationForm
from .models import User


@admin.action(description="Send invitation email")
def send_invitation_email(_, request, queryset):
    for user in queryset:
        if user.last_login:
            continue
        current_site = get_current_site(request)

        domain = current_site.domain
        body = render_to_string("emails/invitation/welcome.html", {"domain": domain})

        message = EmailMultiAlternatives(
            subject="Trackdéchets - outil de préparation de fiche d'inspection",
            body=body,
            from_email=settings.DEFAULT_FROM_EMAIL,
            to=[user.email],
        )

        message.send(fail_silently=False)


@admin.register(User)
class CustomUserAdmin(UserAdmin):
    add_form = AdminCustomUserCreationForm
    form = AdminCustomUserChangeForm
    model = User
    actions = [send_invitation_email]
    search_fields = ("username", "email")
    list_display = [
        "email",
        "user_type",
        "username",
        "is_staff",
        "is_superuser",
        "last_login",
        "date_joined",
        "monaiot_connexion",
        "monaiot_signup",
    ]

    fieldsets = (
        (None, {"fields": ("username", "password")}),
        (_("Personal info"), {"fields": ("email",)}),
        (
            _("Permissions"),
            {
                "fields": (
                    "is_active",
                    "is_staff",
                    "is_superuser",
                    "user_type",
                    "groups",
                    "user_permissions",
                ),
            },
        ),
        (_("Important dates"), {"fields": ("last_login", "date_joined")}),
    )
    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": ("username", "email", "password1", "password2"),
            },
        ),
    )
