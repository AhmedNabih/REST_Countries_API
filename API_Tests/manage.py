import unittest


class TestBasic(unittest.TestCase):

    def test1(self):
        self.assertEqual(self, 5, 4)


if __name__ == '__main__':
    unittest.main()
