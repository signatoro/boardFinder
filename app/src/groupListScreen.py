from kivymd.uix.list import OneLineListItem
from kivymd.uix.screen import MDScreen
from kivymd.uix.button import MDFlatButton

from src.groupListCard import GroupListCard

from kivy.lang import Builder

# Builder.load_file('/kv')
class GroupListScreen(MDScreen):
    group_lists = {}

    def on_pre_enter(self, *args):

        self.add_game_card()
        

        # print("Hello 1, I am Learning the screen")
        return super().on_pre_enter(*args)

    def load_depends(self, load_deps=None):
        #TODO call the endpoint to get data
        self.add_game_card()
        pass
    


    def add_game_card(self):
        self.ids.group_list.clear_widgets()

        group_card_2 = GroupListCard(
            title="Scott's Group",
            description="By the end of it we might hate each other, but boy will we have fun!",
            user_status="Request Pending",
            month='2',
            dow='Saturday',
            day='5',
            time="5:30 pm",
            location="Library, Boston MA",
            image_path='images/pikachu.jpg',
            session_length="4 - 6 Hrs",
            participant='1/4 Attending',
        )
        print ("here 1")

        self.ids.group_list.add_widget(group_card_2)
        self.group_lists["Scott's Group"] = (group_card_2)

        group_card_3 = GroupListCard(
            title="Matty's Group",
            description="We give free stuff!! Please come! Free food, water, new dice set!!! ~Join now~",
            user_status="Request Pending",
            month='1',
            dow='Friday',
            day='0',
            time="1:30 pm",
            location="Library, Boston MA",
            image_path='images/piplup.jpg',
            session_length="4 - 6 Hrs",
            participant='3/6 Attending',
        )

        self.ids.group_list.add_widget(group_card_3)
        self.group_lists["Matty's Group"] = (group_card_3)

        group_card_4 = GroupListCard(
            title="Strategic Board Gamers",
            description="Love strategy games? Join us for evenings filled with strategic board games and fun!",
            user_status="Request Pending",
            month='2',
            dow='Thursday',
            day='9',
            time="6:00 pm",
            location="Game Haven, Denver CO",
            image_path='images/strategic_board_games.jpg',
            session_length="2 - 4 Hrs",
            participant='4/6 Attending',
        )
        self.ids.group_list.add_widget(group_card_4)
        self.group_lists["Strategic Board Gamers"] = group_card_4

        # Group 5
        group_card_5 = GroupListCard(
            title="Dice Masters Collective",
            description="Passionate about dice games? Join us for epic battles and dice-rolling excitement!",
            user_status="Invited",
            month='3',
            dow='Saturday',
            day='17',
            time="2:30 pm",
            location="Game Lounge, Portland OR",
            image_path='images/dice_masters.jpg',
            session_length="2 - 3 Hrs",
            participant='3/5 Attending',
        )
        self.ids.group_list.add_widget(group_card_5)
        self.group_lists["Dice Masters Collective"] = group_card_5

        # Group 6
        group_card_6 = GroupListCard(
            title="Board Game Enthusiasts",
            description="Calling all board game enthusiasts! Join us for a mix of classic and modern board games.",
            user_status="Member",
            month='4',
            dow='Friday',
            day='2',
            time="7:00 pm",
            location="Tabletop Tavern, Dallas TX",
            image_path='images/board_game_enthusiasts.jpg',
            session_length="3 - 5 Hrs",
            participant='6/8 Attending',
        )
        self.ids.group_list.add_widget(group_card_6)
        self.group_lists["Board Game Enthusiasts"] = group_card_6

        # Group 7
        group_card_7 = GroupListCard(
            title="Card Game Crew",
            description="Join our card game crew for evenings filled with card games, laughter, and friendly competition!",
            user_status="Request Pending",
            month='5',
            dow='Wednesday',
            day='14',
            time="6:30 pm",
            location="Card Kingdom, Seattle WA",
            image_path='images/card_game_crew.jpg',
            session_length="2 - 3 Hrs",
            participant='5/7 Attending',
        )
        self.ids.group_list.add_widget(group_card_7)
        self.group_lists["Card Game Crew"] = group_card_7

        # Group 8
        group_card_8 = GroupListCard(
            title="Family Board Gaming",
            description="Family-friendly board gaming fun! Bring your loved ones for a night of board games and bonding.",
            user_status="Invited",
            month='6',
            dow='Sunday',
            day='23',
            time="4:00 pm",
            location="Family Game House, Orlando FL",
            image_path='images/family_board_gaming.jpg',
            session_length="2 - 4 Hrs",
            participant='4/6 Attending',
        )
        self.ids.group_list.add_widget(group_card_8)
        self.group_lists["Family Board Gaming"] = group_card_8

        # Group 9
        group_card_9 = GroupListCard(
            title="Classic Board Games Night",
            description="Rediscover the joy of classic board games! Join us for a night of nostalgia and friendly competition.",
            user_status="Member",
            month='7',
            dow='Tuesday',
            day='5',
            time="7:30 pm",
            location="Vintage Game Cafe, Chicago IL",
            image_path='images/classic_board_games.jpg',
            session_length="2 - 3 Hrs",
            participant='7/10 Attending',
        )
        self.ids.group_list.add_widget(group_card_9)
        self.group_lists["Classic Board Games Night"] = group_card_9

        print ("here 2")


        # print("Hello 2, I am Learning the screen")
        # game_card = GameCard(title="Catan")
        # game_card.pre_load()
        # self.ids.game_results.add_widget(game_card)

        # game_card1 = GameCard(title="Risk")
        # game_card1.pre_load()
        # self.ids.game_results.add_widget(game_card1)

        # game_card2 = GameCard(title="Monopoly")
        # game_card2.pre_load()
        # self.ids.game_results.add_widget(game_card2)

        # self.game_card_list["Catan"] = game_card
        # self.game_card_list["Risk"] = game_card1
        # self.game_card_list["Monopoly"] = game_card2




    def search_games(self, text):
        # if there is an empty field, clear widgets
        #if text == "":
        #    self.ids.search_board_game.clear_widgets()
        #    return

        # Clear previous search results
        
        self.ids.search_board_game.clear_widgets()
        self.ids.group_list.clear_widgets()

        # Filter data based on the search text
        search_results = [item for item in self.group_lists.keys() if item.lower().startswith(text.lower())]

        # Display the filtered results
        for result in search_results:
            game_card = self.group_lists[result]
            # game_card.pre_load()
            self.ids.group_list.add_widget(game_card)



