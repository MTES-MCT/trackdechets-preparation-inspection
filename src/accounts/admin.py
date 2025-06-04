import uuid

from django.conf import settings
from django.contrib import admin, messages
from django.contrib.auth.admin import UserAdmin
from django.contrib.sites.shortcuts import get_current_site
from django.core.mail import EmailMessage
from django.http import HttpResponseRedirect
from django.template.loader import render_to_string
from django.urls import reverse
from django.utils.translation import gettext_lazy as _
from import_export import resources
from import_export.admin import ImportExportMixin
from import_export.exceptions import FieldError

from .constants import UserTypeChoice
from .forms import AdminCustomUserChangeForm, AdminCustomUserCreationForm
from .models import User


class UserResource(resources.ModelResource):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.emails = User.objects.values_list("email", flat=True)

    def before_import_row(self, row, **kwargs):
        if not row["user_category"]:
            raise FieldError("Missing user_category")
        row["username"] = f"{row['first_name']} {row['last_name']}"

    def validate_instance(self, instance, import_validation_errors=None, validate_unique=True):
        return super().validate_instance(instance, import_validation_errors, validate_unique)

    def skip_row(self, instance, original, row, import_validation_errors=None):
        skip = super().skip_row(instance, original, row, import_validation_errors)
        # skip existing accounts
        if row["email"] in self.emails:
            return True
        return skip

    def before_save_instance(self, instance, row, **kwargs):
        instance.id = uuid.uuid4()
        instance.is_active = True
        instance.is_staff = False
        instance.is_superuser = False
        instance.user_type = UserTypeChoice.HUMAN
        instance.password = str(uuid.uuid4())
        instance.email = instance.email.lower()

    class Meta:
        model = User
        fields = ["id", "username", "email", "user_category"]


@admin.action(description="Send invitation email")
def send_invitation_email(_, request, queryset):
    skipped_users = []
    for user in queryset:
        if user.last_login:
            skipped_users.append(user.email)
            continue

        if user.oidc_signup or user.oidc_connexion:
            skipped_users.append(user.email)
            continue

        current_site = get_current_site(request)

        domain = current_site.domain
        body = render_to_string(
            "emails/invitation/welcome.html", {"domain": domain, "password_reset_url": reverse("password_reset")}
        )

        message = EmailMessage(
            subject="Trackdéchets - Accès à Vigiedéchets",
            body=body,
            from_email=settings.DEFAULT_FROM_EMAIL,
            to=[user.email],
        )
        message.content_subtype = "html"  # This is the crucial line
        message.send(fail_silently=False)

    if skipped_users:
        messages.add_message(
            request,
            messages.WARNING,
            f"Les utilisateurs suivants ont été ignorés car déjà activés {','.join(skipped_users)}",
        )


@admin.register(User)
class CustomUserAdmin(ImportExportMixin, UserAdmin):
    add_form = AdminCustomUserCreationForm
    form = AdminCustomUserChangeForm
    model = User
    actions = [send_invitation_email]
    search_fields = ("username", "email")
    list_display = [
        "email",
        "user_type",
        "user_category",
        "username",
        "is_active",
        "is_staff",
        "is_superuser",
        "last_login",
        "date_joined",
        "oidc_connexion",
        "oidc_signup",
    ]
    list_filter = ("is_staff", "is_superuser", "is_active", "user_type", "user_category", "date_joined")
    resource_classes = [
        UserResource,
    ]
    fieldsets = (
        (None, {"fields": ("username", "password")}),
        (_("Personal info"), {"fields": ("email",)}),
        (
            _("Segmentation"),
            {
                "fields": (
                    "user_type",
                    "user_category",
                )
            },
        ),
        (
            _("OIDC"),
            {
                "fields": (
                    "oidc_signup",
                    "oidc_connexion",
                )
            },
        ),
        (
            _("Permissions"),
            {
                "fields": (
                    "is_active",
                    "is_staff",
                    "is_superuser",
                    "groups",
                    "user_permissions",
                ),
            },
        ),
        (_("Important dates"), {"fields": ("last_login", "date_joined")}),
    )

    add_fieldsets = (
        (None, {"fields": (("username", "email", "password1", "password2"))}),
        (
            _("Segmentation"),
            {"fields": ("user_category",)},
        ),
    )

    def response_add(self, request, obj, post_url_continue=None):
        # Redirect to change list

        list_url = reverse("admin:accounts_user_changelist")
        return HttpResponseRedirect(list_url)
