#!python3.6
from aiohttp import web
from app.utils import json_response, text_response
from .models import Patient
from .oauth2 import get_token, make_authorization_url
from .api import get_user
import aiohttp_jinja2


routes = web.RouteTableDef()
access_token = None


@routes.get('/auth/')
@text_response
def auth(request):
    url = make_authorization_url()
    raise web.HTTPFound(url)


@routes.get('/callback/')
@json_response
async def get_callback(request):
    global access_token
    q = request.rel_url.query
    data = dict(q)
    code = data.get('code')
    access_token = await get_token(code)
    if access_token:
        raise web.HTTPFound('/patients/')
    else:
        return {'access_token_error': access_token}


@routes.get('/json/patients/')
@json_response
async def json_patients(request):
    patient = Patient(request.app.db)
    return await patient.query(access_token)


@routes.get('/json/user/')
@json_response
async def json_user(request):
    return await get_user(access_token)


@routes.get('/')
@routes.get('/patients/')
@aiohttp_jinja2.template('patients.html')
async def html_patients(request):
    patient = Patient(request.app.db)
    patients = await patient.query(access_token)
    return {'patients': patients}


@routes.get('/update/')
@aiohttp_jinja2.template('patients.html')
async def update_patients(request):
    patient = Patient(request.app.db)
    await patient.query(access_token, update=True)
    raise web.HTTPFound('/patients/')


@routes.get('/user/')
@aiohttp_jinja2.template('user.html')
async def html_user(request):
    return await get_user(access_token)
