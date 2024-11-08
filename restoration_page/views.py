from rest_framework import views, response
from restoration_page import models, serializers


class RestorationRetrieve(views.APIView):
    def get(self, request, slug):
        restoration = models.Restoration.objects.get(slug=slug)
        serializer = serializers.RestorationSerializer(restoration)
        return response.Response(serializer.data)
