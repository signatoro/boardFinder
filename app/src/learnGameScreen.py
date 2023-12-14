from kivy.app import App
from kivymd.uix.list import OneLineListItem
from kivymd.uix.screen import MDScreen
from kivymd.uix.button import MDFlatButton

from src.gameCard import GameCard

from kivy.lang import Builder

# Builder.load_file('/kv')
class LearnGameScreen(MDScreen):
    game_card_list: dict[str: GameCard] = {}

    def on_pre_enter(self, *args):

        self.add_game_card()
        

        # print("Hello 1, I am Learning the screen")
        return super().on_pre_enter(*args)

    def load_depends(self, load_deps=None):
        #TODO call the endpoint to get data
        pass
    


    def add_game_card(self):
        self.ids.game_results.clear_widgets()
        self.game_card_list = App.get_running_app().get_database().get_board_game_cards()

        for card in self.game_card_list.values():
            self.ids.game_results.add_widget(card)

    def search_games(self, text):
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



