from typing import Any
from motor.motor_asyncio import AsyncIOMotorClient

from api.src.constance import MONGO_ADDRESS, MONGO_PORT, MONGO_DB_NAME

class DB_Collections():

    client: Any = AsyncIOMotorClient(host=MONGO_ADDRESS, port=MONGO_PORT)
    db: Any = client[MONGO_DB_NAME]


    def __init__(cls) -> None:
        cls.client = AsyncIOMotorClient(host=MONGO_ADDRESS, port=MONGO_PORT)
        cls.db = cls.client[MONGO_DB_NAME]

    async def get_db(cls) -> Any:
        return cls.db

