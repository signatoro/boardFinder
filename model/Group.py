
from model.User import User
from model.JoinGroupRequest import JoinGroupRequest


class Group():


    title: str
    image: str # This will be the file path to the image that will be displayed 
    description: str
    addition_information: str

    # TODO: Add meeting time

    owner: User
    
    accepted_user_list: list[User]
    join_request_list: list[JoinGroupRequest]

    # TODO: Decide what tags are.
    tag_list: list[str]

    def __init__(self) -> None:
        pass