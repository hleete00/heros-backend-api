from django.contrib import admin
from .models import Event


@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    fields = (('name',), 'date', 'time',
              'genre', 'description', 'image',)
    list_display = ('name', 'date',)
    list_filter = ('date',)
    ordering = ('-date',)
