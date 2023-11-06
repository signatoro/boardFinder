
from model.User import User

class BoardGameTypes(enumerate):
    STRATEGY= "strategy"
    # TODO: Fill in the rest


class FindGroupRequest():

    user: User
    game_type_pref: list[BoardGameTypes]
    

    def __init__(self) -> None:
        pass
