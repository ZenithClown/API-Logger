# -*- encoding: utf-8 -*-

import time

from uuid import uuid4
from flask_restful import Resource

from .. import getLogger

class MyController(Resource):
    """A Controller defined for DEMO Purpose, returns static JSONs"""

    def __init__(self):
        self.logger = getLogger()

    def get(self):
        """Returns a Static JSON representing a GET requests"""

        self.logger.info("GET, from MyController")
        return {
            "ID"      : str(uuid4()),
            "time"    : str(time.ctime()),
            "message" : "JSON Static Message"
        }