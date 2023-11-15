from kivy.uix.screenmanager import Screen
from kivy.uix.label import Label
from kivy.uix.button import Button

from helpers import slide_transition_to_screen

# The profile screen
class ProfileScreen(Screen):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        test_label = Label(
            text="Profile",
            font_size=24,
            pos_hint={'center_x': 0.5, 'center_y': 0.7}
        )

        test_button = Button(
            text="Return Home",
            size_hint=(None, None),
            size=(100, 50),
            pos_hint={'center_x': 0.5, 'y': 0.1},
            # on_press=self.on_test_button_click
            on_press=lambda func: slide_transition_to_screen(self, "home", "right")
        )

        self.add_widget(test_label)
        self.add_widget(test_button)