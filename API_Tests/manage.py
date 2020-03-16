import unittest
from API.offline_Data import OfflineData


class TestBasic(unittest.TestCase):

    def test_1(self):
        self.assertEqual(5, 5, "ggggg")

    def test_2(self):
        self.assertEqual(4, 4, "ahmed")


if __name__ == '__main__':
    unittest.main()
