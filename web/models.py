from django.db import models
import  uuid
from django.contrib.auth.models import  User

class Userprofile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar = models.ImageField(upload_to='uploads/',blank=True)
    uuid = models.UUIDField(primary_key=True,editable=False,default=uuid.uuid4)

    man_sex = '1'
    woman_sex = '0'

    sex_choices = [
    (man_sex,'man'), # man is 1
    (woman_sex,'woman'), # woman is 0
    ]
    sex = models.CharField(max_length=2,choices=sex_choices,default=man_sex)

    def  __str__(self):
        return self.user.username

class Post(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    title = models.CharField(max_length=200,blank=False,null=False)
    content = models.CharField(max_length=800,blank=False,null=False)
    photo = models.ImageField(upload_to='uploads/')

    def __str__(self):
        return self.title
