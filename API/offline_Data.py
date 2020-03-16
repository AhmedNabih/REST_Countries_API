import json


class OfflineData:
    def __init__(self):
        self.__json_file = open("offline_data/countriesData.json", "r", encoding="utf8")
        self.__data = json.load(self.__json_file)
        self.__json_file.close()
        print("ok")

    def GetData(self, countryName):
        res = None
        for i in self.__data:
            if i["name"].lower() == countryName.lower():
                return i
        return None
