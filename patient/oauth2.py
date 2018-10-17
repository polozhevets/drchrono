#!python3.6
from uuid import uuid4
from settings import CLIENT_ID, CLIENT_SECRET, REDIRECT_URI, BASE_URL
import urllib.parse
from aiohttp import ClientSession, BasicAuth, ClientTimeout


def user_agent():
    """Generate User Agent for each client."""
    return "oauth2 /u/%s" % str(uuid4())


def save_created_state(state):
    # to do
    pass


def is_valid_state(state):
    # to do
    return True


def base_headers():
    return {"User-Agent": user_agent()}


def make_authorization_url():
    """
    Generate a random string for the state parameter.

    Save it for use later to prevent xsrf attacks.
    """
    state = str(uuid4())
    save_created_state(state)
    params = {"client_id": CLIENT_ID,
              "response_type": "code",
              "state": state,
              "redirect_uri": REDIRECT_URI}
    url = BASE_URL + "/o/authorize?" + urllib.parse.urlencode(params)
    return url


async def get_token(code):
    session = BasicAuth(CLIENT_ID, CLIENT_SECRET)
    timeout = ClientTimeout(total=10)
    requests = ClientSession(auth=session, timeout=timeout)
    post_data = {"grant_type": "authorization_code",
                 "code": code,
                 "redirect_uri": REDIRECT_URI}
    headers = base_headers()
    response = await requests.post(
        BASE_URL + "/o/token/",
        auth=session,
        headers=headers,
        data=post_data
    )
    token_json = await response.json()
    await requests.close()
    return token_json.get("access_token")
