from django.urls import path
from . import views


urlpatterns = [
    path('list', views.PortfolioList.as_view()),
    path('', views.PortfolioPageView.as_view())
]