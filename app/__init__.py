#!python3.6
from aiohttp import web
from app.routes import routes
from motor import motor_asyncio
from settings import JOBS, MONGO_DB_NAME, MONGO_HOST
from app.jobs import daily_jobs
import aiohttp_jinja2
import jinja2

app = web.Application()
for route in routes:
    app.router.add_routes(route)

# DB
app.client = motor_asyncio.AsyncIOMotorClient(MONGO_HOST)
app.db = app.client[MONGO_DB_NAME]

# aiohttp_jinja2
aiohttp_jinja2.setup(app, loader=jinja2.FileSystemLoader('templates'))

async def start_background_tasks(app):
    app.loop.create_task(daily_jobs(app))

if JOBS:
    app.on_startup.append(start_background_tasks)
