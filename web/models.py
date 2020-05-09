from django.db import models
from django.contrib.auth.models import  User

class Userprofile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar = models.ImageField(upload_to='uploads/')

    def __str__(self):
        return self.user.name

class Post(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    title = models.CharField(max_length=200,blank=False,null=False)
    content = models.CharField(max_length=800,blank=False,null=False)
    photo = models.ImageField(upload_to='uploads/')

    def __str__(self):
        return self.title
