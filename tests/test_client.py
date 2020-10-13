import unittest
from os import getenv

from spacetrack.client import Client
from spacetrack.query import Query

class QueryTests(unittest.TestCase):
    def setUp(self):
        username = getenv('ST_USERNAME')
        password = getenv('ST_PASSWORD')

        self.client = Client(username, password)

    def test_dispatch_query(self):
        q = Query().obj_class("boxscore") \
            .limit(1)

        res = self.client.dispatch_query(q)