from rest_framework import serializers
from .models import Animals, Deforestations

class AnimalsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Animals
        fields = "__all__"

class DeforestationsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Deforestations
        fields = "__all__"