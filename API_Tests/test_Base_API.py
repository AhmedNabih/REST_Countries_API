import json
import unittest

import requests_cache
from mock import patch, Mock
from API.Base_API import BaseAPI


class TestBaseAPI(unittest.TestCase):

    def setUp(self):
        self.baseAPI = BaseAPI()

    @patch('requests.get')
    def test_get_country_info_success(self, mock_get):
        mock_resp = Mock()
        mock_resp.status_code = 200
        mock_resp.content = json.dumps([{'alpha2Code': 'EG', 'bb': 'hhh'}])

        mock_get.return_value = mock_resp

        self.assertEqual('EG', self.baseAPI.get_country_info("egypt", "alpha2Code"))

    @patch('requests.get')
    def test_get_country_info_fail(self, mock_get):
        mock_resp = Mock()
        mock_resp.status_code = 201

        mock_get.return_value = mock_resp

        self.assertIsNone(self.baseAPI.get_country_info("egypt", "alpha2Code"))

    def test_get_country_info_fail_invalid_input_type(self):

        self.assertIsNone(self.baseAPI.get_country_info(5, "alpha2Code"))
        self.assertIsNone(self.baseAPI.get_country_info("egypt", 0.2))
        self.assertIsNone(self.baseAPI.get_country_info("egypt", 'sss'))

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
        requests_cache.install_cache(cache_name='My_cache', backend='sqlite', expire_after=10)
        _, formCache1 = self.baseAPI.get_country_info("egypt", "alpha2Code")
        _, formCache2 = self.baseAPI.get_country_info("egypt", "alpha2Code")

        self.assertFalse(formCache1)
        self.assertTrue(formCache2)

    def test_cache_fail(self):
        _, formCache1 = self.baseAPI.get_country_info("egypt", "alpha2Code")
        _, formCache2 = self.baseAPI.get_country_info("egypt", "alpha2Code")

        self.assertFalse(formCache1)
        self.assertFalse(formCache2)
