from rest_framework import serializers
from .models import Message,Thread

class MessageSerializer(serializers.ModelSerializer):
    owner = serializers.CharField(source='owner.user.username')
    class Meta :
        model = Message
        fields = ('owner','content')
class ThreadSerializer(serializers.ModelSerializer):
    messages = serializers.SerializerMethodField('get_thread_messages')
    user_1 = serializers.CharField(source='first_user.user.username')
    user_2 = serializers.CharField(source='second_user.user.username')

    class Meta :
        model = Thread
        fields = ('user_1','user_2','messages')

    def get_thread_messages(self,thread_obj):
        messages_qs = Message.objects.all()
        serializer = MessageSerializer(messages_qs,many=True)
        return serializer.data
