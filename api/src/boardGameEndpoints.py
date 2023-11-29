
import json
import logging
from fastapi import APIRouter

from api.src.controller import Controller
from model.BoardGame import BoardGame

class BoardGameEndpoints():

    router: APIRouter = APIRouter(prefix='/boardFinder', tags=["Board Games"])

    def __init__(self, controller) -> None:
        self.controller: Controller = controller
        self.create_endpoints()

    def create_endpoints(self):
        self.router.add_api_route("/boardgames", self.get_board_games, methods=["GET"])
        self.router.add_api_route("/boardgames", self.add_board_games, methods=["POST"])
        self.router.add_api_route("/boardgames/{id}", self.get_board_game, methods=["GET"])
        self.router.add_api_route("/boardgames/{id}", self.delete_board_game, methods=["DELETE"])

    # @router.get("/boardgames")
    async def get_board_games(self):
        try:
            logging.debug("Here Endpoint 1")
            return await self.controller.get_board_games()
        except Exception as ex:
            return {"Error": "An Error occurred while trying to add a board game.", "Error Message": f"{ex}"}
    
    # @router.post('/boardgames')
    async def add_board_games(self, board_games: list[BoardGame]):

        try:
            for board_game in board_games:
                await self.controller.add_board_game(board_game)

            return {"Message": "Your Board game was Successfully added!"}
        except Exception as ex:
            return {"Error": "An Error occurred while trying to add a board game.", "Error Message": f"{ex}"}

    # @router.get('/boardgames/{id}')
    async def get_board_game(self, id: str):

        try: 
            return await self.controller.get_board_game(id)
        except Exception as ex:
            return {"Error": f"An Error occurred while trying to get board game {id}", "Error Message": f"{ex}"}
    
    # boardfinder/boardgames/{id}
    async def delete_board_game(self, id:str):
        try:
            if await self.controller.delete_board_game(id):
                return {"Message": "Successfully deleted board game"}
        except Exception as ex:
            return {"Error": f"There was an error {ex}"}

