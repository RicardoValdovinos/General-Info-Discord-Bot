"""Open Weather Map Api"""
from typing import Dict
import requests
import json


API = 'https://api.openweathermap.org/data/2.5/weather'


class OpenWeatherMapAPI:
    """OpenWeatherMapAPI"""

    def __init__(self, api_key):
        self.api_key = api_key

    async def get_weather(self, location: Dict[str, str]):
        """gets weather from api"""
        if location[1].isdigit():
            zip_code = location[1]
            return requests.get(API + '?zip=' + zip_code + '&APPID=' +
                                self.api_key).text
        else:
            city_name = location[1]
            return requests.get(API + '?q=' + city_name + '&APPID=' +
                                self.api_key).text
        return 'nothing'
