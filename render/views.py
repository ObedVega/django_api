from django.shortcuts import render
import json
from django.http import HttpResponse
from .utils import valida_url
from .utils import obtiene_links

# Create your views here.
def index(request):
    return render(request, 'render/index.html', {})

async def check(request, url):

    newURL = await valida_url(url)
    print(newURL)
    resultado = await obtiene_links(newURL)
    #https://quickstarts.teradata.com/tools-and-utilities/run-bulkloads-efficiently-with-teradata-parallel-transporter.html 
    if resultado == "":
        resultado = {"ruta": "We didn't find broken links", "status": "0"}
    json_string = json.dumps(resultado)

    return HttpResponse(json_string, content_type='application/json')
