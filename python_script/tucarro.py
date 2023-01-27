# CODIGO BASE: https://www.youtube.com/watch?v=RvCBzhhydNk

#PROBLEMA #1: NO ME DEJABA INSTALAR REQUESTS POR PERMISOS---> SOLUCION: COPIAR pip install pip-run --user
# SOLUCION ENCONTRADA EN: https://github.com/pypa/pip/issues/9023

from bs4 import BeautifulSoup
import requests
from csv import writer
import json

url = "https://carros.tucarro.com.co/"
page = requests.get(url)
soup = BeautifulSoup(page.content, "html.parser")
lists = soup.find_all('div', class_="ui-search-result__wrapper")
car_list = []
car_info = {}


with open('tucarro.json', 'w', encoding='utf8', newline='') as f:
    thewriter = writer(f)
    header = ['model', 'location', 'price', 'year', 'km']
    thewriter.writerow(header)
    for list in lists:
        title = list.find('h2', class_="ui-search-item__title").text
        location = list.find('span', class_="ui-search-item__location").text
        price= list.find('span', class_="price-tag-text-sr-only").text
        price = price.replace('pesos', '')
        cosos = list.find_all('li', class_="ui-search-card-attributes__attribute")
        anio = cosos[0].text
        kilometraje = cosos[1].text
        kilometraje = kilometraje.replace('km', '')
        kilometraje = kilometraje.replace('Km', '')
        kilometraje = kilometraje.replace(' ', '')
        kilometraje = kilometraje.replace('.', '')
        info = [location, price,anio, kilometraje]
        car_info = {
            'model': title,
            'location': info[0],
            'price': int(info[1]),
            'year': info[2],
            'km': int(info[3])
        }
        car_list.append(car_info)

cars = {"cars": car_list}

with open('tucarro.json', 'w', encoding='utf8') as f:
    json.dump(cars, f, ensure_ascii=False, indent=4)
