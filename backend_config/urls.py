from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('cdn/service/', include('api.urls')),
    path('cdn/home_page/', include('home_page.urls')),
    path('cdn/projects_page/', include('projects_page.urls')),
    path('cdn/reviews_page/', include('reviews_page.urls')),
    path('cdn/restoration_page/', include('restoration_page.urls')),
    path('cdn/contacts_page/', include('contacts_page.urls')),
    path('cdn/portfolio_page/', include('portfolio_page.urls')),
    path('cdn/blogs_page/', include('blogs_page.urls')),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

