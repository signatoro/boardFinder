from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.core.window import Window

from home import HomeScreen
from profile import ProfileScreen

fixed_size = (Window.size[1] * 0.66 * 1, Window.size[1] * 1)


# The main application
class MyApp(App):
    def build(self):
        # Set minimum window size for desktop and mobile
        Window.minimum_width = fixed_size[0]
        Window.minimum_height = fixed_size[1]
        Window.size = fixed_size

        # returns a window object with all its widgets
        self.window = BoxLayout(orientation='vertical')
        self.window.cols = 1
        self.window.size_hint = (None, None)  # Disable automatic size_hint
        self.window.width = fixed_size[0]  # Set an initial width
        self.window.height = fixed_size[1]  # Set an initial height
        self.window.pos_hint = {"center_x": 0.5, "center_y": 0.5}

        # Set up screen manager and all screens
        screen_manager = ScreenManager()
        screen_manager.add_widget(HomeScreen(name="home"))
        screen_manager.add_widget(ProfileScreen(name="profile"))
        return screen_manager

    def reSize(*args):
        # fixed_size = (Window.size[1] * 0.66, Window.size[1])
        Window.size = fixed_size
        return True

    Window.bind(on_resize=reSize)


if __name__ == "__main__":
    MyApp().run()
