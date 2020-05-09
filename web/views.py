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
