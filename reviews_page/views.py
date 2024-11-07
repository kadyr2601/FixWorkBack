from rest_framework import generics, response, views
from . import models, serializers

class ReviewListView(generics.ListAPIView):
    queryset = models.Review.objects.all()
    serializer_class = serializers.ReviewSerializer


class ReviewsPageView(views.APIView):
    def get(self, request):
        reviews_page = models.ReviewsPage.objects.first()
        serializer = serializers.ReviewsPageSerializer(reviews_page, context={'request': request})
        return response.Response(serializer.data)


