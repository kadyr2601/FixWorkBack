from django.urls import path
from . import views

urlpatterns = [
    path('main-banner/<str:page>', views.MainBannerView.as_view()),
    path('project-list', views.ProjectListView.as_view()),
    path('portfolio-list', views.PortfolioListView.as_view()),
    path('services-banner/<str:page>', views.ServicesBannerView.as_view()),
    path('page-banner/<str:page>', views.PageBannerView.as_view()),
    path('review-list', views.ReviewListView.as_view()),
    path('blog-list', views.BlogListView.as_view()),
    path('blog/<str:slug>', views.BlogRetrieve.as_view()),
    path('partner-list', views.PartnerListView.as_view()),
    path('feedback-create', views.FeedbackCreateView.as_view()),
]