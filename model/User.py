from pydantic import BaseModel


class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    username: str or None = None


class User(BaseModel):
    
    username: str
    email: str or None = None
    phone_number: str or None = None
    disable: bool or None = False


class UserDb(User):

    hashed_password: str

    owned_groups_list: list[int] = []
    joined_groups_list: list[int] = []
    requested_group_list: list[int] = []
    