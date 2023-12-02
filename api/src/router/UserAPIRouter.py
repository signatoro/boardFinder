
from enum import Enum
from fastapi import APIRouter, Depends

from api.src.depends.deps import get_current_active_user

class UserAPIRouter(APIRouter):

    def __init__(self, tags: list[str | Enum] | None = None, prefix: str = "", **kwargs):
        super().__init__(tags=tags, prefix=prefix, dependencies=[Depends(get_current_active_user)], **kwargs)
