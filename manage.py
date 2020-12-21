# -*- encoding: utf-8 -*-

"""API Management and Server Running Module"""

import os
from flask_restful import Api

from app.main import create_app

# setting the environment
from dotenv import load_dotenv # Python 3.6+
load_dotenv(verbose = True)

app = create_app()
api = Api(app)

### --- List of all Resources --- ###
from app.main.controller import MyController

# add all main, and special resources
api.add_resource(MyController, "/home")

### --- __main__ --- ###
if __name__ == "__main__":
    app.run(
            port = os.getenv('port', 5000),
            host = os.getenv('host', 'localhost')
        )