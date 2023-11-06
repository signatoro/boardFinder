

from model.User import User

class JoinGroupRequest():

    user: User
    message: str
    time_sent: str

    def __init__(self) -> None:
        pass