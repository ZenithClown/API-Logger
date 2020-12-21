# -*- encoding: utf-8 -*-

"""Initialization of Flask REST-API Environment"""

from flask import Flask


def create_app():
    """Creates a Simple `app` which can be used for Demonstrating API Logger"""
    
    app = Flask(__name__)
    app.config.update(DEBUG = True, TESTING = False)

    return app