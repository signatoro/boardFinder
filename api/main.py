
import uvicorn
from fastapi import FastAPI
from motor.motor_asyncio import AsyncIOMotorClient

import sys
sys.path.append('/app')

from src.view import APIEndpoints
from src.controller import Controller


MONGO_URI = "mongodb://localhost:27017"
MONGO_DB_NAME = "boardFinderDb"


client = AsyncIOMotorClient(MONGO_URI)
db = client[MONGO_DB_NAME]
app = FastAPI()
controller = Controller(db)
api_endpoints = APIEndpoints(controller)
app.include_router(api_endpoints.router)

def start_program():

    uvicorn.run("main:app", host="10.110.177.171", port=8000, reload="True")

    return 0

# @app.get("/")
# def home_page():
#     return {"Message": "You Made"}


if __name__ == "__main__":
    start_program()
    
