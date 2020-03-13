import json

import requests


class BaseAPI:

    def __init__(self):
        self.__api_url_base = 'https://restcountries.eu/rest/v2/'

    def connect(self):
        api_url = self.__api_url_base
        response = requests.get(api_url)

        if response.status_code == 200:
            return True
        else:
            return False

    def get_country_info(self, cat, keys):
        api_url = self.__api_url_base + cat + '/' + keys
        response = requests.get(api_url)

        if response.status_code == 200:
            return json.loads(response.content)
        else:
            return None
