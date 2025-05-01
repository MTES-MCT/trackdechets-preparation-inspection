import datetime as dt

from django.db import models
from django.utils import timezone


class RegistryV2ExportQuerySet(models.QuerySet):
    def recent(self, days_ago=2):
        cutoff_date = timezone.now() - dt.timedelta(days=days_ago)

        return self.filter(created_at__gte=cutoff_date)
