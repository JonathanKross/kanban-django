from django.shortcuts import render
from rest_framework import viewsets
from .models import Card
from .serializers import CardSerializer


class CardsViewSet(viewsets.ModelViewSet):
    queryset = Card.objects.all().order_by('-id')
    serializer_class = CardSerializer
