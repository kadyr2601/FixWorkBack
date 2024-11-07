from rest_framework import serializers
from .models import Portfolio, PortfolioPage

class PortfolioPageSerializer(serializers.ModelSerializer):
    class Meta:
        model = PortfolioPage
        fields = '__all__'
        depth = 1

class PortfolioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Portfolio
        fields = '__all__'