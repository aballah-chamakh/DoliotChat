from django.shortcuts import render
from reast_framework.viewsets import ModelViewSet
from .models import User
from .serializers import UserSerializer


class UserVieset(ModelViewSet):
    model = User
    serializer_class = UserSerializer


class ProfileViewSet(ModelViewSet):
    model = Profile
    serializer_class = ProfileSerializer 
