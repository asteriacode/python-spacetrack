import unittest
from spacetrack.query import Query, BASE_URL

class QueryTests(unittest.TestCase):
    def test_all(self):
        q = Query() \
            .obj_class("testclass") \
            .limit(20, 10) \
            .order_by([("name", "asc"), ("date", "desc")]) \
            .metadata() \
            .distinct() \
            .empty_result() \
            .column("one_or_two", "1", "2") \
            .column("three", "3") \

        query_url = q.to_url()
        print(f"{query_url = }")
        assert query_url == "https://www.space-track.org/basicspacedata/query/class/testclass/limit/20,10/orderby/name asc,date desc/metadata/true/distinct/true/emptyresult/show/one_or_two/1,2/three/3"

# TODO: More tests