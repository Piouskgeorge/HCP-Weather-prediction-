import requests

def fetch_weather(city):
    url = f"addd your website URL"
    response = requests.get(url)
    data = response.json()
    weather = data['current_weather']
    return (city[0], weather['temperature'], 60, weather['windspeed'])  # Dummy humidity as API doesn't provide it
