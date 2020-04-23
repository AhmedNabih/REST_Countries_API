import json
import unittest

from flask import Flask
from mock import patch, Mock
from API.Base_API import BaseAPI
from API.app import app


class TestBaseAPI(unittest.TestCase):

    def setUp(self):
        self.baseAPI = BaseAPI()
        self.tester = app.test_client()
        self.tester.testing = True

    @patch('requests.get')
    def test_get_country_info_success(self, mock_get):
        mock_resp = Mock()
        mock_resp.status_code = 200
        mock_resp.content = json.dumps([{'alpha2Code': 'EG', 'bb': 'hhh'}])

        mock_get.return_value = mock_resp

        a,_ = self.baseAPI.get_country_info("egypt", "alpha2Code")
        self.assertEqual('EG', a)

    @patch('requests.get')
    def test_get_country_info_fail(self, mock_get):
        mock_resp = Mock()
        mock_resp.status_code = 201

        mock_get.return_value = mock_resp

        a,_ = self.baseAPI.get_country_info("egypt", "alpha2Code")
        self.assertIsNone(a)

    def test_get_country_info_fail_invalid_input_type(self):
        a, _ = self.baseAPI.get_country_info(5, "alpha2Code")
        self.assertIsNone(a)
        b,_ = self.baseAPI.get_country_info("egypt", 0.2)
        self.assertIsNone(b)
        c,_ = self.baseAPI.get_country_info("egypt", 'sss')
        self.assertIsNone(c)

    @patch('requests.get')
    def test_call_api_success(self, mock_get):
        mock_resp = Mock()
        mock_resp.status_code = 200
        mock_get.return_value = mock_resp
        self.assertTrue(self.baseAPI.callAPI())

    @patch('requests.get')
    def test_call_api_fail(self, mock_get):
        mock_resp = Mock()
        mock_resp.status_code = 400
        mock_get.return_value = mock_resp
        self.assertFalse(self.baseAPI.callAPI())

    def test_cache_success(self):
        appTest = Flask(__name__)
        with appTest.app_context():
            _, formCache1 = self.baseAPI.get_country_info("egypt", "alpha2Code")
            _, formCache2 = self.baseAPI.get_country_info("egypt", "alpha2Code")

            self.assertFalse(formCache1)
            self.assertTrue(formCache2)
