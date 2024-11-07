from rest_framework import serializers
from home_page import models

class ServiceCardSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.ServiceCard
        fields = '__all__'


class HomePageSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.HomePage
        fields = '__all__'
        depth = 1