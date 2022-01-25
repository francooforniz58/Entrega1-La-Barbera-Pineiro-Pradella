from django.shortcuts import render
from django.http import HttpResponse
from appBandmates.models import *

def inicio(request):

    return render(request, "appBandmates/inicio.html")
