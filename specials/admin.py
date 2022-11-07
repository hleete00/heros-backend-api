from django.contrib import admin
from .models import Special


@admin.register(Special)
class SpecialAdmin(admin.ModelAdmin):
    list_display = ('day', 'description',)
    list_filter = ('day',)
    ordering = ('day',)
