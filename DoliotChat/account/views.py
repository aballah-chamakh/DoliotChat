from rest_framework.viewsets import ModelViewSet
from .models import User,Profile
from .serializers import UserSerializer,ProfileSerializer


class UserViewset(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class ProfileViewSet(ModelViewSet):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
