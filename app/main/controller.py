# -*- encoding: utf-8 -*-

import time
import flask_restful

from .. import *

class MyController(flask_restful.Resource):
    """A Controller defined for DEMO Purpose, returns static JSONs"""

    def get(self):
        """Returns a Static JSON representing a GET requests"""

        infoLogger.info("GET, from MyController - this is a INFO Message")

        try:
            return 1 / 0 # obviously this will fail!
        except ZeroDivisionError:
            # https://stackoverflow.com/questions/5191830
            errorLogger.exception("ERROR Message, implemented forcefully")
            return {
                "time"    : str(time.ctime()),
                "message" : "Encountered Error",
            }
