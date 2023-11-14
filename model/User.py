from pydantic import BaseModel


class User(BaseModel):

    __id: int

    email: str 
    username: str
    password: str
    phone_number: str

    __owned_groups_list: list
    __joined_groups_list: list
    __requested_group_list: list

    def __init__(self, **data):
        super().__init__(**data)
        pass