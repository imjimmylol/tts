from django.contrib import admin
from django.urls import path
# from django.conf.urls import include, url
from tts.views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('tts_api/', tts_api),
    path('demo/', demo),
]

urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)