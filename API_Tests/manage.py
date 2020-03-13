import unittest


class TestBasic(unittest.TestCase):

    def test1(self):
        self.assertEqual(5, 5, "ggggg")

    def test2(self):
        self.assertEqual(4, 4, "ahmed")


if __name__ == '__main__':
    unittest.main()
