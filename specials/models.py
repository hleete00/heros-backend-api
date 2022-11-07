from django.db import models
from django.utils.translation import gettext_lazy as _


class Special(models.Model):
    DAY_OF_THE_WEEK = (
        ('1', 'Monday'),
        ('2', 'Tuesday'),
        ('3', 'Wednesday'),
        ('4', 'Thursday'),
        ('5', 'Friday'),
        ('6', 'Saturday'),
        ('7', 'Sunday'),
    )

    description = models.CharField(verbose_name=_(
        "Special Description"), max_length=200)
    day = models.CharField(verbose_name=_(
        "Day of Special"), max_length=50, choices=DAY_OF_THE_WEEK)

    class Meta:
        verbose_name = _("Special")
        verbose_name_plural = _("Specials")

    def __str__(self):
        return self.description
