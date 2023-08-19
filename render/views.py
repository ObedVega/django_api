from django.shortcuts import render
import json
from django.http import HttpResponse
from .utils import obtiene_link

# Create your views here.
def index(request):
    return render(request, 'render/index.html', {})

def check(request):
    resultado = obtiene_link('https://quickstarts.teradata.com/tools-and-utilities/run-bulkloads-efficiently-with-teradata-parallel-transporter.html')
    json_string = json.dumps(resultado)

    return HttpResponse(json_string, content_type='application/json')
    #return render(request, respuesta)

'''
def check(request):
    response_data = obtiene_link('https://quickstarts.teradata.com/tools-and-utilities/run-bulkloads-efficiently-with-teradata-parallel-transporter.html')
    
    json_data = json.dumps(response_data)
    #respuesta = [{'nombre': 'Obed'}]

    return HttpResponse(request, json_data)
    #return render(request, respuesta)
    #return JsonResponse(json_data, safe=False)
'''    