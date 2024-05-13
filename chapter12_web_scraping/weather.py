#! python3
# Usage: Usage: python script.py <city>,<country_code>,<state_code>
# where <city> is the name of a City for which weather condition the user
# wants information, <country_code> is the code of the country like "Fr" or "Br"
# for France or Brazil, respectively, <state_code> is the international code of the
# state, like for example 11 for São Paulo, Brazil.
# The program opens up the openwather page for the city chosen and also prints some
# information on the screen.
# Exits something different from 4 arguments are passed.

import sys
import webbrowser
import urllib.parse
import requests

def search_city_url(city, country_code, state_code):
    api_key = ''
    city_name = urllib.parse.quote(city)
    state_code = urllib.parse.quote(state_code)
    country_code = urllib.parse.quote(country_code)
    base_url = f'http://api.openweathermap.org/geo/1.0/direct?q={city_name},{country_code},{state_code}&limit=5&appid={api_key}'
    return base_url

def get_weather_url(lat, lon):
    api_key = 'a59ef00805e9c5a293dbd4127301960d'
    city_lat = urllib.parse.quote(str(lat))
    city_lon = urllib.parse.quote(str(lon))
    base_url = f'https://api.openweathermap.org/data/2.5/weather?lat={city_lat}&lon={city_lon}&appid={api_key}'
    return base_url

def open_local_weather(lat, lon):
    url = get_weather_url(lat, lon)
    webbrowser.open(url)


if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: python script.py <city>,<country_code>,<state_code>")
        sys.exit(1)
    
    city = sys.argv[1]
    country_code = sys.argv[2]
    state_code = sys.argv[3]

    city_url = search_city_url(city, country_code, state_code)

    res = requests.get(city_url)
    data = res.json()

    lat = data[0]['lat']
    lon = data[0]['lon']

    open_local_weather(lat, lon)

    weather_data = get_weather_url(lat, lon)
    weather_data = requests.get(weather_data)
    weather_data = weather_data.json()

    humidity = weather_data['main']['humidity']
    pressure = weather_data['main']['pressure']
    wind = weather_data['wind']['speed']
    description = weather_data['weather'][0]['description']
    temp = weather_data['main']['temp']
    temp = temp - 273.15

    print('Temperature:',temp,'°C')
    print('Wind:',wind)
    print('Pressure: ',pressure)
    print('Humidity: ',humidity)
    print('Description:',description)
