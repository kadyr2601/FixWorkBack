from rest_framework import generics
from restoration_page import models, serializers


class RestorationRetrieve(generics.RetrieveAPIView):
    queryset = models.Restoration.objects.all()
    serializer_class = serializers.RestorationSerializer
    lookup_field = 'slug'
