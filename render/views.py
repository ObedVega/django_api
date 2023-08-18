from django.shortcuts import render
import json
from django.http import HttpResponse
from .utils import obtiene_link

# Create your views here.
def index(request):
    return render(request, 'render/index.html', {})

def check(request):
    resultado = obtiene_link('https://quickstarts.teradata.com/tools-and-utilities/run-bulkloads-efficiently-with-teradata-parallel-transporter.html')
    
    #respuesta = [{'nombre': 'Obed'}]
    json_string = json.dumps(resultado)
    return HttpResponse(json_string)
    #return render(request, respuesta)