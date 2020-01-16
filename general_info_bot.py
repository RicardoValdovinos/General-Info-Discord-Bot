"""Discord bot."""
import json
import discord


CLIENT = discord.Client()


def read_credentials():
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
        await message.channel.send(f'{msg[1]}')


CLIENT.run(read_credentials()['discord_auth_token'])
