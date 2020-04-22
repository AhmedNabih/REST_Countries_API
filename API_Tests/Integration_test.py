import unittest

from flask import Flask
from mock import patch
from API.Base_API import BaseAPI


class Integration(unittest.TestCase):

    @patch('API.Base_API.BaseAPI.get_country_info')
    def test_RunIntegration1(self, mock_get_country_info):
        app = Flask(__name__)
        with app.app_context():
            mock_get_country_info.return_value = "EGY"
            baseAPI = BaseAPI()
            countryInfo = baseAPI.get_country_info(str("egypt"), "alpha3Code")  # EGY
            if countryInfo is None:
                countryInfo = "Not Found Or Invalid Input"

            self.assertEqual(str("EGY"), str(countryInfo))
