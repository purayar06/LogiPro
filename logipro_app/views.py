from django.shortcuts import render
from .models import basicDetailsItems 
from django.http import HttpResponseRedirect 
from .models import reqItems

from django.contrib.auth.decorators import login_required

def login(request):
    return render(request, 'login.html')


# @login_required(login_url='/login')
def basicDetailsView(request):
    
    # user_email = request.user.email
    all_items = basicDetailsItems.objects.all()
    return render(request, 'basicDetails.html',  {'all_items':all_items})

def requirementsView(request):

    all_items = reqItems.objects.all()
    return render(request, 'requirements.html',{'all_items':all_items})
