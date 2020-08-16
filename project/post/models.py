from django.db import models
from django.contrib.auth.models import User


#save image
def image_upload(instance,filename):
    imagename , extension = filename.split(".")
    return "jobs/%s.%s"%(instance.id,extension)
# Create your models here.
class Post(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    title= models.CharField(max_length=20)
    desciptions= models.TextField(max_length=50)
    post= models.TextField(max_length=2000)
    image=models.ImageField(upload_to=image_upload)
    pub_date= models.DateTimeField(auto_now=True)
    def __str__(self):
        return str(self.title)