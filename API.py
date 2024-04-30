import requests
import json

API_KEY = "26e1733cea604488a77134653231301"

def weather_info(city):
    url = f"http://api.weatherapi.com/v1/forecast.json?key={API_KEY}&q={city}&days=1&aqi=yes&alerts=no"
    responce = requests.get(url)
    data = responce.json()

    city = data["location"]["name"]
    country = data["location"]["country"]
    current_weather = data["current"]["condition"]["text"]
    updated = data["current"]["last_updated"]
    temp = data["current"]["temp_c"]
    maxtemp_c = data["forecast"]['forecastday'][0]['day']['maxtemp_c']
    min_temp = data["forecast"]["forecastday"][0]["day"]["mintemp_c"]
    average_temp = data["forecast"]["forecastday"][0]["day"]["avgtemp_c"]
    sunrise = data["forecast"]["forecastday"][0]["astro"]["sunrise"]
    sunset = data["forecast"]["forecastday"][0]["astro"]["sunset"]
    moonrise = data["forecast"]["forecastday"][0]["astro"]["moonrise"]
    moonset = data["forecast"]["forecastday"][0]["astro"]["moonset"]
    moonphase = data["forecast"]["forecastday"][0]["astro"]["moon_phase"]
    wind = data['current']['wind_kph']
    humidity = data['current']['humidity']

    return(f"In <strong>{city}</strong>, {country}, the current temperature is <strong>{temp}</strong> °C, with <strong>{current_weather}</strong>.\n\nThe maximum temperature today is <strong>{maxtemp_c}</strong> °C and the minimum temperature today is <strong>{min_temp}</strong> °C.\n\nThe average temperature stands at <strong>{average_temp}</strong> °C with <strong>{humidity}</strong> % humidity.")
