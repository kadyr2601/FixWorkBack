from rest_framework import serializers
from .models import Restoration, RestorationService


class RestorationServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = RestorationService
        fields = '__all__'

class RestorationSerializer(serializers.ModelSerializer):
    services = RestorationServiceSerializer(many=True)

    class Meta:
        model = Restoration
        fields = '__all__'
        depth = 1