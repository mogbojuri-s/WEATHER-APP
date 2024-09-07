from flask import Flask, render_template, request
import requests

app = Flask(__name__)

# Replace 'YOUR_API_KEY' with your actual OpenWeatherMap API key
WEATHER_API_KEY = '276dcad5626166ccd09af29c96fdec39'
BASE_URL = 'https://api.openweathermap.org/data/2.5/weather'

def get_weather(city):
    params = {'appid': WEATHER_API_KEY, 'q': city, 'units': 'imperial'}
    response = requests.get(BASE_URL, params=params)
    return response.json()

def format_response(weather):
    try:
        if weather.get('cod') != 200:
            return 'City not found or API error'

        city = weather['name']
        condition = weather['weather'][0]['description']
        temp = weather['main']['temp']
        return f'City: {city}\nCondition: {condition}\nTemperature: {temp}°F'
    except Exception as e:
        return f'There was a problem retrieving that information: {e}'

@app.route('/', methods=['GET', 'POST'])
def index():
    weather_info = ""
    if request.method == 'POST':
        city = request.form.get('city')
        if city:
            weather = get_weather(city)
            weather_info = format_response(weather)
        else:
            weather_info = 'Please enter a city name.'
    return render_template('index.html', weather_info=weather_info)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080, debug=True)

