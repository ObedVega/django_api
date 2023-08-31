import httpx
from bs4 import BeautifulSoup
import asyncio
from urllib.parse import urlparse, urlunparse

async def check_broken_links_async(session, url):
#    async with httpx.AsyncClient() as session:
        try:
            print(url)
            response = await session.get(url)
            #if response.status_code != 200:
            return response.status_code  # Devuelve el código de estado
            #else:
            #    return "ok"
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
#            print(links)
            tasks = []
            urls = [link.get("href") for link in links if link.get("href") and link.get("href").startswith("https")]
        #    urls = [link.get("href") for link in links if link.get("href") and link.get("href")]
        #    print(urls)
            for url in urls:
                print(url)
                tasks.append(check_broken_links_async(session, url))

            results = await asyncio.gather(*tasks)
#            print(results)
            for url, status in zip(urls, results):
#                print(url)
                if status == 404:
                    link_data = {"ruta": url, "status": status}
                    links_data.append(link_data)
        else:
            print("Error al obtener la página:", response.status_code)

    return links_data

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

async def revisa_imagenes(main_url):
    async with httpx.AsyncClient() as session:
        response = await session.get(main_url)

        if response.status_code == 200:
            soup = BeautifulSoup(response.text, "html.parser")
            img_tags = soup.find_all('img')    
            imagenes_sin_atributos = []

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
#                if not alt_attr:
#                    print(f"La imagen sin atributo 'alt': {img_tag}")
                
#                if not title_attr:
#                    print(f"La imagen sin atributo 'title': {img_tag['src']}")

    #    cantidad_imagenes = len(img_tags)
    return imagenes_sin_atributos