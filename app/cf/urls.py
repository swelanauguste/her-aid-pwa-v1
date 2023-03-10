from django.contrib import admin
from django.urls import include, path
from django.urls import re_path as url
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    url("", include("pwa.urls")),
    path("", include("heraid.urls")),
    path("admin/", admin.site.urls),
]


urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)