from django.contrib import admin
from django.urls import path, include
from rest_framework.documentation import include_docs_urls
from django.views import static
from django.conf import settings
from django.conf.urls import url

urlpatterns = [
    path('admin/', admin.site.urls),
    path("api/", include('usercrud.urls')),
    path('', include_docs_urls(title='User Api')),
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
