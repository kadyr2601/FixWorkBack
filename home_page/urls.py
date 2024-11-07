from django.urls import path
from home_page.views import HomePageView, ServiceCardView


urlpatterns = [
    path('', HomePageView.as_view()),
    path('services', ServiceCardView.as_view()),

]