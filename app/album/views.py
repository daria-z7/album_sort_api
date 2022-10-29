from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.response import Response
from rest_framework.views import APIView
from django.db.models.functions import Lower

from .models import Album


class AlbumTable(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'albums/index.html'

    def get(self, request):
        sort_column = request.GET.get('sorting', 'pk')
        queryset = Album.objects.order_by(Lower(sort_column))
        return Response({'page_obj': queryset})
