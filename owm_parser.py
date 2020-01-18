import requests
import sys


def parse_weather(cmd):
    if cmd[0] == '!weather':
        cmd.remove('!weather')
        return parse_location(cmd)


def parse_location(cmd):
    if cmd[0].isdigit() or is_float(cmd[0]):
        if len(cmd) == 2:
            if cmd[1].isdigit() or is_float(cmd[1]):
                print(cmd[1])
                return parse_coordinates(cmd)
            print('here')
            return parse_zip_code_country_code(cmd)
        if len(cmd) == 1:
            return parse_zip_code(cmd)
    else:
        return parse_city_name_country_code(cmd)


def parse_zip_code(zip_code):
    return '?zip=' + zip_code


def parse_zip_code_country_code(cmd):
    return parse_zip_code(cmd[0]) + cmd[1]


def parse_city(city_name):
    full_city_name = ''
    for city in city_name:
        if not city.isdigit():
            full_city_name = full_city_name + city + ' '
    return '?q=' + full_city_name


def parse_city_name_country_code(cmd):
    full_city_name = ''
    is_city = True
    country_code = ''
    for param in cmd:
        if is_city:
            if not param.isdigit():
                if param.find(',') == -1:
                    full_city_name = full_city_name + param + ' '
                else:
                    param.replace(',', '')
                    full_city_name = full_city_name + param + ' '
                    is_city = False
        else:
            country_code = param
    if not is_city:
        return '?q=' + full_city_name + country_code
    return '?q=' + full_city_name


def parse_coordinates(coords):
    print('?lat=' + coords[0] + '&lon=' + coords[1])
    return '?lat=' + coords[0] + '&lon=' + coords[1]


def is_float(string):
    try:
        float(string)
        return True
    except ValueError:
        return False
