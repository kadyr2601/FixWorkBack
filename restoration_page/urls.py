from django.urls import path
from . import views


urlpatterns = [
    path('retrieve/<str:slug>', views.RestorationRetrieve.as_view()),
]