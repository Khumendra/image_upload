from django.conf import settings
from django.conf.urls import url
from django.conf.urls.static import static
from django.contrib import admin

from .views import *

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^image_upload/', hotel_image_view, name='image_upload'),
    url(r'^success/', sucess, name='success'),
    url(r'^hotel_images/', display_hotel_images, name='hotel_images'),
]

if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL,
                              document_root=settings.MEDIA_ROOT)
