from django.shortcuts import render
from django.http import JsonResponse
from json import JSONEncoder
from django.views.decorators.csrf import  csrf_exempt
from web.models import  *
from datetime import  datetime
from django.contrib.auth.models import User
from rest_framework.views import  APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated



class HelloView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        content = {'message': 'Hello, World!'}
        return Response(content)


@csrf_exempt
def submit_expense(request):

        if 'token' in request.POST:
            this_token = request.POST['token']
        else:
            this_token = '123456789'
        this_user = User.objects.filter(token__token = this_token).get()

        if 'date' not in request.POST:
            date = datetime.now()

        item = Expense()
        item.user = this_user
        item.amount = request.POST['amount']
        item.text = request.POST['text']
        item.date = date

        item.save()

        return JsonResponse({
         'status' : 'OK',
        }, encoder = JSONEncoder)

@csrf_exempt
def submit_income(request):

        if 'token' in request.POST:
            this_token = request.POST['token']
        else:
            this_token = '123456789'
        this_user = User.objects.filter(token__token = this_token).get()

        if 'date' not in request.POST:
            date = datetime.now()

        item = Income()
        item.user = this_user
        item.amount = request.POST['amount']
        item.text = request.POST['text']
        item.date = date

        item.save()

        return JsonResponse({
         'status' : 'OK',
        }, encoder = JSONEncoder)
