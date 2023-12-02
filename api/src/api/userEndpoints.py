
from fastapi import APIRouter, Depends

# from api.src.router.UserAPIRouter import UserAPIRouter
from api.src.controller import Controller
from api.src.depends.deps import get_current_active_user

class UserEndpoints():

    router = APIRouter(prefix="/boardFinder", tags=['User'])


    def __init__(self, contoller: Controller) -> None:
        self.create_routes()

    def create_routes(self):
        self.router.add_api_route("/user", self.get_user, methods=["GET"])

    def get_user(self, user = Depends(get_current_active_user)):
        return {"Message": f"This worked {user}"}