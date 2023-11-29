
import asyncio
import logging
from jose import JWTError, jwt
from fastapi.security import OAuth2PasswordRequestForm
from fastapi import Depends, APIRouter, HTTPException, status

from api.src.controller import Controller
from model.User import User, Token, UserDb
from api.src.user_authenticator import Authenticator
from api.src.constance import ACCESS_TOKEN_EXPIRE_MINUTES, ALGORITHM, SECRET_KEY


class APIEndpoints():

    router: APIRouter = APIRouter(
        prefix='/boards',
        tags=['Board Apps']
    )


    def __init__(self, controller: Controller) -> None:
        self.controller = controller

        self.router.add_api_route("/", self.get_website, methods=["GET"])
        self.router.add_api_route("/login", self.login_user, methods=["POST"], response_model=Token)
        self.router.add_api_route("/user", self.get_users, methods=["GET"])
        self.router.add_api_route("/user", self.add_user, methods=["POST"])
        self.router.add_api_route("/user/me", self.read_users_me, methods=["GET"], response_model=User)


        self.user_list: list[User] = []


    async def get_website(self):
        # logging.info("Get Request")
        try:
            response = await self.controller.check_db_connection()
            # logging.debug(response)
            return {"Message": response}
            return
        except Exception as ex:
            logging.debug(f"\n\n Error: {ex}")
            return {"Error": ex}
        

    async def add_user(self, user: User, password: str):
        return await self.controller.create_user(user, password)
        pass

    async def get_users(self):
        mes = asyncio.run(self.controller.get_users())

        print(mes)

        return {"Message": "Hello"}
    
    # async def login_user(self, form_data: OAuth2PasswordRequestForm = Depends()):
    #     return await self.controller.login_for_token(form_data)


    # async def read_users_me(self, current_user: str = Depends()):
    #     # TODO: oK so you got most of it working and this will probably work once u get it working 
    #     # You need to make it so the fast api docs page requires authentication for calls like this
    #     # Look at the last chat gpt thing and maybe do some more research
    #     return current_user

    


