
from pydantic import BaseModel

from util.BoardEnum import BoardGameGenre
from model.User import User


class FindGroupRequest(BaseModel):

    __id: int

    user: User
    game_type_pref: list[BoardGameGenre]

    number_of_player: int

    # TODO: This is cursed 
    days_free: list[list[tuple[int,int]]]

    session_time: tuple[float,float]



    # TODO: Figure out if I need custom objects for times available

    def __init__(self, **data):
        super().__init__(**data)
        pass
