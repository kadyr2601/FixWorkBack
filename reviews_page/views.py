from rest_framework import response, views
from . import models, serializers


class ReviewListView(views.APIView):
    def get(self, request):
        reviews = models.Review.objects.all()
        serializer = serializers.ReviewSerializer(reviews, many=True)
        return response.Response(serializer.data)

class ReviewsPageView(views.APIView):
    def get(self, request):
        reviews_page = models.ReviewsPage.objects.first()
        serializer = serializers.ReviewsPageSerializer(reviews_page)
        return response.Response(serializer.data)