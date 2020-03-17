import json
import unittest

from mock import patch, Mock

from API.Base_API import BaseAPI


class Integration(unittest.TestCase):

    def setUp(self):
        self.baseAPI = BaseAPI()

    def RunIntegration(self):
        pass
