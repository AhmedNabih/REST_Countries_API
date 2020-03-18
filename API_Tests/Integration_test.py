import json
import unittest

from flask import jsonify, Flask
from mock import patch, Mock
from API.offline_Data import OfflineData
from API.Base_API import BaseAPI


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
