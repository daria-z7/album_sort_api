from django.urls import path
from .views import AlbumTable

app_name = 'albums'

urlpatterns = [
    path('api/albums/', AlbumTable.as_view(), name='index'),
]
