import httpx
from bs4 import BeautifulSoup
import asyncio
from urllib.parse import urlparse, urlunparse

async def check_broken_links_async(session, url):
        try:
            response = await session.get(url)
            return response.status_code

        except Exception as e:
            print(f"An error occurred: {e}")
            return "broken"

async def obtiene_links(url):
    async with httpx.AsyncClient() as session:
        response = await session.get(url)
        links_data = []

        if response.status_code == 200:
            soup = BeautifulSoup(response.text, "html.parser")
            links = soup.find_all("a")
            tasks = []
            urls = [link.get("href") for link in links if link.get("href") and link.get("href").startswith("https")]

            for url in urls:
                print(url)
                tasks.append(check_broken_links_async(session, url))

            results = await asyncio.gather(*tasks)
            for url, status in zip(urls, results):
                if status == 404:
                    link_data = {"ruta": url, "status": status}
                    links_data.append(link_data)
        else:
            print("Error al obtener la página:", response.status_code)

    return links_data

#Funcion para validar el link
async def valida_url(url):
    # Si no empieza con "http://" ni "https://", asumimos que es un subdominio
    if not url.startswith(("http://", "https://")):
        url = "https://" + url

    # Parseamos el URL para asegurarnos de que esté bien formateado
    parsed_url = urlparse(url)

    # Si el esquema es "http://", lo cambiamos a "https://"
    if parsed_url.scheme == "http":
        parsed_url = parsed_url._replace(scheme="https")

    # Volvemos a construir el URL en su forma normalizada
    normalized_url = urlunparse(parsed_url)

    return normalized_url

#Funcion para revisar imagenes
async def revisa_imagenes(main_url):
    async with httpx.AsyncClient() as session:
        response = await session.get(main_url)
        imagenes_sin_atributos = []
        
        print(response.status_code)
        if response.status_code == 200:
            soup = BeautifulSoup(response.text, "html.parser")
            img_tags = soup.find_all('img')    

            for img_tag in img_tags:
                alt_attr = img_tag.get('alt')
                title_attr = img_tag.get('title')

                if not alt_attr or not title_attr:
                    imagen = {
                        "src": img_tag.get('src'),
                        "alt": alt_attr,
                        "title": title_attr
                    }
                    imagenes_sin_atributos.append(imagen)

    return imagenes_sin_atributos