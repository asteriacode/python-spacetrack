from time import sleep
from datetime import datetime, timedelta

import requests

from spacetrack.query import Query, BASE_URL
from spacetrack.models import OBJ_CLASS_TO_CLASS

MINUTE = timedelta(minutes=1)

# Recommended by spacetrack.
MAX_PER_MINUTE = 30


class Client:
    def __init__(self, username, password, immediate_auth=True, error_on_rate_limit=False):
        self.session = requests.Session()
        self.username = username
        self.password = password
        self.error_on_rate_limit = error_on_rate_limit

        self.rl_start = datetime.now()
        self.rl_count = 0

        if immediate_auth:
            self.attempt_auth()

    # Wait/error to avoid rate limiting, if needed, otherwise record it.
    # This should be called before making an API request
    def rl_request(self):
        # If more than a minute has passed since we started counting
        elapsed = (datetime.now() - self.rl_start)
        if elapsed.seconds / 60 > 0:
            # Restart the counter
            self.rl_start = datetime.now()
            self.rl_count = 1

            return True

        if self.rl_count >= MAX_PER_MINUTE:
            # We need to limit our rates
            if self.error_on_rate_limit:
                raise Exception("Rate limited (Client configured to error)")
            else:
                # Sleep until a minute has past from rl_start
                period_left = MINUTE - elapsed
                sleep(period_left.total_seconds())

                # Restart the timer/count
                self.rl_start = datetime.now()
                self.rl_count = 1
        else:
            self.rl_count += 1

        return True

    def attempt_auth(self):
        # Request a session cookie
        self.rl_request()
        res = self.session.post(BASE_URL + '/ajaxauth/login', data={
            'identity': self.username,
            'password': self.password
        })

        if not res.ok:
            raise Exception("Failed to authenticate with Spacetrack API.")

        # Store the session cookie
        self.session.cookies = res.cookies

    def dispatch_query(self, query, do_retry=True):
        self.rl_request()
        res = self.session.get(query.to_url())

        if not res.ok:
            # Reauth and try again
            if do_retry and res.status_code == 401:
                self.attempt_auth(query)
                self.dispatch_query(query, do_retry=False)
            else:
                raise Exception("Dispatching query failed: %s" % res.status_code)

        content = res.json()
        if query.obj_class in OBJ_CLASS_TO_CLASS:
            content = list([OBJ_CLASS_TO_CLASS[query.obj_class](x) for x in content])

        return content

    def latest_cdms(self, name, limit=10, skip=0):
        """
            Get the latest conjunction data for satellite name
            Returns a (possibly empty) list of Conjunctions
        """
        return self.dispatch_query(Query()
                                   .obj_class("cdm_public")
                                   .order_by([("CREATION_DATE", "DESC")])
                                   .limit(limit, skip=skip)
                                   .column("SAT_1_NAME", name))

    def latest_gps(self, name, limit=10, skip=0):
        """
            Return the latest general pertubation by object_name.
            Returns a (possibly empty) list of Pertubations.
        """
        return self.dispatch_query(Query()
                                   .obj_class("gp")
                                   .order_by([("CREATION_DATE", "DESC")])
                                   .limit(limit, skip=skip)
                                   .column("OBJECT_NAME", name))

    def latest_satcat(self, name):
        """
            Returns the current satcat by object_name.
            Returns a Satellite object or None.
        """
        res = self.dispatch_query(Query()
                                  .obj_class("satcat")
                                  .limit(1)
                                  .column("OBJECT_NAME", name)
                                  .column("CURRENT", "Y"))
        return res.pop() if len(res) > 0 else None

    def latest_decay(self, name):
        """
            Get the latest decay data by object_name.
            Returns a Decay object or None
        """
        res = self.dispatch_query(Query()
                                  .obj_class("decay")
                                  .order_by([("PRECEDENCE", "ASC")])
                                  .limit(1)
                                  .column("OBJECT_NAME", name))
        return res.pop() if len(res) > 0 else None
