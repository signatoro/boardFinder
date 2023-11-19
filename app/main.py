from kivy.lang import Builder
from kivy.uix.screenmanager import Screen, NoTransition, CardTransition, SlideTransition
from kivy.core.window import Window
from kivymd.app import MDApp
from app.createAccount import CreateAccountScreen
from app.createGroup import CreateGroupScreen
import kivy.utils

Window.size = [300, 600]
fixed_size = (Window.size[1] * 0.66 * 1, Window.size[1] * 1)

class HomeScreen(Screen):
    pass


# Set minimum window size for desktop and mobile
Window.minimum_width = fixed_size[0]
Window.minimum_height = fixed_size[1]
Window.size = fixed_size


# The main application
class MyApp(MDApp):
    fixed_size = (Window.size[1] * 0.66 * 1, Window.size[1] * 1)
    searched_games = []
    returned_games_to_display = []

    def build(self):
        Window.bind(on_resize=self.reSize)
        self.title = 'BoardGame Group Finder'
        self.theme_cls.primary_palette = "Teal"
        return Builder.load_file("main.kv")  # GUI

    def reSize(*args):
        # fixed_size = (Window.size[1] * 0.66, Window.size[1])
        Window.size = fixed_size
        return True

    def change_screen(self, screen_name, direction='left'):
        # Get the screen manager from the kv file
        screen_manager = self.root.ids['screen_manager']
        # print(direction, mode)
        # If going left, change the transition. Else make lleft the default

        if direction == "None":
            screen_manager.transition = NoTransition()
            screen_manager.current = screen_name
            return

        screen_manager.transition = SlideTransition(direction=direction)

        screen_manager.current = screen_name


if __name__ == "__main__":
    MyApp().run()
