"""Discord bot."""
import json


def read_credentials(filename):
    """reads credentials from file."""
    with open(filename, 'r') as token:
        credentials = json.load(token)
    return credentials


C = read_credentials('auth.json')
print(C)
