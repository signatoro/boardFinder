from pydantic import BaseModel

class BoardFilterRequest(BaseModel):

    sessions_length: int | None
    max_player_count: int | None

    genre_list: list | None


    def __init__(self) -> None:
        pass