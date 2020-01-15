"""Discord bot."""
import json


def read_credentials():
    """reads credentials from file."""
    with open('auth.json', 'r') as token:
        credentials = json.load(token)
    return credentials


C = read_credentials()
print(C)
