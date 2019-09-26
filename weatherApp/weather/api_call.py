import requests
from django.core.cache import cache, caches
from rest_framework import status

from django.conf import settings

TWENTY_FOUR_HOURS = 60 * 60 * 24


def get_weather_data(city):
    """Make an http request to weather api"""
    url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={settings.APIKEY}'
    # check if the city has data in the cache

    # else get the data from the weather api
    try:
        cached_data = cache.get(city)
        if cached_data:
            return {"status": status.HTTP_200_OK, "data": cached_data.json()}
        else:
            response = requests.get(url)
            if response.status_code == 200:
                cache.set(city, response.json(), timeout=TWENTY_FOUR_HOURS)
        return {"status": response.status_code, "data": response.json()}
    except Exception as e:
        print("Error: ", e)
        return {"status": response.status_code, "data": e}





