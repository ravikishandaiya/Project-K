from django.shortcuts import render
from rest_framework.decorators import api_view

from django.http import HttpResponse
from rest_framework.response import Response
import json


# Create your views here.
def index(request):
    return render(request, 'Kisan_App/index.html')
    
def temp(request):
    return render(request, 'Kisan_App/Agri.html')