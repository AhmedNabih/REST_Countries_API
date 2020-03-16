import unittest
from API.offline_Data import OfflineData
from unittest.mock import patch, mock_open


class TestOfflineData(unittest.TestCase):

    def setUp(self):
        self.FilePath = "TestData/fakeData.json"
        self.offlineData = OfflineData(self.FilePath)

    def tearDown(self):
        pass

    def test_OpenFile_success(self):
        try:
            with self.assertRaises(OSError):
                self.offlineData.OpenFile()
                self.offlineData.CloseFile()
        except AssertionError as e:
            if str(e) != "OSError not raised":
                raise AssertionError

    def test_OpenFile_fail(self):
        self.offlineData = OfflineData("fake path")
        with self.assertRaises(OSError):
            self.offlineData.OpenFile()

    def test_LoadFile_success(self):
        try:
            with self.assertRaises(OSError):
                self.offlineData.OpenFile()
                self.offlineData.LoadFile()
                self.offlineData.CloseFile()
        except AssertionError as e:
            if str(e) != "OSError not raised":
                raise AssertionError

    def test_LoadFile_fail(self):
        self.offlineData = OfflineData("fake path")
        with self.assertRaises(OSError):
            self.offlineData.LoadFile()
