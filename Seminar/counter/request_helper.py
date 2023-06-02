import requests
import json

from classes import Location

__all__ = ['get_location_from_name']


def get_location_from_name(name):
    endpoint = f"https://geocode.maps.co/search?q={name}"
    response = requests.get(endpoint)
    data = json.loads(response.text)[0]

    lat, lon = data['lat'], data['lon']
    return Location(lat, lon)
