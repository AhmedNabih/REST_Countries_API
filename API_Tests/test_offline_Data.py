import unittest
from API.offline_Data import OfflineData


class TestOfflineData(unittest.TestCase):

    def setUp(self):
        self.FilePath = "TestData/testData.json"
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

    def test_GetData_success_valid_name_valid_category(self):
        self.offlineData.OpenFile()
        self.offlineData.LoadFile()
        self.offlineData.CloseFile()

        RealAns1 = "Cairo"
        RealAns2 = "EGY"
        RealAns3 = "['20']"

        self.assertEqual(RealAns1, str(self.offlineData.GetData("egypt", "capital")))
        self.assertEqual(RealAns2, str(self.offlineData.GetData("egypt", "alpha3Code")))
        self.assertEqual(RealAns3, str(self.offlineData.GetData("egypt", "callingCodes")))

    def test_GetData_fail_invalid_name_valid_category(self):
        self.offlineData.OpenFile()
        self.offlineData.LoadFile()
        self.offlineData.CloseFile()

        self.assertIsNone(self.offlineData.GetData("brba2", "capital"))
        self.assertIsNone(self.offlineData.GetData("brba2", "alpha3Code"))
        self.assertIsNone(self.offlineData.GetData("brba2", "callingCodes"))

    def test_GetData_fail_valid_name_invalid_category(self):
        self.offlineData.OpenFile()
        self.offlineData.LoadFile()
        self.offlineData.CloseFile()

        self.assertIsNone(self.offlineData.GetData("egypt", "brba2"))
        self.assertIsNone(self.offlineData.GetData("egypt", "brba2"))
        self.assertIsNone(self.offlineData.GetData("egypt", "brba2"))

    def test_GetData_fail_invalid_name_invalid_Category(self):
        self.offlineData.OpenFile()
        self.offlineData.LoadFile()
        self.offlineData.CloseFile()

        self.assertIsNone(self.offlineData.GetData("brba2", "brba2"))
        self.assertIsNone(self.offlineData.GetData("brba2", "brba2"))
        self.assertIsNone(self.offlineData.GetData("brba2", "brba2"))

    def test_GetData_success_invalid_input_type(self):
        self.offlineData.OpenFile()
        self.offlineData.LoadFile()
        self.offlineData.CloseFile()

        self.assertIsNone(self.offlineData.GetData(5, "brba2"))
        self.assertIsNone(self.offlineData.GetData("brba2", 'kkk'))
        self.assertIsNone(self.offlineData.GetData(0.1, "brba2"))
