from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse("<h2>Hello, world</h1> You're at the Kisan Portal")

def dummy(request, id):
    a = str(type(id))
    a = a[1:-1]
    return HttpResponse(f"<h3>You Choose: TYPE:{a} </h3> <h1>\t%s</h1"%id)