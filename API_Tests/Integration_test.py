import json
import unittest

from flask import jsonify, Flask
from mock import patch, Mock

from API.Base_API import BaseAPI
from API.offline_Data import OfflineData


class Integration(unittest.TestCase):

    def test_RunIntegration1(self):
        app = Flask(__name__)
        with app.app_context():
            baseAPI = BaseAPI()
            countryInfo = baseAPI.get_country_info(str("egypt"), "alpha3Code")  # EGY
            if countryInfo is None:
                countryInfo = "Not Found Or Invalid Input"

            output = jsonify(countryInfo)
            self.assertEqual(str(jsonify("EGY")), str(output))

    def test_RunIntegration2(self):
        app = Flask(__name__)
        with app.app_context():
            FilePath = "TestData/testData.json"
            offData = OfflineData(FilePath)
            offData.OpenFile()
            offData.LoadFile()
            offData.CloseFile()
            countryInfo = offData.GetData("egypt", "alpha3Code")  # EGY
            if countryInfo is None:
                countryInfo = "Not Found Or Invalid Input"

            output = jsonify(countryInfo)
            self.assertEqual(str(jsonify("EGY")), str(output))

    def test_RunIntegration3(self):
        app = Flask(__name__)
        with app.app_context():
            FilePath = "TestData/testData.json"
            offData = OfflineData(FilePath)
            offData.OpenFile()
            offData.LoadFile()
            offData.CloseFile()
            countryInfo = offData.GetData("egypt", "s")  # EGY
            if countryInfo is None:
                countryInfo = "Not Found Or Invalid Input"

            output = jsonify(countryInfo)
            self.assertEqual(str(jsonify("Not Found Or Invalid Input")), str(output))