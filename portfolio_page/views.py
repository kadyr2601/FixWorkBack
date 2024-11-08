from rest_framework import views, response, generics
from .models import Portfolio, PortfolioPage
from .serializers import PortfolioSerializer, PortfolioPageSerializer


class PortfolioList(views.APIView):
    def get(self, request):
        portfolios = Portfolio.objects.all()
        serializer = PortfolioSerializer(portfolios, many=True)
        return response.Response(serializer.data)

class PortfolioPageView(views.APIView):
    def get(self, request):
        portfolio_page = PortfolioPage.objects.first()
        serializer = PortfolioPageSerializer(portfolio_page)
        return response.Response(serializer.data)