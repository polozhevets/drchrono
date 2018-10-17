#!python3.6
from app import app, web
from settings import SITE_HOST, SITE_PORT, DEBUG
import logging

access_log_format = '%a %t "%r" %s %b'

if DEBUG:
    logging.basicConfig(
        level=logging.DEBUG,
    )

web.run_app(app, host=SITE_HOST, port=SITE_PORT, access_log=logging, access_log_format=access_log_format)
