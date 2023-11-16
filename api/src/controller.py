
from passlib.context import CryptContext
from fastapi.security import OAuth2PasswordBearer
from motor.motor_asyncio import AsyncIOMotorCollection, AsyncIOMotorClient


from model.User import User
from api.src.constance import ALGORITHM
from api.src.user_authenticator import Authenticator


class Controller():

    def __init__(self, db: AsyncIOMotorClient) -> None:

        pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
        oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")
        
        self.authenticator = Authenticator()
        self.authenticator.initialize(pwd_context, oauth2_scheme)
        
        self.init_collections(db)


    def init_collections(self, db: AsyncIOMotorClient):
        self.users_collection: AsyncIOMotorCollection = db["users"]

        self.users_collection.create_index("username", unique=True)

        self.groups_collection = db["groups"]
        self.join_group_requests_collection = db["joinGroupRequests"]
        self.local_events_collection = db["localEvents"]
        self.boardgames_collection = db["boardgames"]


    def create_user(self, user: User, password: str):
        try:
            db_user = self.authenticator.create_db_user(user, password)

            self.users_collection.insert_one(db_user.dict(by_alias=True))

            return {"Message": "Successfully create user"}
        except Exception as ex:
            return {"Message": "Failed to create the user somehow", "Error": f"{ex}"}

