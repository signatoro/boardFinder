
import asyncio
import logging
import uvicorn
from fastapi import FastAPI
from motor.motor_asyncio import AsyncIOMotorClient


from api.src.view import APIEndpoints
from api.src.controller import Controller


MONGO_ADDRESS = '10.110.177.171'
MONGO_PORT = 27017
MONGO_DB_NAME = 'boardFinder_db'


def start_program():
    # logger = logging.getLogger(__name__)

    # # Configure the logging level
    # logger.setLevel(logging.DEBUG)

    # # Create a console handler
    # console_handler = logging.StreamHandler()

    # # Create a formatter and set it on the console handler
    # formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
    # console_handler.setFormatter(formatter)

    # # Add the console handler to the logger
    # logger.addHandler(console_handler)

    uvicorn.run("main:run_program", host="0.0.0.0", port=8000, reload="True", factory=True)

    return 0

def run_program():
    console_handler = logging.StreamHandler()
    file_handler = logging.FileHandler(filename="logs/log.log")

    logging.basicConfig(format='%(levelname)s [%(asctime)s]: %(message)s (Line: %(lineno)d [%(filename)s])',
                        datefmt='%Y.%m.%d %I:%M:%S %p',
                        # filename="logs/log.log",
                        # filemode='w',
                        level=logging.DEBUG,
                        handlers=[console_handler, file_handler])

    
    # Setting Up Logging
    logging.debug("Creating FastApi App")
    app = FastAPI()
    controller = Controller()
    api_endpoints = APIEndpoints(controller)
    app.include_router(api_endpoints.router)

    logging.debug("Started connection to db")

    controller.client = AsyncIOMotorClient(host=MONGO_ADDRESS, port=MONGO_PORT)
    controller.db = controller.client[MONGO_DB_NAME]

    loop = asyncio.get_event_loop()
    loop.create_task(controller.init_collections())

    return app

if __name__ == "__main__":
    start_program()
    
