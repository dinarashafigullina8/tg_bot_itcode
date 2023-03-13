from django.shortcuts import render
from project.forms import AddRequestForm
from project.models import Request
from main import send_message
from send_mail import send_email

def new_request(request):
    if request.method == 'POST':
        form = AddRequestForm(request.POST)
        if form.is_valid:
            form.save()
            send_message()
            send_email()
            
    else:
        form = AddRequestForm
    context = {
        'form': form,
        'title': 'Новая заявка'
    }
    return render(request, 'template.html', context=context)
    
