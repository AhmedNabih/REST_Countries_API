import json
import unittest

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
