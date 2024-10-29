from rest_framework import generics, views
from rest_framework.response import Response
from . import models, serializers


class MainBannerView(generics.RetrieveAPIView):
    queryset = models.MainBanner.objects.all()
    serializer_class = serializers.MainBannerSerializer
    lookup_field = "page"


class ProjectListView(generics.ListAPIView):
    queryset = models.Project.objects.all()
    serializer_class = serializers.ProjectSerializer


class PortfolioListView(generics.ListAPIView):
    queryset = models.Portfolio.objects.all()
    serializer_class = serializers.PortfolioSerializer


class ServicesBannerView(generics.RetrieveAPIView):
    queryset = models.Service.objects.all()
    serializer_class = serializers.ServiceSerializer
    lookup_field = "page"


class PageBannerView(generics.RetrieveAPIView):
    queryset = models.PageBanner.objects.all()
    serializer_class = serializers.PageBannerSerializer
    lookup_field = "page"

    def get_object(self):
        page = self.kwargs.get('page')
        return models.PageBanner.objects.filter(page=page)

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance, many=True)
        return Response(serializer.data)


class ReviewListView(generics.ListAPIView):
    queryset = models.Review.objects.all()
    serializer_class = serializers.ReviewSerializer


class BlogListView(generics.ListAPIView):
    queryset = models.Blog.objects.all()
    serializer_class = serializers.BlogSerializer


class BlogRetrieve(generics.RetrieveAPIView):
    queryset = models.Blog.objects.all()
    serializer_class = serializers.BlogSerializer
    lookup_field = "slug"


class PartnerListView(generics.ListAPIView):
    queryset = models.Partner.objects.all()
    serializer_class = serializers.PartnerSerializer


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


class RestorationListView(generics.ListAPIView):
    queryset = models.Restoration.objects.all()
    serializer_class = serializers.RestorationListSerializer


class RestorationRetrieve(generics.RetrieveAPIView):
    queryset = models.Restoration.objects.all()
    serializer_class = serializers.RestorationSerializer
    pagination_class = None
    lookup_field = "slug"