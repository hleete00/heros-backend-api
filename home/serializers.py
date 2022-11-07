from rest_framework import serializers

from .models import HomeCard, HomeSlide


class HomeCardSerializer(serializers.ModelSerializer):
    class Meta:
        model = HomeCard
        fields = ["id", "title", "image", "description"]


class HomeSlideSerializer(serializers.ModelSerializer):
    class Meta:
        model = HomeSlide
        fields = ["id", "image"]
