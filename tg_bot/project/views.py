from django.forms import model_to_dict
from django.shortcuts import render
from project.forms import AddRequestForm
from project.models import Request
# from main import send_message
from send_mail import main
import telebot
from project.config import token
from rest_framework.views import APIView
from rest_framework.response import Response



class NewRequestView(APIView):
    def post(self, request):
        request_new = Request.objects.create(
            region=request.data['region']
        )
        main()
        # send_message()
        return Response(model_to_dict(request_new))
        

