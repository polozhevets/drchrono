from aiohttp import web
from aiohttp import ClientSession, ClientTimeout
from settings import BASE_URL

api_timeout = 10


def get_headers(access_token):
    if not access_token:
        raise web.HTTPFound('/auth/')
    return {'Authorization': 'Bearer %s' % access_token}


async def get_patients(access_token):
    """To do: get_data(result.get('next'))."""
    async def get_data(data_url):
        response = await requests.get(data_url, headers=get_headers(access_token))
        result = None
        if response.status == 200:
            result = await response.json()
        await requests.close()
        if not result:
            result = {'error': response.status}
        return result
    timeout = ClientTimeout(total=api_timeout)
    requests = ClientSession(timeout=timeout)
    data_url = BASE_URL + '/api/patients'
    result = await get_data(data_url)
    return result.get('results')


async def get_user(access_token):
    timeout = ClientTimeout(total=api_timeout)
    requests = ClientSession(timeout=timeout)
    data_url = BASE_URL + '/api/users/current'
    response = await requests.get(data_url, headers=get_headers(access_token))
    await requests.close()
    if response.status == 200:
        result = await response.json()
        return result
    else:
        return {'error': response.status}
