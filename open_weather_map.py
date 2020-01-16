"""Open Weather Map Api"""
from typing import Dict
import requests
import json


API = 'https://api.openweathermap.org/data/2.5/weather'


def read_api_key():
    """reads credentials from file."""
    with open('auth.json', 'r') as token:
        credentials = json.load(token)
    return credentials


API_KEY = read_api_key()["open_weather_api_key"]


class OpenWeatherMapAPI:
    """OpenWeatherMapAPI"""
    async def get_weather(self, location: Dict[str, str]):
        """gets weather from api"""
        if len(location) == 2:
            if location[1].isdigit():
                zip_code = location[1]
                return requests.get(API + '?zip=' + zip_code + '&APPID=' +
                                    API_KEY).text
            else:
                city_name = location[1]
                return requests.get(API + '?q=' + city_name + '&APPID=' +
                                    API_KEY).text
        return 'nothing'
