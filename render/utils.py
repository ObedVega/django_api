import httpx
from bs4 import BeautifulSoup
import asyncio

async def check_broken_links_async(session, url):
    async with httpx.AsyncClient() as session:
        try:
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
            
            tasks = []
            urls = [link.get("href") for link in links if link.get("href") and link.get("href").startswith("https")]
            for url in urls:
                tasks.append(check_broken_links_async(session, url))

            results = await asyncio.gather(*tasks)

            for url, status in zip(urls, results):
                link_data = {"ruta": url, "status": status}
                links_data.append(link_data)
        else:
            print("Error al obtener la página:", response.status_code)

    return links_data
