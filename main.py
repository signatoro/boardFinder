# import src.view
# from src.controller import Controller


import uvicorn
from fastapi import FastAPI
from api.view import APIEndpoints


app = FastAPI()
api_endpoints = APIEndpoints()
app.include_router(api_endpoints.router)


def start_program():
    uvicorn.run("main:app", port=8000, reload="True") # host="10.110.177.171",
    return 0


@app.get("/")
def home_page():
    return {"Message": "You Made"}


if __name__ == "__main__":
    start_program()
