from kivymd.uix.screen import MDScreen
from kivymd.uix.button import MDFlatButton

from src.gameCard import GameCard

from kivy.lang import Builder

# Builder.load_file('/kv')
class LearnGameScreen(MDScreen):

    def on_pre_enter(self, *args):

        self.add_game_card()
        

        print("Hello 1, I am Learning the screen")
        return super().on_pre_enter(*args)

    def load_depends(self, load_deps=None):
        #TODO call the endpoint to get data
        pass
    


    def add_game_card(self):
        print("Hello 2, I am Learning the screen")
        game_card = GameCard(title="Rishav Sucks")
        game_card.pre_load()
        self.ids.game_results.add_widget(game_card)

        game_card1 = GameCard(title="Matty Sucks")
        game_card1.pre_load()
        self.ids.game_results.add_widget(game_card1)

        game_card2 = GameCard(title="Scott Sucks")
        game_card2.pre_load()
        self.ids.game_results.add_widget(game_card2)
