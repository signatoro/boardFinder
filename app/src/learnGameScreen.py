from kivymd.uix.list import OneLineListItem
from kivymd.uix.screen import MDScreen
from kivymd.uix.button import MDFlatButton

from src.gameCard import GameCard

from kivy.lang import Builder

# Builder.load_file('/kv')
class LearnGameScreen(MDScreen):
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
        # print("Hello 2, I am Learning the screen")
        game_card = GameCard(title="Catan")
        game_card.pre_load()
        self.ids.game_results.add_widget(game_card)

        game_card1 = GameCard(title="Risk")
        game_card1.pre_load()
        self.ids.game_results.add_widget(game_card1)

        game_card2 = GameCard(title="Monopoly")
        game_card2.pre_load()
        self.ids.game_results.add_widget(game_card2)

        self.game_card_list["Catan"] = game_card
        self.game_card_list["Risk"] = game_card1
        self.game_card_list["Monopoly"] = game_card2


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



