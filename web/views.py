from django.shortcuts import render
from django.http import JsonResponse
from json import JSONEncoder
from django.views.decorators.csrf import  csrf_exempt
from web.models import  *
from datetime import  datetime
from django.contrib.auth.models import User
from rest_framework import  status
from rest_framework.views import  APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from . import serializers

class allPost(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        try:
            all_post_temp = Post.objects.all()
            data = []

            for items in all_post_temp:
                data.append({
                    'id':items.id,
                    'title':items.title,
                    'user':items.user.username,
                    'content':items.content,
                })

            return Response({'data':data})
        except:
            return Response({'status':'Error'})


class HelloView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        content = {'message': 'Hello, World!'}
        return Response(content)


class AllUserProfile(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        try:
            all_user_profile = Userprofile.objects.all()
            data = []

            for user in all_user_profile:
                data.append({
                    'username' : user.user.username,
                    'uuid' : user.uuid,
                    'sex' : user.sex,
                })

            return Response({'data' : data},status=status.HTTP_200_OK)
        except:
            return Response({'data': 'ERROR'})

class RegisterUser(APIView):

    def post(self, request):
    #    try:
            serialized_data = serializers.RegisterUserSerializers(data=request.data)

        #    if serialized_data.is_valid():
        #        username = serializer.data.get('username')
        #        password = serializer.data.get('password')
        #        sex = serializer.data.get('sex')
        #    else:
        #        return Response({'status' : 'Bad Req'})

            username = request.data['username']
            password = request.data['password']
            sex = request.data['sex']

            new_user = User()
            new_user.username = username
            new_user.set_password(password)
            new_user.save()

            profile_user = Userprofile()
            profile_user.user = new_user
            profile_user.sex = sex
            profile_user.save()

            return Response({'data' : 'user created successful'},status=status.HTTP_200_OK)

    #    except:

        #    return Response({'data': 'ERROR'})
