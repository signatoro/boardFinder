
import asyncio
import logging
from typing import Any
from datetime import datetime, timedelta
from passlib.context import CryptContext
from fastapi.security import OAuth2PasswordBearer
from fastapi import Depends, HTTPException, status
from api.src.constance import ACCESS_TOKEN_EXPIRE_MINUTES
from motor.motor_asyncio import AsyncIOMotorCollection, AsyncIOMotorClient, AsyncIOMotorDatabase

from model.User import User, UserDb, Token
from api.src.user_authenticator import Authenticator


class Controller():

    client: AsyncIOMotorClient
    db: AsyncIOMotorDatabase
    
    users_collection: AsyncIOMotorCollection = None
    group_collection: AsyncIOMotorCollection = None
    boardgames_collection: AsyncIOMotorCollection = None
    local_events_collection: AsyncIOMotorCollection = None
    join_group_requests_collection: AsyncIOMotorCollection = None
    

    def __init__(self) -> None:

        self.pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
        self.oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")


    def initialize(self):
        loop = asyncio.get_event_loop()
        loop.create_task(self.init_collections())

        self.users_collection = self.db["users"]
        
        self.authenticator = Authenticator()
        self.authenticator.initialize(self.pwd_context, self.oauth2_scheme, self.users_collection)

    async def check_db_connection(self):
        try:
            db_names = await self.client.list_database_names()

            collection_names = await self.db.list_collection_names()

            # Getting list of users
            cursor = self.users_collection.find({})
            entries = await cursor.to_list(length=None)

            users: list[UserDb] = []
            for user in entries:
                users.append(UserDb(**user))

            logging.debug(f"Connected to MongoDB. Available databases: {db_names}")
            logging.debug(f"Connected to MongoDB. Available collections: {collection_names}")
            logging.debug(f"Connected to MongoDB. User Entries: {entries}")

            return {"Databases": db_names, "Collections:": collection_names, 'EntryUser': users}
            
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

    
    async def login_for_token(self, form_data: dict):
        user = await self.authenticator.authenticate_user(form_data.username, form_data.password)
        if not user:
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,
                                detail="Incorrect username or password", headers={"WWW-Authenticate": "Bearer"})
        access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
        access_token = self.authenticator.create_access_token(
            data={"sub": user.username}, expires_delta=access_token_expires)
        
        token = Token(access_token=access_token,token_type='bearer')
        
        return token

        

    async def get_users(self) -> dict:
        users = self.users_collection.find().to_list(length=None)

        return {'user': users}
        pass

    async def create_user(self, user: User, password: str):
        try:
            db_user = self.authenticator.create_db_user(user, password)

            await self.users_collection.insert_one(db_user.model_dump(by_alias=True))

            return {"Message": "Successfully create user"}
        except Exception as ex:
            return {"Message": "Failed to create the user somehow", "Error": f"{ex}"}


