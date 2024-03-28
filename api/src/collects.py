import os
from typing import Any
from motor.motor_asyncio import AsyncIOMotorClient

from dotenv import load_dotenv

load_dotenv()

class DB_Collections():

    client: Any = AsyncIOMotorClient(host=os.getenv('MONGO_ADDRESS'), port=os.getenv('MONGO_PORT'))
    db: Any = client[os.getenv('MONGO_DB_NAME')]


    def __init__(cls) -> None:
        cls.client = AsyncIOMotorClient(host=os.getenv('MONGO_ADDRESS'), port=os.getenv('MONGO_PORT'))
        cls.db = cls.client[os.getenv('MONGO_DB_NAME')]

    async def get_db(cls) -> Any:
        return cls.db

