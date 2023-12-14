from kivymd.uix.chip import MDChip
from datetime import time, datetime, timedelta

from src.userCard import UserCard
from src.gameCard import GameCard
from src.groupCard import GroupCard
from src.groupListCard import GroupListCard
from src.gameGroupScreen import GameGroupScreen
from src.boardGameScreen import BoardGameScreen

DAYS = ["monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday"]


class GroupDB():
    pass


class Database():
    __initialize = False
    _database = None

    __user: dict[str, UserCard] = None
    __groups_cards: dict[str, GroupCard] = None
    __groups_screen: dict[str, GameGroupScreen] = None
    __group_list_cards: dict[str, GroupListCard] = None
    __game_data: dict[str, dict] = None

    def __new__(cls):
        if not cls._database:
            cls._database = super().__new__(cls)
        return cls._database

    def __init__(cls):
        pass

    def initialize(cls):
        if not cls.__initialize:
            cls.__user = {}
            cls.__groups_cards = {}
            cls.__groups_screen = {}
            cls.__group_list_cards = {}
            cls.__game_data = {}
            cls.generate_information()
            cls.__initialize = True

    def generate_information(cls):
       
        game1 = {
            "title": "Monopoly",
            "image_path": "images/monopoly.jpg",
            "general_description": "Monopoly is a classic board game that has been entertaining families for generations. It\"s a real estate trading game where players buy, sell, and trade properties to build their real estate empire.",
            "main_description": "Monopoly, the iconic board game, traces its origins back to the early 20th century. Created to illustrate the economic concepts of land grabbing and rent, it has become a staple in households worldwide. The game involves strategy, negotiation, and a bit of luck as players strive to bankrupt their opponents. Roll the dice, move your token, and make strategic decisions to become the ultimate real estate tycoon!",
            "tutorial_video_link": "videos/monopoly_tutorial.mp4",
            "tags": ["Classic", "Real Estate", "Strategy", "Family", "Iconic"],
            "helpful_links": [
            "http://monopoly.com/rules",
            "http://monopolystrategy.com",
            "http://monopolycommunity.com"
            ]
        }
        cls.__game_data["Monopoly"]=game1
        game2 = {
            "title": "Risk",
            "image_path": "images/risk.jpg",
            "general_description": "Risk is a strategic board game of global domination. Players engage in epic battles, deploy armies, and conquer territories in a quest for world domination. Its a game of alliances, betrayals, and calculated risk-taking.",
            "main_description": "Risk, introduced in the 1950s, simulates the complexities of global warfare. The game unfolds on a world map divided into territories, and players use armies to vie for control. Risk requires strategic planning, diplomatic cunning, and the courage to take calculated risks. Forge alliances, break truces, and navigate the treacherous path to victory! The world is your battlefield.",
            "tutorial_video_link": "videos/risk_tutorial.mp4",
            "tags": ["Strategy", "Global Domination", "Alliances", "Classic", "Epic"],
            "helpful_links": [
            "http://riskrules.com",
            "http://riskstrategy.com",
            "http://riskcommunity.com"
            ]
        }
        cls.__game_data["Risk"]=game2
        game3 = {
            "title": "Catan",
            "image_path": "images/catan.jpg",
            "general_description": "Catan, also known as The Settlers of Catan, is a resource management and trading game. Settlers establish colonies on the island of Catan, gather resources, and trade to expand their settlements and cities.",
            "main_description": "Catan, a modern classic in board gaming, transports players to an uninhabited island rich in resources. The game involves resource gathering, trading, and strategic expansion. Players must build roads, settlements, and cities while vying for dominance. Catan\"s modular board ensures a unique experience in each game. Embark on a journey of exploration, negotiation, and clever resource management!",
            "tutorial_video_link": "videos/catan_tutorial.mp4",
            "tags": [
            "Resource Management",
            "Trading",
            "Settlements",
            "Strategy",
            "Classic"
            ],
            "helpful_links": [
            "http://catanrules.com",
            "http://catanstrategy.com",
            "http://catancommunity.com"
            ]
        }
        cls.__game_data["Catan"]=game3
        game4 = {
            "title": "Sorry!",
            "image_path": "images/sorry.jpg",
            "general_description": "Sorry! is a classic board game of sweet revenge. Players race to get their pawns from Start to Home, but the journey is fraught with obstacles and opportunities to send opponents back to the starting line.",
            "main_description": "Sorry!, a delightful game of chance and strategy, takes players on a journey of twists and turns. The goal is simple: get your pawns home before your opponents. However, the path is filled with Sorry cards that allow players to bump, slide, and swap places. It\"s a game of strategy, luck, and the occasional heartfelt apology. Experience the thrill of Sorry! as you race to victory!",
            "tutorial_video_link": "videos/sorry_tutorial.mp4",
            "tags": ["Classic", "Race", "Strategy", "Family", "Apologies"],
            "helpful_links": [
            "http://sorryrules.com",
            "http://sorrystrategy.com",
            "http://sorrycommunity.com"
            ]
        }
        cls.__game_data["Sorry!"]=game4
        game5={
            "title": "Scythe",
            "image_path": "images/scythe.jpg",
            "general_description": "Scythe is a board game set in an alternate history 1920s Eastern Europe. Players control factions vying for control over the mysterious Factory. It combines resource management, area control, and strategic combat.",
            "main_description": "Scythe unfolds in a beautifully crafted world where players navigate the aftermath of the Great War. Factions deploy mechs, harvest resources, and engage in diplomatic maneuvers to dominate the land. Each decision carries weight, and victory requires a delicate balance of expansion and diplomacy. Scythe is a masterpiece of strategy and storytelling, inviting players to shape the destiny of a war-torn world.",
            "tutorial_video_link": "videos/scythe_tutorial.mp4",
            "tags": [
            "Alternate History",
            "Strategy",
            "Mechs",
            "Resource Management",
            "Diplomacy"
            ],
            "helpful_links": [
            "http://scytherules.com",
            "http://scythestrategy.com",
            "http://scythecommunity.com"
            ]
        }
        cls.__game_data["Scythe"]=game5
        game6={
            "title": "Ticket to Ride",
            "image_path": "images/ticket_to_ride.jpg",
            "general_description": "Ticket to Ride is a railway-themed board game where players build train routes to connect cities and complete destination tickets. It\"s a game of strategic planning, blocking opponents, and racing to achieve railway dominance.",
            "main_description": "Ticket to Ride invites players to embark on a cross-country railway adventure. Collect train cards, claim routes, and strategically connect cities to complete destination tickets. The game combines elements of strategy and luck as players race to build the longest routes and fulfill secret objectives. Ticket to Ride is easy to learn but offers depth for strategic mastery. All aboard for an unforgettable journey through the world of railways!",
            "tutorial_video_link": "videos/ticket_to_ride_tutorial.mp4",
            "tags": ["Railway", "Strategy", "Destination Tickets", "Family", "Classic"],
            "helpful_links": [
            "http://tickettoriderules.com",
            "http://tickettoridestrategy.com",
            "http://tickettoridecommunity.com"
            ]
        }
        cls.__game_data["Ticket to Ride"]=game6










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
                md_bg_color="teal"
            ),
            MDChip(
                text=f"Family Friendly",
                text_color=(0, 0, 0, 1),
                md_bg_color="teal"
            ),
            MDChip(
                text=f"21+",
                text_color=(0, 0, 0, 1),
                md_bg_color="teal"
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
        cls.add_game_group_screen(game_group_2)

        pass

    def get_board_game_cards(cls):
        temp = {}
        [temp.update({data['title']: GameCard(**data)}) for data in cls.__game_data.values()]
        return temp
    
    def get_board_game(cls, title: str) -> dict:
        return cls.__game_data[title]

    def add_game_group_screen(cls, group_screen: GameGroupScreen):
        cls.__groups_screen[group_screen.group_title] = group_screen
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
        return temp
    
    def get_group_list_card(cls, title: str) -> list[GroupListCard]:
        return cls.__group_list_cards[title]

    def get_group_list_cards(cls) -> list[GroupListCard]:
        temp = []
        [temp.append(group) for group in cls.__group_list_cards.values()]
        return temp
    


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

        cls.add_group_card(created_group_card)

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
