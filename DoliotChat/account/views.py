from rest_framework.viewsets import ModelViewSet
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import action
from .models import User,Profile
from .serializers import UserSerializer,ProfileSerializer


class UserViewset(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    @action(methods=['get'],detail=False)
    def get_user_info(self,request):
        user_obj = request.user
        serializer = UserSerializer(user_obj,many=False)
        return Response({"user_info":serializer.data},status=status.HTTP_200_OK)




class ProfileViewSet(ModelViewSet):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
