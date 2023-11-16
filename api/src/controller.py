
import asyncio
import logging
from typing import Any
from passlib.context import CryptContext
from fastapi.security import OAuth2PasswordBearer
from motor.motor_asyncio import AsyncIOMotorCollection, AsyncIOMotorClient, AsyncIOMotorDatabase


from model.User import User
from api.src.constance import ALGORITHM
from api.src.user_authenticator import Authenticator


class Controller():

    client: AsyncIOMotorClient
    db: AsyncIOMotorDatabase

    def __init__(self) -> None:

        pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
        oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")
        
        self.authenticator = Authenticator()
        self.authenticator.initialize(pwd_context, oauth2_scheme)

    async def check_db_connection(self):
        try:
            db_names = await self.client.list_database_names()

            collection_names = await self.db.list_collection_names()
            cursor = self.users_collection.find({})

            entries = await cursor.to_list(length=None)

            logging.debug(f"Connected to MongoDB. Available databases: {db_names}")
            logging.debug(f"Connected to MongoDB. Available collections: {collection_names}")
            logging.debug(f"Connected to MongoDB. User Entries: {entries}")

            

            return {"Databases": db_names, "Collections:": collection_names, 'Entry[User]': entries}
            
        
        except Exception as e:
            return(f"Failed to connect to MongoDB. Error: {e}")
        

    async def init_collections(self):
        self.users_collection = self.db["users"]
        self.group_collection = self.db["groups"]
        self.join_group_requests_collection = self.db["joinGroupRequests"]
        self.local_events_collection = self.db["localEvents"]
        self.boardgames_collection = self.db["boardgames"]

        await self.users_collection.create_index("username", unique=True)
        await self.group_collection.create_index("group_name", unique=True)

        

    async def get_users(self) -> dict:
        users = self.users_collection.find().to_list(length=None)

        return {'user': users}


    async def create_user(self, user: User, password: str):
        try:
            db_user = self.authenticator.create_db_user(user, password)

            await self.users_collection.insert_one(db_user.model_dump(by_alias=True))

            return {"Message": "Successfully create user"}
        except Exception as ex:
            return {"Message": "Failed to create the user somehow", "Error": f"{ex}"}

