#!python3.6
import asyncio
import inspect

jobs = []

async def daily_jobs(app):
    while True:
        for job in jobs:
            if inspect.iscoroutinefunction(job):
                await job(app)
            else:
                job(app)
        await asyncio.sleep(60 * 60 * 24)
