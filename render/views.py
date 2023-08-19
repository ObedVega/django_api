from django.http.response import JsonResponse
from django.shortcuts import render
import json
from django.http import HttpResponse
from .utils import obtiene_link

# Create your views here.
def index(request):
    return render(request, 'render/index.html', {})

#@api_view(['GET'])
def check(request):
    resultado = obtiene_link('https://quickstarts.teradata.com/tools-and-utilities/run-bulkloads-efficiently-with-teradata-parallel-transporter.html')
    
    #respuesta = [{'nombre': 'Obed'}]
    json_string = json.dumps(resultado)
    #return HttpResponse(request, json_string)
    #return render(request, respuesta)
    return JsonResponse(json_string, safe=False)