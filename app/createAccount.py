from kivy.uix.screenmanager import Screen
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.popup import Popup
from kivy.uix.textinput import TextInput

from helpers import slide_transition_to_screen
from enum import Enum, auto


# Enum that represents the state of an input
class InputState(Enum):
    empty: int = 0
    valid: int = 1
    invalid: int = 2


# The profile "create an account" screen
class CreateAccountScreen(Screen):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        # Main Widgets
        self.create_account_label = Label(
            text="Create an Account",
            font_size=26,
            pos_hint={'center_x': 0.5, 'center_y': 0.85}
        )
        # self.cool_button = Button(
        #     text="Cool",
        #     size_hint=(None, None),
        #     size=(100, 50),
        #     pos_hint={'center_x': 0.5, 'y': 0.2},
        #     on_press=self.cool_function
        # )
        self.home_button = Button(
            text="Return Home",
            size_hint=(None, None),
            size=(100, 50),
            pos_hint={'center_x': 0.15, 'y': 0.9},
            on_press=lambda func: slide_transition_to_screen(self, "home", "right")
        )

        # Username Fields
        self.username_input_state = InputState.empty
        self.usernames = ["Rishav", "Johnny", "CleoT"]

        # Username Widgets
        self.username_label = Label(
            text="Username: ",
            font_size=24,
            pos_hint={'center_x': 0.25, 'center_y': 0.7}
        )
        self.username_textbox = TextInput(
            text="",
            font_size=24,
            size_hint=(None, None),
            size=(200, 60),
            pos_hint={'center_x': 0.66, 'y': 0.65},
            multiline=False
        )
        self.username_textbox.bind(text=self.on_username_input)
        self.username_message = Label(
            text="Please create a username with\nat least five characters.",
            font_size=18,
            color=[1, 1, 0, 1],
            pos_hint={'center_x': 0.5, 'center_y': 0.61}
        )

        # Email Widgets
        self.email_label = Label(
            text="Email: ",
            font_size=24,
            pos_hint={'center_x': 0.25, 'center_y': 0.53}
        )
        self.email_textbox = TextInput(
            text="",
            font_size=24,
            size_hint=(None, None),
            size=(200, 60),
            pos_hint={'center_x': 0.66, 'y': 0.48},
            multiline=False
        )

        # Email Fields
        self.email_revealed = False

        # Password Widgets

        # Password Fields
        self.password_revealed = False

        # Confirm Password Widgets

        # Confirm Password Fields
        self.confirm_password_revealed = False

        # Add Widgets
        self.add_widget(self.create_account_label)
        self.add_widget(self.home_button)
        self.add_widget(self.username_label)
        self.add_widget(self.username_textbox)
        self.add_widget(self.username_message)

        self.content = Button(text='Close me!', size_hint=(None, None), size=(150, 100))
        self.popup = Popup(content=self.content, size_hint=(None, None), auto_dismiss=False, size=(200, 500))
        self.content.bind(on_press=self.popup.dismiss)

    # Called when the Username TextInput input changes
    def on_username_input(self, instance, value):
        new_username_input_state = None
        if self.username_textbox.text == "":
            new_username_input_state = InputState.empty
            self.username_message.text = "Please create a username with\nat least five characters."
            self.username_message.color = [1, 1, 0, 1]
        elif len(self.username_textbox.text) < 5:
            new_username_input_state = InputState.invalid
            self.username_message.text = "Please create a username with\nat least five characters."
            self.username_message.color = [1, 1, 0, 1]
        elif self.username_textbox.text in self.usernames:
            new_username_input_state = InputState.invalid
            self.username_message.text = "Username taken!"
            self.username_message.color = [1, 0.3, 0.3, 1]
        elif " " in self.username_textbox.text:
            new_username_input_state = InputState.invalid
            self.username_message.text = "Please do not include spaces!"
            self.username_message.color = [1, 0.3, 0.3, 1]
        else:
            new_username_input_state = InputState.valid
            self.username_message.text = "Valid username!"
            self.username_message.color = [0.3, 1, 0.3, 1]

        self.username_input_state = new_username_input_state

        if not self.email_revealed and self.username_input_state == InputState.valid:
            self.add_widget(self.email_label)
            self.add_widget(self.email_textbox)
            self.popup.open()
            self.email_revealed = True
        elif self.email_revealed and not self.password_revealed and self.email_textbox.text == "" and new_username_input_state == InputState.invalid:
            self.remove_widget(self.email_label)
            self.remove_widget(self.email_textbox)
            self.email_revealed = False


    # def cool_function(self, instance):
    #     if self.cool:
    #         self.add_widget(self.create_account_label)
    #     else:
    #         self.remove_widget(self.create_account_label)
    #     self.cool = not self.cool
