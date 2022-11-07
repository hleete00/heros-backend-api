from django.db import models
from django.utils.translation import gettext_lazy as _


class HomeCard(models.Model):
    title = models.CharField(verbose_name=_(
        "Title"), max_length=100)

    image = models.ImageField(verbose_name=_(
        "Image"), upload_to='home/static/home_card_images/')
    description = models.TextField(verbose_name=_("Description"))

    class Meta:
        verbose_name = _("Home Card")
        verbose_name_plural = _("Home Cards")

    def __str__(self):
        return self.title


class HomeSlide(models.Model):
    title = models.CharField(verbose_name=_(
        "Title"), max_length=100)
    image = models.ImageField(verbose_name=_(
        "Image"), upload_to='home/static/home_slide_images/')

    class Meta:
        verbose_name = _("Home Slide")
        verbose_name_plural = _("Home Slides")

    def __str__(self):
        return self.title
