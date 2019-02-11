from django.db import models
from account.models import Profile
from django.db.models.signals import post_save,pre_save
from django.dispatch import receiver
from channels.layers import get_channel_layer

# Create your models here.


class Thread(models.Model):
    first_user = models.ManyToMany(Profile)
    second_user = models.ManyToMany(Profile)
    thread_name = models.CharField(max_length=255,blank=True,null=True)
    def __str__(self):
        return 'this thread for {first_user} & {second_user}'.format(first_user=self.first_user.user.username,
                                                                     second_user=self.second_user.user.username)
class Message(models.Model):
    owner = models.OneToOneField(Profile,on_delete=models.CASCADE)
    content = models.TextField()
    Thread = models.ForeignKey(Thread,on_delete=models.CASCADE)
    def __str__(self):
        return 'msg from {owner} on the thread {thread}'.format(owner=self.owner.user.username,thread=self.thread)


class MessageNotification(models.Model):
    message = models.OneToOneField(Message,on_delete=models.CASCADE)
    def __str__(self):
        return self.message


@receiver(post_save, sender=Message)
def create_user_profile(sender, message, created, **kwargs):

    if created :
        if message.owner != message.first_user and message.first_user is None :
            MessageNotification.objects.create(message=message)



        profile_obj = Profile.objects.create(user=instance)
