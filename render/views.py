from django.shortcuts import render
import json
from django.http import HttpResponse
from urllib.parse import unquote
from .utils import obtiene_links

# Create your views here.
def index(request):
    return render(request, 'render/index.html', {})

async def check(request, url):
    decoded_param = unquote(url) 
    print(decoded_param)
    
    resultado = await obtiene_links('https://quickstarts.teradata.com/tools-and-utilities/run-bulkloads-efficiently-with-teradata-parallel-transporter.html')
    #resultado = [{'nombre': decoded_param}]
    url = "https://quickstarts.teradata.com/tools-and-utilities/run-bulkloads-efficiently-with-teradata-parallel-transporter.html"
    #resultado = await obtiene_links(url)
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