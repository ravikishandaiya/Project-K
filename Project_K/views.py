from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse("<h2>Hello, world</h1> You're at the index Page.")
