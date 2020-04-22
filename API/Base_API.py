import json
import requests


class BaseAPI:

    def __init__(self):
        self.__api_url_base = 'https://restcountries.eu/rest/v2/name/'

    def callAPI(self):
        api_url = self.__api_url_base + "egypt"
        response = requests.get(api_url)
        return response.status_code == 200

    def get_country_info(self, country, cat):
        if type(country) is not str:
            return None, None
        if type(cat) is not str:
            return None, None
        api_url = self.__api_url_base + country
        try:
            response = requests.get(api_url)
            if response.status_code == 200:
                if response.from_cache:
                    print("from cache")
                return json.loads(response.content)[0][str(cat)], response.from_cache
            else:
                return None, None
        except:
            return None, None
