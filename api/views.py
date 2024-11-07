from rest_framework import generics, views
from rest_framework.response import Response
from . import models, serializers

class FeedbackCreateView(views.APIView):
    def post(self, request):
        data = request.data

        feedback = models.Feedback.objects.create(
            name=data.get('name'),
            email=data.get('email'),
            phone=data.get('phone'),
            message=data.get('message')
        )

        files = request.FILES.values()
        for file in files:
            models.FeedbackFile.objects.create(feedback=feedback, file=file)

        return Response({'status': 'ok'})

class SEORetrieve(generics.RetrieveAPIView):
    queryset = models.SEO.objects.all()
    serializer_class = serializers.SEOSettingsSerializer
    pagination_class = None
    lookup_field = "page"