from __future__ import absolute_import, print_function

from django.db import models
from django.utils import timezone

from sentry.db.models import FlexibleForeignKey, Model, sane_repr


class Dashboard(Model):
    """
    A dashboard.
    """

    __core__ = True

    title = models.CharField(max_length=255)
    created_by = FlexibleForeignKey("sentry.User")
    organization = FlexibleForeignKey("sentry.Organization")
    date_added = models.DateTimeField(default=timezone.now)

    class Meta:
        app_label = "sentry"
        db_table = "sentry_dashboard"
        unique_together = (("organization", "title"),)

    __repr__ = sane_repr("organization", "title")
