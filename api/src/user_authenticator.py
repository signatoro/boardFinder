from typing import Any
from jose import JWTError, jwt
from datetime import datetime, timedelta
from passlib.context import CryptContext
from fastapi import Depends, FastAPI, HTTPException, status
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm


from model.User import User, UserDb
from api.src.constance import ALGORITHM, SECRET_KEY, ACCESS_TOKEN_EXPIRE_MINUTES


class Authenticator(object):
    _instance = None

    _initialized: bool = False

    # Password Encryption Objects
    pwd_context: CryptContext
    oauth2_scheme: OAuth2PasswordBearer

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super(Authenticator, cls).__new__(cls, *args, **kwargs)
        
        return cls._instance
    

    def initialize(cls, pwd_context: CryptContext, oauth2_scheme: OAuth2PasswordBearer):
        cls.pwd_context = pwd_context
        cls.oauth2_scheme = oauth2_scheme

        cls._initialized = True

    def verify_pass(cls, plain_pass: str, hashed_pass: str) -> bool:
        if not cls._initialized:
            raise Exception("Authenticator has not been Initialized")
        
        return cls.pwd_context.verify(plain_pass, hashed_pass)
    
    def get_password_hashed(cls, plain_pass: str) -> str:
        if not cls._initialized:
            raise Exception("Authenticator has not been Initialized")
        
        return cls.pwd_context.hash(plain_pass)
    
    def get_user(cls, db: Any, username: str):
        if not cls._initialized:
            raise Exception("Authenticator has not been Initialized")
        
        # TODO: Pull from the Data Base
        pass


    def create_db_user(cls, user: User, plain_pass: str) -> UserDb:
        if not cls._initialized:
            raise Exception("Authenticator has not been Initialized")
        
        user_db = UserDb(**user, hashed_password=cls.get_password_hashed(plain_pass))
        return user_db
        

    

    

