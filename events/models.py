from django.db import models
from django.utils.translation import gettext_lazy as _


class Event(models.Model):
    name = models.CharField(verbose_name=_(
        "Event Name"), max_length=120)
    date = models.DateField(verbose_name=_(
        "Date"),)
    time = models.TimeField(verbose_name=_(
        "Time"),)
    genre = models.CharField(verbose_name=_(
        "Event Genre"), max_length=60)
    description = models.TextField(verbose_name=_(
        "Description"), blank=True)
    image = models.ImageField(
        upload_to='events/static/event_images/', null=True, blank=True)

    class Meta:
        verbose_name = _("Event")
        verbose_name_plural = _("Events")

    def __str__(self):
        return self.name
