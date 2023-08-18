import requests
from bs4 import BeautifulSoup

def obtiene_link(url):
    response = requests.get(url)
    n=0
    link_status = ""
    links_data = []

    if response.status_code == 200:
        soup = BeautifulSoup(response.text, "html.parser")
        
        links = soup.find_all("a")
        for link in links:
            ruta = link.get("href")
            if ruta is not None and ruta.startswith("https"):    
                n+=1
                link_status = check_broken_links(ruta)
                link_data = {"ruta": ruta, "status": link_status}
                links_data.append(link_data)
    else:
        print("Error al obtener la página:", response.status_code)

    return links_data

def check_broken_links(url):
    res=""
    response = requests.get(url)
    try:
        if response.status_code != 200:
            res = "Broken"
        else:
            res = "Good"
    except Exception as e:
        print(f"An error occurred: {e}")
    return res
