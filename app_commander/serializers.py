from rest_framework import serializers
from .models import Commander


class CommanderListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Commander
        fields = "__all__"
