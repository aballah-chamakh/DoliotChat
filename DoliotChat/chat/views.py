from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .models import Thread
from .serializers import ThreadSerializer

class ThreadViewSet(ModelViewSet):
    queryset = Thread.objects.all()
    serializer_class = ThreadSerializer
