from kivy.lang import Builder
from kivy.uix.screenmanager import Screen, NoTransition, SlideTransition
from kivy.core.window import Window
from kivymd.app import MDApp
from createAccountScreen import CreateAccountScreen
from createGroup import CreateGroupScreen
import kivy.utils
import createAccountScreen

from src.gameCard import GameCard
from src.learnGameScreen import LearnGameScreen
from src.boardGameScreen import BoardGameScreen

# Window.size = [300, 600]
# fixed_size = (Window.size[1] * 0.66 * 1, Window.size[1] * 1)
option_list = 'sorry,monopoly,risk,catan,mancala,gameoflife,chess,gloomhaven,scrabble,jenga,codenames'.split(
    ',')


class HomeScreen(Screen):
    pass


# Set minimum window size for desktop and mobile
# Window.minimum_width = fixed_size[0]
# Window.minimum_height = fixed_size[1]
# Window.size = fixed_size


# The main application
class MyApp(MDApp):
    
    searched_games = []
    returned_games_to_display = []

    def build(self):
        Window.size = (Window.size[1] * .55, Window.size[1] * 1)
        self.title = 'BoardGame Group Finder'
        self.theme_cls.primary_palette = "Teal"
        return Builder.load_file("main.kv")  # GUI

    def change_screen(self, screen_name, direction='left', mode="", load_deps=None):
        # Get the screen manager from the kv file
        screen_manager = self.root.ids['screen_manager']
        # print(direction, mode)
        # If going left, change the transition. Else make left the default
        if direction == 'left':
            mode = "push"
        elif direction == 'right':
            mode = 'pop'
        elif direction == "None":
            screen_manager.transition = NoTransition()
            screen_manager.current = screen_name
            return

        if load_deps: 
            screen_manager.get_screen(screen_name).load_depends(load_deps)


        screen_manager.transition = SlideTransition(direction=direction)  # mode=mode)

        screen_manager.current = screen_name


if __name__ == "__main__":
    MyApp().run()
