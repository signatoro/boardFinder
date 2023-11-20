from kivy.lang import Builder
from kivy.uix.screenmanager import Screen, NoTransition, SlideTransition
from kivy.core.window import Window
from kivymd.app import MDApp
from kivy.clock import Clock
from createAccountScreen import CreateAccountScreen
from createGroup import CreateGroupScreen
import kivy.utils
import createAccountScreen

from src.gameCard import GameCard
from src.learnGameScreen import LearnGameScreen
from src.boardGameScreen import BoardGameScreen

import time


class HomeScreen(Screen):
    pass


# The main application
class MyApp(MDApp):

    lastUserResize = 0
    lastRatioResize = 0
    searched_games = []
    returned_games_to_display = []

    def build(self):
        Window.minimum_width = 400
        Window.minimum_height = 600
        self.lastRatioResize = time.time()-2
        self.lastRatioResize = time.time()-2
        #self.forceWindowRatio()
        self.title = 'BoardGame Group Finder'
        self.theme_cls.primary_palette = "Teal"
        # self.theme_cls.theme_style = "Dark"
        Window.bind(on_resize=self.userResize)
        return Builder.load_file("main.kv")  # GUI

    def change_screen(self, screen_name, direction='left', mode="", load_deps=None):
        # Get the screen manager from the kv file
        screen_manager = self.root.ids['screen_manager']
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

    def userResize(self, *args):
        #print('a')
        if self.lastUserResize + 0.3 < time.time():
            #print('b')
            Clock.schedule_once(self.forceWindowRatio, 0.1)
            self.lastUserResize = time.time()
        return True

    def forceWindowRatio(self, *args):
        #print('c')
        if self.lastUserResize + 0.3 > time.time():
            Clock.schedule_once(self.forceWindowRatio, 0.1)
            return
        if self.lastRatioResize + 0.3 < time.time():
            #print('d')
            self.lastRatioResize = time.time()
            Window.size_hint = ((2/3), 1)
            averageSize = (Window.size[0] + Window.size[1]) / 2
            Window.size = (averageSize * 2 * 2 / 5, averageSize * 2 * 3 / 5)
        return True


if __name__ == "__main__":
    MyApp().run()
