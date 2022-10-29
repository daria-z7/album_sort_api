from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('', include('album.urls', namespace='albums')),
    path('admin/', admin.site.urls),
]
