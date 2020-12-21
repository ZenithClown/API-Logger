# -*- encoding: utf-8 -*-
# this file will be excluded form sphinx-build
# include the class seperately to sphinx-build, if required

import os

# setting the environment
from dotenv import load_dotenv # Python 3.6+

load_dotenv(verbose = True)

basedir    = os.path.abspath(os.path.dirname(__file__)) # base directory
local_base = os.getenv('DATABASE_URL', 'my-database-url-string')

class Config:
    """Base Configuration Class - Inherited by Others"""

    DEBUG      = False
    SECRET_KEY = os.getenv("SECRET_KEY", "my_secret_key")


class DevelopmentConfig(Config):
    """Development Configuration: invoke this using config_name = dev"""

    DEBUG = True # This is a development server.

    # set database
    SQLALCHEMY_DATABASE_URI = f"{local_base}/{os.getenv('dev_db', 'dev-database')}"
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class TestingConfig(Config):
    """Testing Environment: invoke this using config_name = test"""

    DEBUG   = True
    TESTING = True

    # set database
    SQLALCHEMY_DATABASE_URI = f"{local_base}/{os.getenv('test_db', 'test-database')}"

    PRESERVE_CONTEXT_ON_EXCEPTION  = False
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class ProductionConfig(Config):
    """Production Environment: invoke this using config_name = prod"""

    DEBUG = False

    # uncomment the line below to use configure database
    # SQLALCHEMY_DATABASE_URI = local_base

config_by_name = dict(
        dev  = DevelopmentConfig,
        test = TestingConfig,
        prod = ProductionConfig
    )

key = Config.SECRET_KEY
