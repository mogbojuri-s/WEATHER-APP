from flask import Flask, render_template, request
import requests

app = Flask(__name__)

WEATHER_API_KEY = '276dcad5626166ccd09af29c96fdec39'
BASE_URL = 'https://api.openweathermap.org/data/2.5/weather'

def get_weather(city):
    params = {'appid': WEATHER_API_KEY, 'q': city, 'units': 'imperial'}
    response = requests.get(BASE_URL, params=params)
    return response.json()

def format_response(weather):
    try:
        if weather.get('cod') != 200:
            return 'City not found or API error', None

        city = weather['name']
        condition = weather['weather'][0]['description']
        temp = weather['main']['temp']
        icon = weather['weather'][0]['icon']
        weather_info = f'City: {city}\nCondition: {condition}\nTemperature: {temp}°F'
        return weather_info, icon
    except Exception as e:
        return f'There was a problem retrieving that information: {e}', None

@app.route('/', methods=['GET', 'POST'])
def index():
    weather_info = ""
    weather_icon = ""
    if request.method == 'POST':
        city = request.form.get('city')
        if city:
            weather, icon = get_weather(city), get_weather(city)['weather'][0]['icon']
            weather_info, weather_icon = format_response(weather)
            weather_icon = icon
        else:
            weather_info = 'Please enter a city name.'
    return render_template('index.html', weather_info=weather_info, weather_icon=weather_icon)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080, debug=True)
