from kivy.lang import Builder
from kivy.uix.screenmanager import Screen, NoTransition, CardTransition
from kivy.core.window import Window
from kivymd.app import MDApp
import kivy.utils

fixed_size = (Window.size[1] * 0.66 * 1, Window.size[1] * 1)


class HomeScreen(Screen):
    pass


class CreateAGroupScreen(Screen):
    pass


# Set minimum window size for desktop and mobile
Window.minimum_width = fixed_size[0]
Window.minimum_height = fixed_size[1]
Window.size = fixed_size


# The main application
class MyApp(MDApp):
    fixed_size = (Window.size[1] * 0.66 * 1, Window.size[1] * 1)
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
