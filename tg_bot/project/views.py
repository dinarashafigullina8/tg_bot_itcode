from django.forms import model_to_dict
from project.models import Request, User
from send_mail import main
from rest_framework.views import APIView
from rest_framework.response import Response
import runpy
from django.shortcuts import render
from project.forms import AddRequestForm


def new_request(request):
    if request.method == 'POST':
        form = AddRequestForm(request.POST)
        if form.is_valid:
            form.save()
            main()
            runpy.run_module(mod_name='bot')
            
    else:
        form = AddRequestForm
    context = {
        'form': form,
        'title': 'Новая заявка'
    }
    return render(request, 'template.html', context=context)

# class NewRequestView(APIView):
#     def post(self, request):
#         request_new = Request.objects.create(region=request.data['region'])
#         main()
#         runpy.run_module(mod_name='bot')
#         return Response(model_to_dict(request_new)) 

    
        

