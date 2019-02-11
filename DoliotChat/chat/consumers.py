from channels.generic.websocket import AsyncJsonWebsocketConsumer
from channels.db import database_sync_to_async

# connect on thread_name => abdallah11_zied25
#
class ChatConsumer(AsyncJsonWebsocketConsumer):
    async def websocket_connect(self,event):
        username  = self.scope['user'].username
        self.other_username,self.otheruser_id = self.scope['kwargs']['username'].split('_')
        id = self.scope['user'].id
        self.thread_name1 = username+str(id)+other_user
        self.thread_name2 = otheruser+ username+str(id)
        self.thread = await self.get_thread_or_create_new_one()
        await self.accept()

    async def websocket_receive(self,event):
        print(event)

    async def websocket_disconnect(self,event):
        print(event)

    @database_sync_to_async
    def get_thread_or_create_new_one(self):
        thread_obj = Thread.objects.get(thread_name_in = [self.thread_name1,self.thread_name2])
        if not thread_obj :
            second_user = Porfile.objects.get(id=self.otheruser_id).user
            thread_obj = Thread.objects.create(thread_name=self.thread_name1,first_user = self.scope['user'],second_user=second_user)
        return thread_user