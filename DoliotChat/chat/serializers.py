from rest_framework import serializers
from .models import Message,Thread

class MessageSerializer(serializers.ModelSerializer):
    owner = serializers.CharField(source='owner.user.username')
    other_user = serializers.CharField(source='other_user.user.username')
    class Meta :
        fields = ('owner','other_user','content')
class ThreadSerializer(serializers.ModelSerializer):
    messages = serializers.SerializerMethodField('get_thread_messages')
    first_user = serializers.CharField(source='first_user.user.username')
    second_user = serializers.CharField(source='second_user.user.username')

    class Meta :
        fields = ('first_user','second_user','message')

    def get_thread_messages(self,thread_obj):
        messages_qs = Message.objects.all()
        serializer = MessageSerializer(messages_qs,many=True)
        return serializers.all()
