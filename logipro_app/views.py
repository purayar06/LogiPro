from django.shortcuts import render
from .models import logiProItems 
from django.http import HttpResponseRedirect 

from django.contrib.auth.decorators import login_required

def login(request):
    return render(request, 'login.html')


@login_required(login_url='/login')
def logipro_appView(request):
    
    user_email = request.user.email
    all_items = logiProItems.objects.filter(user=user_email)
    return render(request, 'basicDetails.html',  {'all_items':all_items})

