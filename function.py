
#https://api.openweathermap.org/

import requests
from bs4 import BeautifulSoup as BS
import json

#function for weather
def weather(city:str):
    city.replace(" ", "%20")
    city.replace("-", "%20")

    token_weather = 'TOKEN'# your token weather home.openweathermap.org

    url = requests.get(f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={token_weather}')
    parser = BS(url.content, "html.parser")

    json_url = json.loads(str(parser))

    city = json_url['name']
    temp = round(json_url['main']['temp'] - 273.15)
    weather = json_url["weather"][0]['main']
    # print(json_url)
    dict1 = [city, temp, weather]
    return dict1