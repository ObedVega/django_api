#from rest_framework.decorators import api_view, permission_classes
from django.shortcuts import render
import json
from django.http import HttpResponse, JsonResponse
from .utils import valida_url, obtiene_links, revisa_imagenes
import requests
import pymongo
from django.views.decorators.http import require_POST

# Configura la conexión a MongoDB
client = pymongo.MongoClient('mongodb+srv://saldi:Saldi_1.0@saldi.y8swx.mongodb.net/bustedweb?retryWrites=true&w=majority')
db = client['bustedweb']
collection = db['locations'] 

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


async def datos(request, api, ip, ciudad, estado, pais, loc):
    print("LLEGE1")
    print(api, ip, ciudad, estado, pais, loc)
    print("LLEGE2")

    print("LLEGE3")
  
    print("LLEGE4")
    # Datos a insertar
    api = api
    ip = ip
    ciudad = ciudad
    estado = estado
    pais = pais
    loc = loc
    print("LLEGE5")

    # Crear un documento
    documento = {
        "api": api,
        "ip": ip,
        "ciudad": ciudad,
        "estado": estado,
        "pais": pais,
        "loc": loc
    }
    print("LLEGE6")
    # Insertar el documento en la colección
    resultado = collection.insert_one(documento)
 
    print("LLEGE7")
    if resultado.inserted_id:
        print(f"Documento insertado con ID: {resultado.inserted_id}")
    else:
        print("La inserción falló")

#        registro = f"{ciudad}, {estado}, {pais}\n"

#        db = connections['default'].get_database()
#        db = client['nombre_de_tu_base_de_datos']
#    archivo_txt = 'registros.txt'
#    with open(archivo_txt, 'a') as archivo:
#        archivo.write(registro)
    
#    resultado = []

#    respuestaVacia = {"ok": "ok"}
#    resultado.append(respuestaVacia)

#    json_string = json.dumps(resultado)
#    return HttpResponse(json_string, content_type='application/json')  
    return HttpResponse("OK", content_type="text/plain", status=200)

def consultar_archivo(request):
    client = pymongo.MongoClient('mongodb+srv://saldi:Saldi_1.0@saldi.y8swx.mongodb.net/bustedweb?retryWrites=true&w=majority')
    db = client['bustedweb']
    collection = db['locations'] 
#    try:
        # Ruta al archivo de texto que deseas consultar
#        archivo_txt = 'registros.txt'

        # Abre el archivo en modo lectura y lee su contenido
#        with open(archivo_txt, 'r') as archivo:
#            contenido = archivo.read()

        # Devuelve el contenido como respuesta HTTP
#        return HttpResponse(contenido, content_type='text/plain')
#    except Exception as e:
        # En caso de error, devuelve una respuesta JSON de error
#        return JsonResponse({'error': str(e)})
    # Conecta a la base de datos MongoDB configurada en settings.py


    # Realiza la consulta MongoDB
    resultados = list(collection.find({}))

    for resultado in resultados:
        resultado['_id'] = str(resultado['_id'])
    # Cierra la conexión a MongoDB
    client.close()

    # Convierte los resultados a una lista de diccionarios JSON
#    resultados_json = [resultado for resultado in resultados]

    # Devuelve los resultados como una respuesta JSON
    return JsonResponse(resultados, safe=False)

def db_connect():
    """
    Función para conectar a la base de datos MongoDB y obtener la colección 'usuarios'.
    """
    # Conexión a la base de datos
    client = pymongo.MongoClient('mongodb+srv://saldi:Saldi_1.0@saldi.y8swx.mongodb.net/saldi_shop?retryWrites=true&w=majority')
    db = client['saldi_shop']
    collection = db['usuarios']
    
    return collection

@require_POST
async def registro(request):
    try:
        collection = db_connect()

        if 'email' in request.POST and 'password' in request.POST:
            email = request.POST['email']
            password = request.POST['password']

            new_user = {
                    'email': email,
                    'password': password
                }
            collection.insert_one(new_user)
            
            return JsonResponse({'message':'Usuario creado correctamente'}, status=201)
        else:
            return JsonResponse({'error': 'Se requieren email y contraseña en la solicitud'}, status=400)
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=500)