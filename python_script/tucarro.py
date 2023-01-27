# CODIGO BASE: https://www.youtube.com/watch?v=RvCBzhhydNk

#PROBLEMA #1: NO ME DEJABA INSTALAR REQUESTS POR PERMISOS---> SOLUCION: COPIAR pip install pip-run --user
# SOLUCION ENCONTRADA EN: https://github.com/pypa/pip/issues/9023

from bs4 import BeautifulSoup
import requests
import json

url = "https://carros.tucarro.com.co/"
page = requests.get(url)
soup = BeautifulSoup(page.content, "html.parser")
lists = soup.find_all('div', class_="ui-search-result__wrapper")

def get_data(list):
    car_list = []
    car_info = {}
    with open('db.json', 'w', encoding='utf8', newline='') as f:
        for list in lists:
            title = list.find('h2', class_="ui-search-item__title").text
            location = list.find('span', class_="ui-search-item__location").text
            price= list.find('span', class_="price-tag-text-sr-only").text.replace('pesos', '')
            cosos = list.find_all('li', class_="ui-search-card-attributes__attribute")
            anio = cosos[0].text
            kilometraje = cosos[1].text
            remove = [' ', 'km', 'Km', '.']
            for i in remove:
                kilometraje = kilometraje.replace(i, '')
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
        json.dump(cars, f, ensure_ascii=False, indent=4)
get_data(lists)

