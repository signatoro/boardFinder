
import uvicorn
from fastapi import FastAPI
from motor.motor_asyncio import AsyncIOMotorClient


from api.src.view import APIEndpoints
from api.src.controller import Controller


MONGO_URI = "mongodb://mongodb:27017"
MONGO_DB_NAME = "boardFinderDb"


client = AsyncIOMotorClient(MONGO_URI)
db = client[MONGO_DB_NAME]
app = FastAPI()
controller = Controller(db)
api_endpoints = APIEndpoints(controller)
app.include_router(api_endpoints.router)

def start_program():

    # TODO: Ok so you need to start with setting up the getting the data base async using the chatgpt stuff
    # Then you need to ping it and make sure that it is connected
    # Then Start making the user work


    print(f'\n\n\nPinging \n\n\n')

    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload="True")

    return 0

# @app.get("/")
# def home_page():
#     return {"Message": "You Made"}


if __name__ == "__main__":
    start_program()
    
