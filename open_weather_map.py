"""Open Weather Map Api"""
import requests
import json
import owm_parser

API = 'https://api.openweathermap.org/data/2.5/weather'


class OpenWeatherMapAPI:
    """OpenWeatherMapAPI"""

    def __init__(self, api_key):
        self.api_key = api_key

    async def get_weather(self, weather):
        """gets weather from api"""
        return requests.get(API + owm_parser.parse_weather(weather) + '&APPID=' + self.api_key).text
