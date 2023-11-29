

from bson import ObjectId
from pydantic import BaseModel, Field



class BoardGame(BaseModel):

    play_time: int
    max_players: int

    title: str
    image_path: str
    general_description: str
    main_description: str
    tutorial_video_link: str

    tags: list[str]
    helpful_links: list[str]

    def __init__(self, **data):
        super().__init__(**data)



class BoardGameDB(BoardGame):

    # Using Field to provide a default value for __id
    id: ObjectId = Field(default_factory=ObjectId, alias="_id")

    def __init__(self, **data):
        super().__init__(**data)

    class Config:
        # Autogenerate ID field
        arbitrary_types_allowed = True
        json_encoders = {ObjectId: str}

class BoardGameCard(BaseModel):

    id: str

    title: str
    image_path: str
    general_description: str

    tags: list[str]
    def __init__(self, **data):
        super().__init__(**data)
        
    

    