from rest_framework import viewsets
from .models import Jrello
from .serializers import JrelloSerializer
from rest_framework.views import APIView


class JrelloViewSet(viewsets.ModelViewSet):
    queryset = Jrello.objects.all().order_by('name')
    serializer_class = JrelloSerializer
