from django.urls import path
from . import views

urlpatterns = [
    path('feedback-create', views.FeedbackCreateView.as_view()),
    path('seo/<str:page>', views.SEORetrieve.as_view()),
]