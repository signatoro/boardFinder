from pydantic import BaseModel

from model.User import User

class JoinGroupRequest(BaseModel):

    user: User
    message: str
    time_sent: str

    def __init__(self, **data):
        super().__init__(**data)
        pass