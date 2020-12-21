# -*- encoding: utf-8 -*-

"""API Management and Server Running Module"""

import os
from flask_restful import Api

from app.main import (
        db, # SQLAlchemy Connector dB Object
        create_app
    )

# setting the environment
from dotenv import load_dotenv # Python 3.6+
load_dotenv(verbose = True)

app = create_app(os.getenv("PROJECT_ENV_NAME") or "dev") # check config.py
api = Api(app)

### --- List of all Resources --- ###
from app.main.application import *

# starting from this design, use the convention of API URL as follows:
# localhost:5000/api/v1.x/... or localhost:5000/api/v2.x/... or, etc.
# set version of api from __api_version__
__api_version__ = "v0.1-template"

# add all main, and special resources

### --- __main__ --- ###
if __name__ == "__main__":
    PORT = os.getenv('port', 5000)
    HOST = os.getenv('host', 'localhost')
    app.run() # need to set host and other informations - from .env File