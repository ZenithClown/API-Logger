# -*- encoding: utf-8 -*-
# must require Python 3.6+ : (i) f-String, (ii) dotenv

import yaml
import logging
from logging.config import dictConfig

try:
    import importlib.resources as pkg_resources
except ImportError:
    # Try backported to PY<37 `importlib_resources`.
    import importlib_resources as pkg_resources

from . import static

# def logmaker():
#     path = os.path.join("home", "debmalya", "pOrgz", "logs.log")
#     return logging.FileHandler(path)

def getLogger(loggerName : str = __name__):
    """Defination of a Logger-Functionality - can be used to Track User Sessions and Login Information"""

    # https://stackoverflow.com/questions/6028000/
    # https://stackoverflow.com/questions/56688232/
    loggerFile = pkg_resources.open_text(static, 'logger.yaml') # included static file in MANIFEST.in

    # define logger using PyYAML
    config = yaml.safe_load(loggerFile.read())
    dictConfig(config)

    return logging.getLogger(loggerName)

# logger = getLogger()