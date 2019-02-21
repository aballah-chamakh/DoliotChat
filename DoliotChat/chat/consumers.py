from channels.generic.websocket import AsyncJsonWebsocketConsumer
from channels.db import database_sync_to_async
from .serializers import ThreadSerializer,MessageSerializer
import json
from .models import Thread,Message
from account.models import Profile
# connect on thread_name => abdallah11_zied25
#
class ChatConsumer(AsyncJsonWebsocketConsumer):
    async def websocket_connect(self,event):
        username  = self.scope['user'].username
        self.other_username,self.otheruser_id = self.scope['url_route']['kwargs']['username_id'].split('_')
        id = self.scope['user'].profile.id
        self.thread_name1 = username+str(id)+self.other_username+str(self.otheruser_id)
        self.thread_name2 = self.other_username+str(self.otheruser_id)+username+str(id)
        self.thread = await self.get_thread_or_create_new_one()
        print(self.thread.thread_name)
        serializer = ThreadSerializer(self.thread,many=False)
        await self.channel_layer.group_add(self.thread.thread_name,self.channel_name)
        await self.accept()
        await self.channel_layer.send(self.channel_name,{'type':'load.thread',
                                                       'thread':serializer.data})

    async def load_thread(self,event):
        print('load thread')
        thread = event['thread']
        data = {'type':'load_thread','thread':thread}
        await self.send_json(data)
    async def websocket_receive(self,event):
        message = json.loads(event['text'])['message']
        msg_obj = await self.create_message(message)
        serializer = MessageSerializer(msg_obj,many=False)
        await self.channel_layer.group_send(self.thread.thread_name,{'type':'send.message',
                                                            'message':serializer.data})

    async def send_message(self,event) :
        print(event)
        await self.send_json({'type':'new_message','message':event['message']})




    async def websocket_disconnect(self,event):
        self.channel_layer.group_discard(self.thread.thread_name,self.channel_name)

    @database_sync_to_async
    def get_thread_or_create_new_one(self):
        try :
            thread_obj = Thread.objects.get(thread_name__in = [self.thread_name1,self.thread_name2])
        except :
            second_user = Profile.objects.get(id=self.otheruser_id).user.profile
            thread_obj = Thread.objects.create(thread_name=self.thread_name1,first_user= self.scope['user'].profile,second_user=second_user)
            return thread_obj
        return thread_obj
    @database_sync_to_async
    def create_message(self,content):
        print(self.thread.thread_name)
        msg_obj = Message.objects.create(content=content,thread=self.thread,owner=self.scope['user'].profile)
        return msg_obj
