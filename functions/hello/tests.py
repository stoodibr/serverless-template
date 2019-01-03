import unittest

from .main import index


class HelloTest(unittest.TestCase):
    def test_index(self):
        body = index({}, {})
        self.assertEqual(body['message'], 'Go Serverless!')
