from rest_framework import serializers
from .models import Review, ReviewsPage

class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = '__all__'

class ReviewsPageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ReviewsPage
        fields = '__all__'
        depth = 1