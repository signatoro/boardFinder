
from fastapi import APIRouter


from model.User import User
from api.src.controller import Controller

class APIEndpoints():

    router: APIRouter = APIRouter(
        prefix='/boards',
        tags=['Board Apps']
    )



    def __init__(self, controller: Controller) -> None:
        self.controller = controller

        self.router.add_api_route("/", self.get_website, methods=["GET"])
        self.router.add_api_route("/user", self.get_users, methods=["GET"])
        self.router.add_api_route("/user", self.add_user, methods=["POST"])


        self.user_list: list[User] = []


    def get_website(self):
        return {"Message": "Hello World"}
    

    def add_user(self, user: User, password: str):
        return self.controller.create_user(user, password)

    async def get_users(self):
        mes = await self.controller.get_users()

        print(mes)

        return {"Message": "Hellow"}
    
    
        


