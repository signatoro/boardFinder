
from src.userCard import UserCard
from src.groupCard import GroupCard


class GroupDB():

    pass

class Database():

    _database = None

    __user: dict[str, UserCard] = None
    __groups: dict[str, GroupCard] = None
    __games: dict = None


    def __new__(cls):
        if not cls._database:
            cls._database = super().__new__(cls)
        return cls._database
    
    def __init__(cls): 
        pass



    def initialize(cls):
        cls.__user = {}
        cls.__groups = {}
        cls.__games = {}

        cls.generate_information()

    def generate_information(cls):
        

        pass



    def add_group(cls, groupCard: GroupCard):
        cls.__groups[groupCard.title] = groupCard 

    def get_group(cls, title: str) -> GroupCard:
        return cls.__groups[title]
    
    def add_user(cls, userCard: UserCard):
        cls.__user[userCard.first_name] = userCard

    def get_user(cls, first_name: str):
        return cls.__user[first_name]
    

    