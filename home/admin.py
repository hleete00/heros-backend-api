from django.contrib import admin
from .models import HomeCard, HomeSlide


@admin.register(HomeCard)
class HomeCardAdmin(admin.ModelAdmin):
    list_display = ('title', 'description')


@admin.register(HomeSlide)
class HomeSlideAdmin(admin.ModelAdmin):
    list_display = ('title', "image",)
