#!python3.6
import json
from bson import ObjectId
import datetime
from aiohttp import web
from aiohttp.client_exceptions import ClientConnectorError
import logging
import inspect


class JSONEncoder(json.JSONEncoder):
    """JSONEncoder."""

    def default(self, o):
        """Json defaults."""
        if isinstance(o, ObjectId):
            return str(o)
        elif isinstance(o, datetime.datetime):
            return o.timestamp()
        return json.JSONEncoder.default(self, o)


def json_response(fn):
    async def decorator(*args, **kwargs):
        headers = {'Access-Control-Allow-Origin': '*'}
        result = None
        try:
            result = await fn(*args, **kwargs)
        except ClientConnectorError as e:
            result = {'error': e}
            logging.error(e)
        responce = json.dumps(result, cls=JSONEncoder)
        return web.json_response(body=responce, headers=headers)
    return decorator


def text_response(fn):
    async def decorator(*args, **kwargs):
        if inspect.iscoroutinefunction(fn):
            result = await fn(*args, **kwargs)
        else:
            result = fn(*args, **kwargs)
        headers = {'Access-Control-Allow-Origin': '*'}
        return web.Response(text=str(result), headers=headers)
    return decorator
