import uuid

from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _

from accounts.models import User


class ProviderChoice(models.TextChoices):
    MONAIOT = "MONAIOT", _("MonAIOT")


class OidcLogin(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    provider = models.CharField(_("Provider"), max_length=30, choices=ProviderChoice.choices)
    user = models.ForeignKey(User, verbose_name=_("User"), on_delete=models.SET_NULL, blank=True, null=True)
    info = models.JSONField(_("Info"), default=dict)
    account_created = models.BooleanField(_("Account Created"), default=False)
    created_at = models.DateTimeField(_("Created at"), default=timezone.now)

    class Meta:
        verbose_name = _("Login OIDC")
        verbose_name_plural = _("Logins OIDC")
        ordering = ("-created_at",)
