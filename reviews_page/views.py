from rest_framework import response, views, generics
from . import models, serializers


class ReviewListView(generics.ListAPIView):
    queryset = models.Review.objects.all()
    serializer_class = serializers.ReviewSerializer

class ReviewsPageView(views.APIView):
    def get(self, request):
        reviews_page = models.ReviewsPage.objects.first()
        serializer = serializers.ReviewsPageSerializer(reviews_page)
        return response.Response(serializer.data)