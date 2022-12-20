
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
#import labelapp

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('labelapp.urls')),
] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
