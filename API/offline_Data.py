import json


class OfflineData:

    def __init__(self, path):
        self.__json_file = None
        self.data = None
        self.__FilePath = path

    def OpenFile(self):
        try:
            self.__json_file = open(self.__FilePath, "r", encoding="utf8")
        except:
            raise OSError

    def CloseFile(self):
        self.__json_file.close()

    def LoadFile(self):
        try:
            self.data = json.load(self.__json_file)
        except:
            raise OSError

    def GetData(self, countryName):
        for i in self.data:
            if i["name"].lower() == countryName.lower():
                return i
        return None
