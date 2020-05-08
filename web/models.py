from django.db import models
from django.contrib.auth.models import  User

class Token(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    token = models.CharField(max_length=47)


class Expense(models.Model):
    text = models.CharField(max_length=255)
    date = models.DateTimeField()
    amount = models.BigIntegerField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.text

class Income(models.Model):
    text = models.CharField(max_length=100)
    date = models.DateTimeField()
    amount = models.BigIntegerField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def  __str__(self):
        return self.text

class Post(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    title = models.CharField(max_length=200,blank=False,null=False)
    content = models.CharField(max_length=800,blank=False,null=False)
    photo = models.ImageField()

    def __str__(self):
        return self.title
