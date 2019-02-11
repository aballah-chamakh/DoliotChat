from rest_framework import serializers
from .models import Message,Thread

class MessageSerializer(serializers.ModelSerializer):
    owner = serializers.CharField(source='owner.user.username')
    class Meta :
        fields = ('owner','content')
class ThreadSerializer(serializers.ModelSerializer):
    messages = serializers.MethodSerializer('get_thread_messages')
    class Meta :
        fields = ('message')
    def get_thread_messages(self,thread_obj):
        messages_qs = Message.objects.all()
        serializer = MessageSerializer(messages_qs,many=True)
        return serializers.all()
        
