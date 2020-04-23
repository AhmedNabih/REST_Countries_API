import json
import unittest

from flask import jsonify, Flask
from API.app import app
from mock import patch, Mock


class TestApp(unittest.TestCase):

    def setUp(self):
        self.tester = app.test_client()
        app.doTesting = True
        self.tester.testing = True

    def test_status_code(self):
        response = self.tester.get('/')
        self.assertEqual(response.status_code, 200)

    @patch('requests.get')
    def test_Getting_Data_success(self, mock_get):
        mock_resp = Mock()
        mock_resp.status_code = 200
        mock_resp.content = json.dumps([{'capital': 'Cairo'}])
        mock_get.return_value = mock_resp

        appTest = Flask(__name__)
        with appTest.app_context():
            response = self.tester.get("/egypt/capital/")
            strTest = ['Cairo']
            jsonData = jsonify(strTest)
            self.assertEqual(response.data, jsonData.data)

