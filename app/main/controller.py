# -*- encoding: utf-8 -*-

import time

from uuid import uuid4
from flask_restful import Resource

class MyController(Resource):
    """A Controller defined for DEMO Purpose, returns static JSONs"""

    def get(self):
        """Returns a Static JSON representing a GET requests"""

        return {
            "ID"      : str(uuid4()),
            "time"    : str(time.ctime()),
            "message" : "JSON Static Message"
        }