from kivymd.uix.list import OneLineListItem
from kivymd.uix.screen import MDScreen
from kivymd.uix.button import MDFlatButton

from src.groupCard import GroupCard

from kivy.lang import Builder

# Builder.load_file('/kv')
class GroupListScreen(MDScreen):
    game_card_list = {}

    def on_pre_enter(self, *args):

        self.add_game_card()
        

        # print("Hello 1, I am Learning the screen")
        return super().on_pre_enter(*args)

    def load_depends(self, load_deps=None):
        #TODO call the endpoint to get data
        pass
    


    def add_game_card(self):
        self.ids.game_results.clear_widgets()

        group_card_2 = GroupCard(
            parent=self,
            game_group=None,  # Dummy Group Card
            title="Scott's Group",
            description="By the end of it we might hate each other, but boy will we have fun!",
            user_status="Request Pending",
            month='2',
            day='5',
            time="5:30 pm",
            location="Library, Boston MA",
            image_path='images/pikachu.jpg',
            session_length="4 - 6 Hrs",
            participant='1/4 Attending',
        )

        self.ids.game_results.add_widget(group_card_2)

        group_card_3 = GroupCard(
            parent=self,
            game_group=None,  # Dummy Group Card
            title="Matty's Group",
            description="We give free stuff!! Please come! Free food, water, new dice set!!! ~Join now~",
            user_status="Request Pending",
            month='1',
            day='0',
            time="1:30 pm",
            location="Library, Boston MA",
            image_path='images/piplup.jpg',
            session_length="4 - 6 Hrs",
            participant='3/6 Attending',
        )
        self.ids.game_results.add_widget(group_card_3)

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
        self.ids.game_results.clear_widgets()

        # Filter data based on the search text
        search_results = [item for item in self.game_card_list.keys() if item.lower().startswith(text.lower())]

        # Display the filtered results
        for result in search_results:
            game_card = self.game_card_list[result]
            game_card.pre_load()
            self.ids.game_results.add_widget(game_card)



