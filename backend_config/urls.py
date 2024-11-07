from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('service/', include('api.urls')),
    path('home_page/', include('home_page.urls')),
    path('projects_page/', include('projects_page.urls')),
    path('reviews_page/', include('reviews_page.urls')),
    path('restoration_page/', include('restoration_page.urls')),
    path('contacts_page/', include('contacts_page.urls')),
    path('portfolio_page/', include('portfolio_page.urls')),
    path('blogs_page/', include('blogs_page.urls')),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

