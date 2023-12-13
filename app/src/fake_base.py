
from kivymd.uix.chip import MDChip
from datetime import time, datetime, timedelta


from src.userCard import UserCard
from src.groupCard import GroupCard
from src.groupListCard import GroupListCard
from src.gameGroupScreen import GameGroupScreen
DAYS = ["monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday"]

class GroupDB():

    pass



class Database():

    _database = None

    __user: dict[str, UserCard] = None
    __groups_cards: dict[str, GroupCard] = None
    __groups_screen: dict[str, GameGroupScreen] = None
    __group_list_cards: dict[str, GroupListCard] = None
    __games: dict = None


    def __new__(cls):
        if not cls._database:
            cls._database = super().__new__(cls)
        return cls._database
    
    def __init__(cls):
        pass



    def initialize(cls):
        cls.__user = {}
        cls.__groups_cards = {}
        cls.__groups_screen = {}
        cls.__group_list_cards = {}
        cls.__games = {}

        cls.generate_information()

    def generate_information(cls):

        user1 = UserCard(first_name="Matty", last_name="Pizza", avatar_path="images/avatar_stock.png")
        user2 = UserCard(first_name="Alice", last_name="Coders", avatar_path="images/avatar_stock.png")
        user3 = UserCard(first_name="Bob", last_name="Gamer", avatar_path="images/avatar_stock.png")
        user4 = UserCard(first_name="Charlie", last_name="Artist", avatar_path="images/avatar_stock.png")
        user5 = UserCard(first_name="Eva", last_name="Reader", avatar_path="images/avatar_stock.png")
        user6 = UserCard(first_name="David", last_name="Traveler", avatar_path="images/avatar_stock.png")
        user7 = UserCard(first_name="Sophie", last_name="Musician", avatar_path="images/avatar_stock.png")
        user8 = UserCard(first_name="John", last_name="Adventurer", avatar_path="images/avatar_stock.png")
        user9 = UserCard(first_name="Lily", last_name="Foodie", avatar_path="images/avatar_stock.png")
        user10 = UserCard(first_name="Max", last_name="Explorer", avatar_path="images/avatar_stock.png")

        cls.add_user(user1)
        cls.add_user(user2)
        cls.add_user(user3)
        cls.add_user(user4)
        cls.add_user(user5)
        cls.add_user(user6)
        cls.add_user(user7)
        cls.add_user(user8)
        cls.add_user(user1)
        cls.add_user(user9)
        cls.add_user(user10)



        tags_list = [
            MDChip(
                text=f"Competitive",
                text_color=(0, 0, 0, 1),
                md_bg_color = "teal"
            ),
            MDChip(
                text=f"Family Friendly",
                text_color=(0, 0, 0, 1),
                md_bg_color = "teal"
            ),
            MDChip(
                text=f"21+",
                text_color=(0, 0, 0, 1),
                md_bg_color = "teal"
            )
        ]

        game_data = {
            "group_board_games": ["catan", "monopoly"],
            "group_image": "images/piplup.jpg",
            "group_title": "test group",
            "group_general_description": "Come have a grand ol' time with your boi, chef Rish",
            "group_additional_description": "this is addy info",
            "group_mtg_day_and_recurring_info": {"Saturday": True},
            "group_meeting_start_time": "4:00:00 PM",
            "group_meeting_end_time": "8:00:00 PM",
            "group_meeting_location": "BPD",
            "group_max_players": "8",
            "group_host_fname": "alice",
            "group_host_lname": "bobol",
            "group_host_email": "bobol.alice@gmail.com",
            "group_host_phone_num": "911-991-1000",
            "group_tags": tags_list,
            "new_group": False,
            "owner": user1,
            "list_of_members": [user1],
            "list_of_pending": []
        }
        game_group_ = GameGroupScreen(**game_data)
        # game_group_.load_depends(game_data, 'home_screen')

        cls.add_game_group_screen(game_group_)

        # GameGroupScreen instances
        game_data_1 = {
            "group_board_games": ["chess", "scrabble"],
            "group_image": "images/group_image_1.jpg",
            "group_title": "Strategic Game Enthusiasts",
            "group_general_description": "Join us for intense and strategic board gaming sessions. We play a variety of games that challenge the mind and entertain the soul.",
            "group_additional_description": "All skill levels are welcome. Whether you're a seasoned strategist or just getting started, there's a game for everyone.",
            "group_mtg_day_and_recurring_info": {"Friday": True},
            "group_meeting_start_time": "6:00:00 PM",
            "group_meeting_end_time": "10:00:00 PM",
            "group_meeting_location": "Game Haven",
            "group_max_players": "10",
            "group_host_fname": "Alice",
            "group_host_lname": "Coders",
            "group_host_email": "alice.coders@gmail.com",
            "group_host_phone_num": "555-123-4567",
            "group_tags": [],
            "new_group": False,
            "owner": user2,
            "list_of_members": [user1, user3],
            "list_of_pending": [user4],
        }

        game_group_1 = GameGroupScreen(**game_data_1)
        # game_group_1.load_depends(game_data_1, 'home_screen')
        cls.add_game_group_screen(game_group_1)

        # GameGroupScreen instances
        game_data_2 = {
            "group_board_games": ["risk", "ticket to ride"],
            "group_image": "images/group_image_2.jpg",
            "group_title": "Adventure Board Gamers",
            "group_general_description": "Embark on thrilling adventures through board games! Join us for epic journeys, strategic conquests, and exciting quests. All adventurers are welcome!",
            "group_additional_description": "No experience necessary. Whether you're a seasoned explorer or a newcomer, our group is all about fun and camaraderie.",
            "group_mtg_day_and_recurring_info": {"Sunday": True},
            "group_meeting_start_time": "2:00:00 PM",
            "group_meeting_end_time": "6:00:00 PM",
            "group_meeting_location": "Quest Haven",
            "group_max_players": "12",
            "group_host_fname": "Bob",
            "group_host_lname": "Gamer",
            "group_host_email": "bob.gamer@gmail.com",
            "group_host_phone_num": "555-987-6543",
            "group_tags": [],
            "new_group": False,
            "owner": user3,
            "list_of_members": [user1, user2],
            "list_of_pending": [user4, user5],
        }

        game_group_2 = GameGroupScreen(**game_data_2)
        # game_group_2.load_depends(game_data_2, 'home_screen')
        cls.add_game_group_screen(game_group_2)
        

        pass




    def add_game_group_screen(cls, group_screen: GameGroupScreen):
        cls.__groups_screen[group_screen.group_title] = GameGroupScreen
        cls.created_group_cards(group_screen)
    
    def get_game_group_screen(cls, title: str) -> GameGroupScreen:
        return cls.__groups_screen[title]


    def add_group_card(cls, groupCard: GroupCard):
        cls.__groups_cards[groupCard.title] = groupCard 

    def get_group_card(cls, title: str) -> GroupCard:
        return cls.__groups_cards[title]
    
    def get_group_cards(cls) -> list[GroupCard]:
        temp = []
        [temp.append(group) for group in cls.__groups_cards.values()]
        return cls.__groups_cards.values()
    
    def add_user(cls, userCard: UserCard):
        cls.__user[userCard.first_name] = userCard

    def get_user(cls, first_name: str) -> UserCard:
        return cls.__user[first_name]

    
    

    ## OMG This code is a mess
    ## TODO: Clean up code
    
    def created_group_cards(cls, game_group_screen_info: GameGroupScreen):
        dow = ""
        for key in game_group_screen_info.group_mtg_day_and_recurring_info.keys():
            dow = key
        next_date_of_meeting = cls.get_updated_date_of_next_meeting(dow)
        session_length = cls.get_hours_between_times(game_group_screen_info.group_meeting_start_time,
                                                      game_group_screen_info.group_meeting_end_time)

        created_group_card = GroupCard(
            game_group=game_group_screen_info,
            title=game_group_screen_info.group_title,
            description=game_group_screen_info.group_general_description,
            user_status="Open To New Members",
            month=str(next_date_of_meeting.month),
            day=str(int(next_date_of_meeting.day)),
            dow=dow,
            time=f"{game_group_screen_info.group_meeting_start_time} - {game_group_screen_info.group_meeting_end_time}",
            location=game_group_screen_info.group_meeting_location,
            image_path=game_group_screen_info.group_image,
            session_length=f"{str(int(session_length))} Hrs",
            participant=f'1/{game_group_screen_info.group_max_players} Attending',
        )

        cls.__groups_cards[created_group_card.title] = created_group_card

        # adding new group to group list
        created_group_list_card = GroupListCard(
            title=game_group_screen_info.group_title,
            description=game_group_screen_info.group_general_description,
            user_status="Open To New Members",
            month=str(next_date_of_meeting.month),
            day=str(int(next_date_of_meeting.day)),
            dow=dow,
            time=f"{game_group_screen_info.group_meeting_start_time} - {game_group_screen_info.group_meeting_end_time}",
            location=game_group_screen_info.group_meeting_location,
            image_path=game_group_screen_info.group_image,
            session_length=f"{str(int(session_length))} Hrs",
            participant=f'1/{game_group_screen_info.group_max_players} Attending',
        )

        cls.__group_list_cards[created_group_list_card.title] = created_group_list_card

    def get_updated_date_of_next_meeting(self, next_dow):
        current_date = datetime.now()

        current_day = current_date.weekday()

        target_day = DAYS.index(next_dow.lower())

        days_until_next = (target_day - current_day + 7) % 7
        return current_date + timedelta(days=days_until_next)
    
    def get_hours_between_times(self, start_time, end_time):
        time_format = "%I:%M:%S %p"

        datetime1 = datetime.strptime(start_time, time_format)
        datetime2 = datetime.strptime(end_time, time_format)

        time_difference = datetime2 - datetime1

        total_hours = time_difference.total_seconds() / 3600

        return total_hours


    