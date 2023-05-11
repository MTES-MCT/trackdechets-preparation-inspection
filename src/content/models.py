from django.db import models
from django.utils.translation import gettext_lazy as _


class FeedbackResult(models.Model):
    content = models.TextField(verbose_name=_("Contenu"))
    created = models.DateTimeField(verbose_name=_("Date"), auto_now_add=True)
    author = models.EmailField(verbose_name=_("Rempli par"))

    class Meta:
        verbose_name = _("Résultat")
        verbose_name_plural = _("Résultats")
        ordering = ("-created",)
        app_label = "content"

        indexes = [
            models.Index(fields=["created", "author"]),
        ]
