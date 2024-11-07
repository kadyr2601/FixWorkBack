from django.urls import path
from . import views


urlpatterns = [
    path('list', views.BlogView.as_view()),
    path('', views.BlogsPageView.as_view()),
    path('retrieve/<str:slug>', views.BlogRetrieve.as_view()),
]