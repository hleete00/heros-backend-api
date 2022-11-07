from django.contrib import admin
from .models import Employee


@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    fields = (('name',), 'role', 'description', 'image',)
    list_display = ('name', 'role',)
    list_filter = ('name', 'role',)
