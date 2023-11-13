
from fastapi import APIRouter


from model.User import User


class APIEndpoints():

    router: APIRouter = APIRouter(
        prefix='/boards',
        tags=['Board Apps']
    )



    def __init__(self) -> None:
        self.router.add_api_route("/", self.get_website, methods=["GET"])
        self.router.add_api_route("/user", self.get_users, methods=["GET"])
        self.router.add_api_route("/user", self.add_user, methods=["POST"])


        self.user_list: list[User] = []


    def get_website(self):
        return {"Message": "Hello World"}
    

    def add_user(self, user:User):
        self.user_list.append(user)

        return {"Message": "User Added successfully"}

    def get_users(self):

        return {"Message": self.user_list}
        


