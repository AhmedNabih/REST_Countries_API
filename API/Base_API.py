import json
import requests


class BaseAPI:

    def __init__(self):
        self.__api_url_base = 'https://restcountries.eu/rest/v2/name/'

    def get_country_info(self, country, cat):
        if type(country) is not str:
            return None
        if type(cat) is not str:
            return None
        api_url = self.__api_url_base + country
        try:
            response = requests.get(api_url)
            if response.status_code == 200:
                if response.from_cache:
                    print("from cache")
                return json.loads(response.content)[0][str(cat)]
            else:
                return None
        except:
            return None
