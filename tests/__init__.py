import unittest
from test_query import *
from test_client import *
from os import environ

# This could put sensitive data into stdout (ie cookies, usernames, passwords)
# Only use it if you're ok with that.
if environ.get('DEBUG_REQUESTS') == '1':
    import requests
    import logging
    import http.client as http_client

    # Log all HTTP Requests and reponse headers
    http_client.HTTPConnection.debuglevel = 1

    logging.basicConfig()
    logging.getLogger().setLevel(logging.DEBUG)
    requests_log = logging.getLogger("requests.packages.urllib3")
    requests_log.setLevel(logging.DEBUG)
    requests_log.propagate = True

if __name__ == "__main__":
    unittest.main()