import asyncio
import logging
from typing import Any
from jose import JWTError, jwt
from datetime import datetime, timedelta
from passlib.context import CryptContext
from motor.motor_asyncio import AsyncIOMotorCollection
from fastapi import Depends, FastAPI, HTTPException, status
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm


from model.User import User, UserDb
from api.src.constance import ALGORITHM, SECRET_KEY, ACCESS_TOKEN_EXPIRE_MINUTES


class Authenticator(object):
    _instance = None

    _initialized: bool = False

    user_collection: AsyncIOMotorCollection

    # Password Encryption Objects
    pwd_context: CryptContext
    oauth2_scheme: OAuth2PasswordBearer



    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super(Authenticator, cls).__new__(cls, *args, **kwargs)
        
        return cls._instance
    

    def initialize(cls, pwd_context: CryptContext, oauth2_scheme: OAuth2PasswordBearer, user_collection: AsyncIOMotorCollection):
        cls.pwd_context = pwd_context
        cls.oauth2_scheme = oauth2_scheme
        cls.user_collection = user_collection

        cls._initialized = True

    
    def create_db_user(cls, user: User, plain_pass: str) -> UserDb:
        '''
        This method takes in the user information and creates a UserDb object and return is
        '''
        
        if not cls._initialized:
            raise Exception("Authenticator has not been Initialized")
        
        user_db = UserDb(username=user.username,
                         email=user.email,
                         phone_number=user.phone_number,
                         disable=user.disable,
                         hashed_password=cls.get_password_hashed(plain_pass))
        return user_db

    def verify_pass(cls, plain_pass: str, hashed_pass: str) -> bool:
        if not cls._initialized:
            raise Exception("Authenticator has not been Initialized")
        
        return cls.pwd_context.verify(plain_pass, hashed_pass)
    
    def get_password_hashed(cls, plain_pass: str) -> str:
        if not cls._initialized:
            raise Exception("Authenticator has not been Initialized")
        
        return cls.pwd_context.hash(plain_pass)
    
    async def get_user(cls, username: str) -> UserDb:
        if not cls._initialized:
            raise Exception("Authenticator has not been Initialized")
        try:
            raw_user = await cls.user_collection.find_one({'username': username})

            if raw_user:
                return UserDb(**raw_user)
            
            return None
        except Exception as ex:
            logging.error(f"An error occurred while getting user: {username}. Error: {ex}")
            raise Exception(f"An error occurred while getting user: {username}. Error")
    
    async def authenticate_user(cls, username: str, plain_pass: str):

        user = await cls.get_user(username=username)
        

        if not user:
            return False
        if not cls.verify_pass(plain_pass=plain_pass, hashed_pass=user.hashed_password):
            return False
        
        return user
    
    def create_access_token(cls, data: dict, expires_delta: timedelta or None = None) -> str:
        temp_encode = data.copy()

        if expires_delta:
            expire = datetime.utcnow() + expires_delta
        else:
            expire = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
        
        temp_encode.update({'exp': expire})
        encoded_jw_token = jwt.encode(temp_encode, SECRET_KEY, algorithm=ALGORITHM)

        return encoded_jw_token

    async def get_current_user(cls, token: str = Depends(lambda: Authenticator.oauth2_scheme)) -> UserDb:
        credential_exception = HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,
                                         detail="Could not validate credentials", headers={"WWW-Authenticate": "Bearer"})
        username: str = ''
        try: 
            payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
            username: str = payload.get("sub")
            if username is None:
                raise credential_exception
            
        except JWTError as ex:
            logging.error(f"There was an error while trying to get jwt token payload. {ex}")

        user = cls.get_user(username=username)

        if user is None:
            raise credential_exception
        
        return user
    
    async def get_current_active_user(cls, current_user: UserDb= Depends(get_current_user)) -> UserDb:
        if current_user.disable:
            raise HTTPException(status_code=400, detail="User is Inactive")
        
        return current_user

        

    

    

