import unittest
from API.InternetConnection import Connection
from mock import patch, MagicMock, Mock


class TestInternetConnection(unittest.TestCase):

    def setUp(self):
        self.con = Connection()

    @patch('urllib.request.urlopen')
    def test_CheckInternetConnection_success(self, mock_urlopen):
        cm = MagicMock()
        cm.getcode.return_value = 200
        cm.read.return_value = 'contents'
        cm.__enter__.return_value = cm
        mock_urlopen.return_value = cm

        self.assertEqual(True, self.con.CheckInternetConnection())

    def test_CheckInternetConnection_fail(self):
        a = Mock('urllib.request.urlopen', side_effect=Exception)

        self.assertEqual(False, self.con.CheckInternetConnection())
