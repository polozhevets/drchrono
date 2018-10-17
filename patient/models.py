#!python3.6
from settings import PATIENT_COLLECTION
import logging
from .api import get_patients
from pymongo.errors import DuplicateKeyError
from utils import _hash_from_dict
import asyncio


class Patient(object):
    """Docstring for Patient."""

    def __init__(self, db, **kwargs):
        """Init."""
        super(Patient, self).__init__()
        self.collection = db[PATIENT_COLLECTION]

    async def query(self, access_token, query={}, update=False):
        """Get data."""
        data = await self.collection.find(query).to_list(length=None)
        if not data or update:
            await self.collection.create_index([("id", 1)], unique=True)
            await self.collection.create_index([("sha1", 1)], unique=True)
            data = await get_patients(access_token)
            logging.info('Updating patients list...')
            for element in data:
                sha1 = _hash_from_dict(element)
                element['sha1'] = sha1  # Good to compare
                try:
                    await self.collection.insert_one(element)
                except DuplicateKeyError:
                    if not await self.collection.find_one({'sha1': sha1}):
                        element.pop('_id')
                        await self.collection.replace_one({'id': element['id']}, element, True)
        if update:
            await asyncio.sleep(60 * 60 / 500)
            return data
        return data
