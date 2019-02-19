from django.db import models
from account.models import Profile
from django.db.models.signals import post_save,pre_save
from django.dispatch import receiver
from channels.layers import get_channel_layer

# Create your models here.


class Thread(models.Model):
    first_user = models.ForeignKey(Profile,on_delete=models.CASCADE,related_name='first_user',null=True,blank=True)
    second_user = models.ForeignKey(Profile,on_delete=models.CASCADE,related_name='second_user',null=True,blank=True)
    thread_name = models.CharField(max_length=255,blank=True,null=True)
    # def __str__(self):
    #     return 'this thread for {first_user} & {second_user}'.format(first_user=self.first_user.user.username,
    #                                                                  second_user=self.second_user.user.username)
class Message(models.Model):
    owner = models.ForeignKey(Profile,on_delete=models.CASCADE)
    content = models.TextField()
    thread = models.ForeignKey(Thread,on_delete=models.CASCADE)

    def __str__(self):
        return 'msg from {owner} on the thread {thread}'.format(owner=self.owner.user.username,thread=self.thread)


    # @property
    # def other_user(self):
    #     if self.owner != self.thread.first_user :
    #         return self.thread.first_user
    #     else :
    #         return self.thread.second_user

# @receiver(post_save, sender=Message)
# def create_user_profile(sender, instance, created, **kwargs):
#     if created :
#         profile_obj = Profile.objects.create(user=instance)
