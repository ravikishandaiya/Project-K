from django.http import HttpResponse
import json

def basic(request):
    response_data = {'APP': 'Kisan App','Function': 'basic data', 'desc': 'test api for getting basic data', 'supported methods': 'GET'}
    
    return HttpResponse(json.dumps(response_data), content_type="application/json")
