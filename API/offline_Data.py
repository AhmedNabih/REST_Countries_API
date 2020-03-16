import json


class OfflineData:
    FilePath = "offline_data/countriesData.json"
    data = None

    def __init__(self):
        self.__json_file = None
        self.OpenFile()
        self.LoadFile()
        self.CloseFile()

    def OpenFile(self):
        try:
            self.__json_file = open(self.FilePath, "r", encoding="utf8")
        except IOError:
            print("File Opening Error")

    def CloseFile(self):
        self.__json_file.close()

    def LoadFile(self):
        self.data = json.load(self.__json_file)

    def GetData(self, countryName):
        for i in self.data:
            if i["name"].lower() == countryName.lower():
                return i
        return None
