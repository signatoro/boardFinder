from kivymd.uix.screen import MDScreen
from kivymd.uix.button import MDFlatButton

from src.gameCard import GameCard

from kivy.lang import Builder

# Builder.load_file('/kv')
class LearnGameScreen(MDScreen):

    def on_pre_enter(self, *args):

        self.add_elements()
        

        print("Hello 1, I am Learning the screen")
        return super().on_pre_enter(*args)
    

    def add_elements(self):
        for x in range(3):
            self.add_game_card()


    def add_game_card(self):
        print("Hello 2, I am Learning the screen")
        game_card = GameCard(title="Rishav Sucks")
        self.ids.game_results.add_widget(game_card)
        print(self.ids)
