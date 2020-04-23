import unittest

from flask import Flask, jsonify
from mock import patch
from API.Base_API import BaseAPI
from API.app import app


class Integration(unittest.TestCase):

    def setUp(self):
        self.tester = app.test_client()
        self.tester.testing = True

    @patch('API.Base_API.BaseAPI.get_country_info')
    def test_RunIntegration1(self, mock_get_country_info):
        appTest = Flask(__name__)
        with appTest.app_context():
            mock_get_country_info.return_value = "EGY", None
            baseAPI = BaseAPI()
            countryInfo,_ = baseAPI.get_country_info(str("egypt"), "alpha3Code")  # EGY
            if countryInfo is None:
                countryInfo = "Not Found Or Invalid Input"

            self.assertEqual(str("EGY"), str(countryInfo))

    def test_Getting_Data_success(self):
        appTest = Flask(__name__)
        with appTest.app_context():
            response = self.tester.get("/egypt/capital/")
            strTest = ['Cairo']
            jsonData = jsonify(strTest)
            self.assertEqual(response.data, jsonData.data)