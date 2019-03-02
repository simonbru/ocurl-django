from django.conf import settings
from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _


class Link(models.Model):
    name = models.CharField(verbose_name=_('name'), max_length=120, unique=True)
    owner = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='links',
        blank=True,
        null=True,
    )
    destination = models.URLField(verbose_name=_('destination'))
    expiration_date = models.DateTimeField(verbose_name=_('expiration date'), blank=True, null=True)

    @property
    def is_expired(self):
        return self.expiration_date and self.expiration_date < timezone.now()
