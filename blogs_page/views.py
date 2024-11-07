from rest_framework import views, response, serializers, generics
from .models import Blog, BlogsPage

class BlogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Blog
        fields = '__all__'

class BlogsPageSerializer(serializers.ModelSerializer):
    class Meta:
        model = BlogsPage
        fields = '__all__'
        depth = 1

class BlogsPageView(views.APIView):
    def get(self, request, *args, **kwargs):
        page = BlogsPage.objects.first()
        serializer = BlogsPageSerializer(page, context={'request': request})
        return response.Response(serializer.data)


class BlogView(generics.ListAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer

class BlogRetrieve(generics.RetrieveAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer
    lookup_field = 'slug'