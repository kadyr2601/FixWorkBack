from rest_framework import views, response, generics
from .models import Portfolio, PortfolioPage
from .serializers import PortfolioSerializer, PortfolioPageSerializer


class PortfolioList(generics.ListAPIView):
    queryset = Portfolio.objects.all()
    serializer_class = PortfolioSerializer

class PortfolioPageView(views.APIView):
    def get(self, request):
        portfolio_page = PortfolioPage.objects.first()
        serializer = PortfolioPageSerializer(portfolio_page)
        return response.Response(serializer.data)