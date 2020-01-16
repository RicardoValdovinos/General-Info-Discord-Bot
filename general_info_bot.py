"""Discord bot."""
import json
import discord
from open_weather_map import OpenWeatherMapAPI

CLIENT = discord.Client()
WEATHER_API = OpenWeatherMapAPI()


def read_auth_token():
    """reads credentials from file."""
    with open('auth.json', 'r') as token:
        credentials = json.load(token)
    return credentials


@CLIENT.event
async def on_ready():
    print('We have logged in as {0.user}'.format(CLIENT))


@CLIENT.event
async def on_message(message):
    if message.author == CLIENT.user:
        return

    if message.content.startswith('!weather'):
        msg = message.content.split(' ')
        await message.channel.send(await WEATHER_API.get_weather(msg))


CLIENT.run(read_auth_token()['discord_auth_token'])
