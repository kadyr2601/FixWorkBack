from rest_framework import views, response
from home_page import models, serializers


class HomePageView(views.APIView):
    def get(self, request):
        home_page = models.HomePage.objects.first()
        serializer = serializers.HomePageSerializer(home_page)
        return response.Response(serializer.data)


class ServiceCardView(views.APIView):
    def get(self, request):
        home_page = models.ServiceCard.objects.all().order_by('-id')[:3]
        serializer = serializers.ServiceCardSerializer(home_page, many=True)
        return response.Response(serializer.data)
