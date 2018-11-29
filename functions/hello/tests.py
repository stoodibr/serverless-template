import json
import unittest

from .main import handler


class HelloTest(unittest.TestCase):
    def test_handler(self):
        response = handler({}, {})
        self.assertEqual(response['statusCode'], 200)

        body = json.loads(response['body'])
        self.assertEqual(body['message'], 'Go Serverless!')
