from django.contrib import admin
from .models import *

class CustomUserProfile(admin.ModelAdmin):
    list_display = ['user','uuid','sex']

class CustomPost(admin.ModelAdmin):
    list_display = ['title','content']

admin.site.register(Userprofile, CustomUserProfile)
admin.site.register(Post, CustomPost)
