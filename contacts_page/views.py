from rest_framework import views, serializers, response
from .models import ContactsPage

class ContactPageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContactsPage
        fields = '__all__'
        depth = 1

class ContactPageView(views.APIView):
    def get(self, request):
        contact_page = ContactsPage.objects.first()
        serializer = ContactPageSerializer(contact_page, context={'request': request})
        return response.Response(serializer.data)
