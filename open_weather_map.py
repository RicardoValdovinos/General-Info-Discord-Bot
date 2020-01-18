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

    def help_menu(self):
        return '''
    ```Hello!

    If you want to use the !weather command make sure to use it as shown
    below:
        !weather <zip_code>
        !weather <zip_code>, <country_code>
        !weather <city_name>
        !weather <city_name>, <country_code>
        !weather <latitude> <longitude>

    Examples:
        !weather 85032 
        !weather 85032, US
        !weather phoenix
        !weather phoenix, US
        !weather 33 -112 

    Use ISO 3166 country codes. You can find country codes here: https://www.iso.org/obp/ui/#search

    ```
    '''
