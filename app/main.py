from kivy.lang import Builder
from kivy.uix.screenmanager import Screen, NoTransition, CardTransition
from kivy.core.window import Window
from kivymd.app import MDApp
from app.createAccount import CreateAccountScreen
import kivy.utils

Window.size = [300, 600]
fixed_size = (Window.size[1] * 0.66 * 1, Window.size[1] * 1)
option_list = 'sorry,monopoly,risk,catan,mancala,gameoflife,chess,gloomhaven,scrabble,jenga,codenames'.split(
    ',')


class HomeScreen(Screen):
    pass


class CreateAGroupScreen(Screen):
    current_progress_bar_window_value = 0

    def __init__(self, **kwargs):
        super(CreateAGroupScreen, self).__init__(**kwargs)

    def generate_search_game_options(self, value):
        # filtered_option_list = list(set(option_list + value[:value.rfind(' ')].split(' ')))
        # val = value[value.rfind(' ') + 1:]
        # if not val:
        #     return
        # try:
        #     option_data = []
        #     for i in range(len(option_list)):
        #         word = [word for word in option_list if word.startswith(val)][0][len(val):]
        #         if not word:
        #             return
        #         if self.text + word in option_list:
        #             if self.text + word not in app.option_data:
        #                 popped_suggest = option_list.pop(option_list.index(str(self.text + word)))
        #                 app.option_data.append(popped_suggest)
        #         app.update_data(app.option_data)
        #
        #     except IndexError:
        #
        #         pass
        return


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

    def change_screen(self, screen_name, direction='left', mode=""):
        # Get the screen manager from the kv file
        screen_manager = self.root.ids['screen_manager']
        # print(direction, mode)
        # If going left, change the transition. Else make lleft the default
        if direction == 'left':
            mode = "push"
        elif direction == 'right':
            mode = 'pop'
        elif direction == "None":
            screen_manager.transition = NoTransition()
            screen_manager.current = screen_name
            return

        screen_manager.transition = CardTransition(direction=direction, mode=mode)

        screen_manager.current = screen_name


if __name__ == "__main__":
    MyApp().run()
