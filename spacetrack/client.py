import requests
from requests.utils import add_dict_to_cookiejar
from spacetrack.query import Query, BASE_URL

class Client:
    def __init__(self, username, password):
        self.session = requests.Session()
        self.session.headers = {
            'User-Agent': "curl/7.72.0",
            "Accept": "*/*"
        }
        self.username = username
        self.password = password

        self.attempt_auth()

    def attempt_auth(self):
        # Request a session cookie
        res = self.session.post(BASE_URL + '/ajaxauth/login', data={
            'identity': self.username,
            'password': self.password
        })

        if not res.ok:
            raise Exception("Failed to authenticate with Spacetrack API.")

        # Store the session cookie
        self.session.cookies = res.cookies

    def dispatch_query(self, query):
        # TODO: Rate limiting
        res = self.session.get(query.to_url())

        if not res.ok:
            # TODO: Reauth and try again
            raise Exception("Dispatching query failed")

        # TODO: Parse into class
        return res.json()