from pydantic import BaseModel


class User(BaseModel):
    
    username: str
    email: str or None
    phone_number: str or None


class UserDb(User):

    id: int

    hashed_password: str

    owned_groups_list: list[int]
    joined_groups_list: list[int]
    requested_group_list: list[int]
    