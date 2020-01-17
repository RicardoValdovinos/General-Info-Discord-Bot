"""Discord bot."""
import json
import discord
from open_weather_map import OpenWeatherMapAPI


def read_auth_token():
    """reads credentials from file."""
    with open('auth.json', 'r') as token:
        credentials = json.load(token)
    return credentials


CLIENT = discord.Client()
WEATHER_API = OpenWeatherMapAPI(read_auth_token()['open_weather_api_key'])


@CLIENT.event
async def on_ready():
    print('We have logged in as {0.user}'.format(CLIENT))


@CLIENT.event
async def on_message(message):
    if message.author == CLIENT.user:
        return

    if message.content.startswith('!weather'):
        msg = message.content.split(' ')
        if len(msg) == 1:
            await message.channel.send(help_menu())
        else:
            if msg[1] == 'help':
                await message.channel.send(help_menu())
            else:
                await message.channel.send(await WEATHER_API.get_weather(msg))


def help_menu():
    return '''
```Hello!

If you want to use the !weather command make sure to use it as shown
below:
    !weather <zip_code>
    !weather <city_name>
    !weather <latitude> <longitude>

Examples:
    !weather 85032 
    !weather phoenix
    !weather 33 -112 
```
'''


CLIENT.run(read_auth_token()['discord_auth_token'])
