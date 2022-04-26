
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('nepl-administration/', admin.site.urls),
    path('', include('nivdas.urls')),
]

admin.site.site_header = "NEPL Administration"
if settings.DEBUG == True:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
