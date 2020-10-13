import unittest
from os import getenv

from spacetrack.client import Client
from spacetrack.query import Query
from unittest.mock import patch

class QueryTests(unittest.TestCase):
    def setUp(self):
        username = getenv('ST_USERNAME')
        password = getenv('ST_PASSWORD')

        self.client = Client(username, password)

    # Note this doesn't actually fire off any requests
    def test_rate_limit_error(self):
        err_client = Client("", "", immediate_auth=False, error_on_rate_limit=True)
        for _ in range(0, 30):
            err_client.rl_request()

        with self.assertRaises(Exception):
            err_client.rl_request()

    # Note this doesn't actually fire off any requests
    @patch('spacetrack.client.sleep')
    def test_rate_limit_sleep(self, sleep):
        sleep_client = Client("", "", immediate_auth=False)
        for _ in range(0, 30):
            sleep_client.rl_request()

        sleep_client.rl_request()
        assert sleep.called

    def test_dispatch_query(self):
        q = Query().obj_class("boxscore") \
            .limit(1)

        res = self.client.dispatch_query(q)