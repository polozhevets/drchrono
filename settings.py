#!python3.6
from os.path import isfile
from envparse import env


if isfile('defaults.env'):
    env.read_envfile('defaults.env')

# Server app
DEBUG = env.bool('DEBUG', default=False)
SITE_HOST = env.str('HOST', default='127.0.0.1')
SITE_PORT = env.int('PORT', default=8888)
SECRET_KEY = env.str('SECRET_KEY', default='enter your secret')
MONGO_HOST = env.str('MONGO_HOST', default='127.0.0.1')
MONGO_DB_NAME = env.str('MONGO_DB_NAME', default='testdb')
USER_COLLECTION = env.str('USER_COLLECTION', default='users')
JOBS = env.bool('JOBS', default=False)
# OAuth2
CLIENT_ID = env.str('CLIENT_ID')
CLIENT_SECRET = env.str('CLIENT_SECRET')
REDIRECT_URI = env.str('REDIRECT_URI')
# Drchrono
BASE_URL = env.str('BASE_URL')
PATIENT_COLLECTION = env.str('PATIENT_COLLECTION', default='patients')
