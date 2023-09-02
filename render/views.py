#from rest_framework.decorators import api_view, permission_classes
from django.shortcuts import render
import json
from django.http import HttpResponse
from .utils import valida_url, obtiene_links, revisa_imagenes
import requests

def index(request):
    return render(request, 'render/index.html', {})

#@api_view(['GET'])
async def check(request, url):
 
    newURL = await valida_url(url)
 
    rnewURL = requests.head(newURL, allow_redirects=True)
  
    resultado = await obtiene_links(rnewURL.url)

    #https://quickstarts.teradata.com/tools-and-utilities/run-bulkloads-efficiently-with-teradata-parallel-transporter.html 
    
    if not resultado:
        respuestaVacia = {"ruta": "We didn't find broken links", "status": "0"}
        resultado.append(respuestaVacia)

    json_string = json.dumps(resultado)

    return HttpResponse(json_string, content_type='application/json')

#Revisa Imagenes
async def check_img(request, main_url):
    ip = request.remote_addr
    #print(ip)
    newURL = await valida_url(main_url)
    rnewURL = requests.head(newURL, allow_redirects=True)

    resultado = await revisa_imagenes(rnewURL.url)
    #print(resultado)

    #respuestaVacia = {"cantidad": resultado}
#    resultado.append(respuestaVacia)
# json_data = json.dumps(imagenes_sin_atributos, indent=4)
#    print(len(resultado))
    json_string = json.dumps(resultado)
    return HttpResponse(json_string, content_type='application/json') 

async def datos(request, ciudad, estado, pais):
    print(ciudad, estado, pais)
    print(estado)
    print(pais)

    resultado = []

    respuestaVacia = {"ok": "ok"}
    resultado.append(respuestaVacia)

    json_string = json.dumps(resultado)
    return HttpResponse(json_string, content_type='application/json') 