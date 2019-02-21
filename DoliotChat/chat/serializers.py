from rest_framework import serializers
from .models import Message,Thread
from account.serializers import ProfileSerializer


class MessageSerializer(serializers.ModelSerializer):
    owner = serializers.CharField(source='owner.user.username')
    owner_image = serializers.CharField(source='owner.image.url')
    profile_id = serializers.IntegerField(source='owner.id')
    class Meta :
        model = Message
        fields = ('profile_id','owner','content','owner_image')
class ThreadSerializer(serializers.ModelSerializer):
    messages = serializers.SerializerMethodField('get_thread_messages')
    first_user = ProfileSerializer()
    second_user = ProfileSerializer()

    class Meta :
        model = Thread
        fields = ('first_user','second_user','messages')

    def get_thread_messages(self,thread_obj):
        messages_qs = Message.objects.filter(thread=thread_obj)
        serializer = MessageSerializer(messages_qs,many=True)
        return serializer.data
