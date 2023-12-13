from kivy.lang import Builder
from kivy.uix.screenmanager import NoTransition, SlideTransition
from kivy.core.window import Window
from kivymd.app import MDApp
from kivy.config import Config

from src.createAccountScreen import CreateAccountScreen
from src.signInScreen import SignInScreen
from src.homeScreen import HomeScreen
from src.profileScreen import ProfileScreen
from src.createGroup import CreateGroupScreen
from src.findGroupScreen import FindGroupScreen
from src.groupListCard import GroupListCard
from src.gameCard import GameCard
from src.topBar import TopBar
from src.learnGameScreen import LearnGameScreen
from src.boardGameScreen import BoardGameScreen
from src.gameGroupScreen import GameGroupScreen
from src.groupListScreen import GroupListScreen


import time
from kivy.clock import Clock

Clock.max_iteration = 60


# The main application
class MyApp(MDApp):

    lastResize = 0
    searched_games = []
    returned_games_to_display = []
    groups_list = []
    top_bars = []

    signed_in = False
    username = None
    main_screen_manager = None

    def build(self):
        self.signed_in = False
        self.username = None
        Window.minimum_width = 400
        Window.minimum_height = 600
        # self.lastResize = time.time()-2
        self.force_window_ratio()
        self.title = 'BoardGame Group Finder'
        self.theme_cls.primary_palette = "Teal"
        Config.set('input', 'mouse', 'mouse,multitouch_on_demand')
        # self.theme_cls.theme_style = "Dark"
        # Window.bind(on_resize=self.force_window_ratio)
        return Builder.load_file("kv/main.kv")  # GUI

    def on_start(self):
        self.main_screen_manager = self.root.ids['screen_manager']

    def get_screen_manager(self):
        return self.root.ids['screen_manager']

    def change_screen(self, screen_name, direction='left', mode="", load_deps=None):
        # Get the screen manager from the kv file
        # print(direction, mode)
        # If going left, change the transition. Else make left the default
        if direction == 'left':
            mode = "push"
        elif direction == 'right':
            mode = 'pop'
        elif direction == "None":
            self.main_screen_manager.transition = NoTransition()
            self.main_screen_manager.current = screen_name
            return

        if load_deps:
            if self.main_screen_manager.current_screen.name == 'home_screen' and screen_name == 'game_group_screen':
                # rendering already published group from group card
                self.main_screen_manager.get_screen(screen_name).load_screen_data(load_deps, self.main_screen_manager.current_screen.name)
            elif self.main_screen_manager.current_screen.name == 'create_group_screen' and screen_name == 'game_group_screen':
                # rendering review of group host created
                self.main_screen_manager.get_screen(screen_name).load_depends(load_deps, self.main_screen_manager.current_screen.name)

        self.main_screen_manager.transition = SlideTransition(direction=direction)  # mode=mode)

        self.main_screen_manager.current = screen_name

        for bar in self.top_bars:
            bar.update_actions()

    def force_window_ratio(self, *args):
        if self.lastResize + 0.1 > time.time():
            return
        self.lastResize = time.time()
        Window.size_hint = ((2/3), 1)
        averageSize = (Window.size[0] + Window.size[1]) / 2
        Window.size = (averageSize * 2 * 2 / 5, averageSize * 2 * 3 / 5)
        return True

    def get_screen_name(self):
        if self.root is None or self.root.ids['screen_manager'] is None:
            return ""
        return self.root.ids['screen_manager'].current


    def get_signed_in(self):
        return self.signed_in

    def set_signed_in(self, signed_in):
        self.signed_in = signed_in

    def add_top_bar(self, bar):
        self.top_bars.append(bar)
        bar.update_actions()

    def add_group(self, group):
        self.groups_list.append(group)

    def remove_group(self, group):
        self.groups_list.remove(group)


if __name__ == "__main__":
    MyApp().run()




































