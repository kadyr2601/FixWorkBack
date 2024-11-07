from django.urls import path
from . import views
urlpatterns = [
    path('list', views.ReviewListView.as_view()),
    path('', views.ReviewsPageView.as_view()),
]