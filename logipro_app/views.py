from django.shortcuts import render
from .models import logiProItems 
from django.http import HttpResponseRedirect 

from django.contrib.auth.decorators import login_required

def index(request):
    return render(request, 'index.html')