from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
# Create your models here.
class Profile(models.Model):
    user= models.OneToOneField(User, on_delete=models.CASCADE)
    phone=models.CharField(max_length=23,null=True,blank=True)
    adress=models.CharField(max_length=500)
    def __str__(self):
        return str(self.user)
@ receiver(post_save,sender=User)
def my_call(sender,instance,created,**kwargs):
    if created:
        Profile.objects.create(
            user=instance,
        )