
from enum import Enum
from pydantic import BaseModel

from model.User import User

class BoardGameTypes(Enum):
    STRATEGY= "strategy"
    # TODO: Fill in the rest


class FindGroupRequest():

    user: User
    game_type_pref: list[BoardGameTypes]
    # TODO: Figure out if I need custom objects for times available

    def __init__(self, **data):
        super().__init__(**data)
        pass
