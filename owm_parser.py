import requests
import sys


def parse_weather(cmd):
    if cmd[0] == '!weather':
        cmd.remove('!weather')
        return parse_location(cmd)
    else:
        syntax_error()


def parse_location(cmd):
    if cmd[0].isdigit():
        if len(cmd) == 2:
            if cmd[1].isdigit():
                return parse_coordinates(cmd)
            else:
                return parse_zip_code_country_code(cmd, cmd[1])
        if len(cmd) == 1:
            return parse_zip_code(cmd)
    else:
        if len(cmd) == 2:
            return parse_city_name_country_code(cmd)
        else:
            return parse_city(cmd)


def parse_zip_code(zip_code):
    return '?zip=' + zip_code


def parse_zip_code_country_code(zip_code, country_code):
    if country_code.isdigit():
        syntax_error()
    return parse_zip_code(zip_code) + ',' + country_code


def parse_city(city_name):
    full_city_name = ''
    for city in city_name:
        if not city.isdigit():
            full_city_name = full_city_name + city + ' '
        else:
            syntax_error()
    return '?q=' + full_city_name


def parse_city_name_country_code(cmd):
    full_city_name = ''
    for city in city_name:
        if not city.isdigit():
            full_city_name = full_city_name + city + ' '
        else:
            syntax_error()


def parse_coordinates(coords):
    return '?lat=' + coords[0] + '&lon=' + coords[1]


def syntax_error():
    print('SYNTAX ERROR!')
    sys.exit()
