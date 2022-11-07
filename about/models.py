from django.db import models
from django.utils.translation import gettext_lazy as _


class Employee(models.Model):
    name = models.CharField(verbose_name=_(
        "Employee Name"), max_length=120)
    role = models.CharField(verbose_name=_(
        "Employee Role"), max_length=60)
    description = models.TextField(verbose_name=_(
        "Employee Description"), blank=True)
    image = models.ImageField(
        upload_to='about/static/employee_images/', null=True, blank=True)

    class Meta:
        verbose_name = _("Employee")
        verbose_name_plural = _("Employees")

    def __str__(self):
        return self.name
