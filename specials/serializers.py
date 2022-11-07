from rest_framework import serializers

from .models import Special


class SpecialSerializer(serializers.ModelSerializer):
    class Meta:
        model = Special
        fields = ["id", "description", "day"]
