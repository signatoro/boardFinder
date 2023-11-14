
from pydantic import BaseModel

from model.User import User
from util.DateTimes import Days
from model.BoardGame import BoardGame
from model.JoinGroupRequest import JoinGroupRequest


class Group(BaseModel):

    __id: int

    title: str

    image: str # This will be the file path to the image that will be displayed 
    
    description: str
    addition_information: str

    # Host Information
    name: str
    email: str
    phone_number: str

    owner: User

    # Meeting Info
    recurring: bool
    day: Days

    # TODO: need to figure out what time of data this should be
    time: tuple[int, int]

    location: str

    board_game_list: list [BoardGame]
    
    accepted_user_list: list[int]
    join_request_list: list[int]

    # TODO: Decide what tags are.
    tag_list: list[str]

    def __init__(self, **data) -> None:
        super().__init__(**data)
        