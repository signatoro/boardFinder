
from model.Group import Group

class User():

    username: str = None
    email: str 
    password: str

    owned_groups_list: list[Group]
    joined_groups_list: list[Group]

    def __init__(self):
        pass