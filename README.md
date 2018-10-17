## Drchrono web API

For creating the app I used aiohttp -
 asynchronous web framework, written by Python Core developers.

Also I used Mongodb with motor(asyncronous driver) as database,
envparse for working with secure environment variables, jinja2 for templates

For beginning you need *Python 3.6* or above and install requirements to virtualenv

```bash
virtualenv --python=python3.6 env
source env/bin/activate
pip install -r requirements.txt
```

You must add config *defaults.env* file there will be your secure settings (database connection, secret salt etc.)

Short sample *defaults.env* file

```python
DEBUG=True
MONGO_HOST='localhost'
MONGO_DB_NAME='drchrono'
SECRET_KEY='your_key_for_sessions'
HOST='0.0.0.0'
PORT=3000
USER_COLLECTION='users'
CLIENT_ID='drchrono_client_id'
CLIENT_SECRET='drchrono_client_secret'
REDIRECT_URI='http://host.net/callback/'
BASE_URL='https://drchrono.com'
```

MongoDB with auth: *'mongodb://user:pass@mongo_host:mongo_port/mongo_database'*

You can add new views modules in app/modules.py per comma

To start app activate virtualenv and run *server.py*

```bash
source env/bin/activate
python server.py
```

###### Tested on:
- Ubuntu 16.04 + python3.6 / python3.7
- Windows 10 + python3.7
- Windows 10 Linux Ubuntu 14.04 subsystem + python 3.6
