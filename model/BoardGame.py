
from pydantic import BaseModel

class BoardGame(BaseModel):

    __id: int

    play_time: int
    max_players: int

    title: str
    image_path: str
    general_description: str
    tutorial_video_link: str

    tags: list[str]
    helpful_links: list[str]

    def __init__(self, **data):
        super().__init__(**data)
        pass

    