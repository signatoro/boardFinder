from pydantic import BaseModel


class User(BaseModel):

    username: str = None
    email: str 
    password: str

    __owned_groups_list: list
    __joined_groups_list: list

    def __init__(self, **data):
        super().__init__(**data)
        pass