from enum import Enum
from pydantic import BaseModel

from util.EventEnums import Months, Location_Type


class LocalEvent(BaseModel):

    __id: int

    title: str
    event_link: str
    description: str

    location_type: Location_Type

    month: Months
    day: int

    # TODO: figure out how to do this.
    # Time 7:00pm or 11:00am
    time: int
    location: str | None
    

    def __init__(self, **data):
        super().__init(data)
        