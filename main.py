
import asyncio
import logging
import uvicorn
from fastapi import FastAPI
from logging.handlers import RotatingFileHandler
from motor.motor_asyncio import AsyncIOMotorClient
from fastapi.middleware.cors import CORSMiddleware



from api.src.view import APIEndpoints
from api.src.controller import Controller
from api.src.collects import DB_Collections
from api.src.api.userEndpoints import UserEndpoints
from api.src.api.boardGameEndpoints import BoardGameEndpoints
from api.src.api.localEventsEndpoints import LocalEventEndpoints


# MONGO_ADDRESS = '10.110.185.117'
# MONGO_PORT = 27017
# MONGO_DB_NAME = 'boardFinder_db'



def start_program():

    uvicorn.run("main:run_program", host="0.0.0.0", port=8000, reload="True", factory=True)

    return 0

def run_program():

    console_handler = logging.StreamHandler()
    file_handler = RotatingFileHandler(filename="logs/log.log", maxBytes=1e8, backupCount=5)

    logging.basicConfig(format='%(levelname)s [%(asctime)s]: %(message)s (Line: %(lineno)d [%(filename)s])',
                        datefmt='%Y.%m.%d %I:%M:%S %p',
                        # filename="logs/log.log",
                        # filemode='w',
                        level=logging.DEBUG,
                        handlers=[console_handler, file_handler])

    
    # Setting Up Logging
    logging.debug("Creating FastApi App")
    app = FastAPI()

    # Allow all origins (replace "*" with your frontend URL in production)
    origins = ["*"]

    app.add_middleware(
        CORSMiddleware,
        allow_origins=origins,
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    # client = AsyncIOMotorClient(host=MONGO_ADDRESS, port=MONGO_PORT)
    # db = client[MONGO_DB_NAME]

    db_collect = DB_Collections()
    controller = Controller(DB_Collections.client, DB_Collections.db)

    board_game_endpoints = BoardGameEndpoints(controller)
    app.include_router(board_game_endpoints.router)
    
    api_endpoints = APIEndpoints(controller)
    app.include_router(api_endpoints.router)

    user_endpoints = UserEndpoints(controller)
    app.include_router(user_endpoints.router)

    logging.debug("Started connection to db")

    controller.initialize()


    return app

if __name__ == "__main__":
    start_program()
    
