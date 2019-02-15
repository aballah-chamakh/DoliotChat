from rest_framework import serializers
from .models import User,Profile


class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(source='password',write_only=True)
    password2 = serializers.CharField(write_only=True)
    class Meta :
        model = User
        fields = ['id','username','email','password','password2']
    def validate(self,data):
        email = data.get('email')
        qs = User.objects.filter(email=email)
        if qs :
            raise serializers.ValidationError('email already exist')
        password = data.get('password')
        password2 = data.get('password2')
        if password != password2 :
            raise serializers.ValidationError('passwords should match')
    def save(self,validated_data):
        email = validated_data.get('email')
        username = validated_data.get('username')
        password = validated_data.get('password')
        user_obj = User(email=email,username=username)
        user_obj.set_password(password)
        user_obj.save()
        return user_obj

class ProfileSerializer(serializers.ModelSerializer):

    user = UserSerializer(read_only=True)
    class Meta :
        model = Profile
        fields = ['id','user','image']
