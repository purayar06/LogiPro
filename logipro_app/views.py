from django.shortcuts import render
from .models import logiProItems 
from django.http import HttpResponseRedirect 

from django.contrib.auth.decorators import login_required

@login_required(login_url='/login')
def login(request):
    return render(request, 'basicDetails.html')


@login_required(login_url='/login')
def logipro_appView(request):
    
    user_email = request.user.email
    all_items = logiProItems.objects.all()
    all_items = logiProItems.objects.filter(user=user_email)
    return render(request, 'login.html',  {'all_items':all_items})

@login_required(login_url='/login')
def req_View(request):
    venue=request.venue
    print(venue)
    data=RegItems(venue=venue)
    data.save()
    
