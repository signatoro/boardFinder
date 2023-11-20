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


class CreateAccountScreen(Screen):
    def __init__(self, **kwargs):
        super(CreateAccountScreen, self).__init__(**kwargs)
        self.username_input_state = InputState.empty
        self.usernames = ["Rishav", "Johnny", "CleoT"]
        self.email_input_state = InputState.empty
        self.emails = ["Rishav", "Johnny", "CleoT"]
        self.password_input_state = InputState.empty
        self.password_confirm_input_state = InputState.empty

    def submit_username(self):
        new_username_input_state = None
        # Empty username was input
        if self.ids.username_text_field.text == "":
            new_username_input_state = InputState.empty
            self.ids.username_message_label.text = "Please create a username with\nat least five characters."
            self.ids.username_message_label.color = [0.7, 0.5, 0.5, 1]
        # Username is too short
        elif len(self.ids.username_text_field.text) < 5:
            new_username_input_state = InputState.invalid
            self.ids.username_message_label.text = "Please create a username with\nat least five characters."
            self.ids.username_message_label.color = [0.7, 0.5, 0.5, 1]
        # Username is taken
        elif self.ids.username_text_field.text in self.usernames:
            new_username_input_state = InputState.invalid
            self.ids.username_message_label.text = "Username taken!"
            self.ids.username_message_label.color = [0.7, 0.3, 0.3, 1]
        # Username contains space
        elif " " in self.ids.username_text_field.text:
            new_username_input_state = InputState.invalid
            self.ids.username_message_label.text = "Please do not include spaces."
            self.ids.username_message_label.color = [0.7, 0.5, 0.5, 1]
        # Username is valid
        else:
            new_username_input_state = InputState.valid
            self.ids.username_message_label.text = "Valid username!"
            self.ids.username_message_label.color = [0.15, 0.8, 0.15, 1]

        self.username_input_state = new_username_input_state

        # Do not hide email if it contains input, nor if the password has been revealed
        if not self.ids.password_text_field.disabled or self.ids.email_text_field.text != "":
            return
        # Reveal email if it is disabled and username given is valid
        if self.ids.email_text_field.disabled and self.username_input_state == InputState.valid:
            self.ids.email_prompt_label.opacity = 1
            self.ids.email_text_field.disabled = False
            self.ids.email_text_field.opacity = 1
            self.ids.email_message_label.opacity = 1
        # Hide email if it is enabled and the username given is invalid
        elif not self.ids.email_text_field.disabled and new_username_input_state != InputState.valid:
            self.ids.email_prompt_label.opacity = 0
            self.ids.email_text_field.disabled = True
            self.ids.email_text_field.opacity = 0
            self.ids.email_message_label.opacity = 0

    def submit_email(self):
        new_email_input_state = None
        # Empty email was input
        if self.ids.email_text_field.text == "":
            new_email_input_state = InputState.empty
            self.ids.email_message_label.text = "Please enter your email."
            self.ids.email_message_label.color = [0.7, 0.5, 0.5, 1]
        # Email is taken
        elif self.ids.email_text_field.text in self.emails:
            new_email_input_state = InputState.invalid
            self.ids.email_message_label.text = "Email in use!"
            self.ids.email_message_label.color = [0.7, 0.3, 0.3, 1]
        # Email does not contain '@' and '.' characters
        elif "@" not in self.ids.email_text_field.text or "." not in self.ids.email_text_field.text:
            new_email_input_state = InputState.invalid
            self.ids.email_message_label.text = "Invalid email."
            self.ids.email_message_label.color = [0.7, 0.3, 0.3, 1]
        # Email is valid
        else:
            new_email_input_state = InputState.valid
            self.ids.email_message_label.text = "Valid email!"
            self.ids.email_message_label.color = [0.15, 0.8, 0.15, 1]

        self.email_input_state = new_email_input_state

        # Do not hide password if it contains input, nor if the confirm-password has been revealed
        if not self.ids.password_confirm_text_field.disabled or self.ids.password_text_field.text != "":
            return
        # Reveal password if it is disabled and email given is valid
        if self.ids.password_text_field.disabled and self.email_input_state == InputState.valid:
            self.ids.password_prompt_label.opacity = 1
            self.ids.password_text_field.disabled = False
            self.ids.password_text_field.opacity = 1
            self.ids.password_message_label.opacity = 1
        # Hide password if it is enabled and the email given is invalid
        elif not self.ids.password_text_field.disabled and new_email_input_state != InputState.valid:
            self.ids.password_prompt_label.opacity = 0
            self.ids.password_text_field.disabled = True
            self.ids.password_text_field.opacity = 0
            self.ids.password_message_label.opacity = 0

    def submit_password(self):
        new_password_input_state = None
        # Empty password was input
        if self.ids.password_text_field.text == "":
            new_password_input_state = InputState.empty
            self.ids.password_message_label.text = "Please create a password with\nat least five characters."
            self.ids.password_message_label.color = [0.7, 0.5, 0.5, 1]
        # Password is too short
        elif len(self.ids.password_text_field.text) < 5:
            new_password_input_state = InputState.invalid
            self.ids.password_message_label.text = "Please create a password with\nat least five characters."
            self.ids.password_message_label.color = [0.7, 0.5, 0.5, 1]
        # Password is valid
        else:
            new_password_input_state = InputState.valid
            self.ids.password_message_label.text = "Valid password!"
            self.ids.password_message_label.color = [0.15, 0.8, 0.15, 1]

        self.password_input_state = new_password_input_state

        # Do not hide confirm-password if it contains input
        if self.ids.password_confirm_text_field.text != "":
            return
        # Reveal confirm-password if it is disabled and password given is valid
        if self.ids.password_confirm_text_field.disabled and self.password_input_state == InputState.valid:
            self.ids.password_confirm_prompt_label.opacity = 1
            self.ids.password_confirm_text_field.disabled = False
            self.ids.password_confirm_text_field.opacity = 1
            self.ids.password_confirm_message_label.opacity = 1
        # Hide confirm-password if it is enabled and the password given is invalid
        elif not self.ids.password_text_field.disabled and new_password_input_state != InputState.valid:
            self.ids.password_confirm_prompt_label.opacity = 0
            self.ids.password_confirm_text_field.disabled = True
            self.ids.password_confirm_text_field.opacity = 0
            self.ids.password_confirm_message_label.opacity = 0

    def submit_password_confirm(self):
        new_password_confirm_input_state = None
        # Passwords do not match
        if self.ids.password_text_field.text != self.ids.password_confirm_text_field.text:
            new_password_confirm_input_state = InputState.empty
            self.ids.password_confirm_message_label.text = "Passwords do not match!"
            self.ids.password_confirm_message_label.color = [0.8, 0.4, 0.4, 1]
        # Password is valid
        else:
            new_password_confirm_input_state = InputState.valid
            self.ids.password_confirm_message_label.text = "Passwords match!"
            self.ids.password_confirm_message_label.color = [0.15, 0.8, 0.15, 1]

        self.password_confirm_input_state = new_password_confirm_input_state

        # Reveal create account button if it is disabled and passwords match
        if self.ids.create_account_button.disabled and self.password_confirm_input_state == InputState.valid:
            self.ids.create_account_button.disabled = False
            self.ids.create_account_button.opacity = 1
        # Hide create account button if it is enabled and the passwords do not match
        elif not self.ids.create_account_button.disabled and new_password_confirm_input_state != InputState.valid:
            self.ids.create_account_button.disabled = True
            self.ids.create_account_button.opacity = 0


# The profile "create an account" screen
# class CreateAccountScreen(Screen):
#
#     def __init__(self, **kwargs):
#         super().__init__(**kwargs)

    #     # Main Widgets
    #     self.create_account_label = Label(
    #         text="Create an Account",
    #         font_size=26,
    #         pos_hint={'center_x': 0.5, 'center_y': 0.85}
    #     )
    #     # self.cool_button = Button(
    #     #     text="Cool",
    #     #     size_hint=(None, None),
    #     #     size=(100, 50),
    #     #     pos_hint={'center_x': 0.5, 'y': 0.2},
    #     #     on_press=self.cool_function
    #     # )
    #     self.home_button = Button(
    #         text="Return Home",
    #         size_hint=(None, None),
    #         size=(100, 50),
    #         pos_hint={'center_x': 0.15, 'y': 0.9},
    #         on_press=lambda func: slide_transition_to_screen(self, "home_screen", "right")
    #     )
    #
    #     # Username Fields
    #     self.username_input_state = InputState.empty
    #     self.usernames = ["Rishav", "Johnny", "CleoT"]
    #
    #     # Username Widgets
    #     self.username_label = Label(
    #         text="Username: ",
    #         font_size=24,
    #         pos_hint={'center_x': 0.25, 'center_y': 0.7}
    #     )
    #     self.username_textbox = TextInput(
    #         text="",
    #         font_size=24,
    #         size_hint=(None, None),
    #         size=(200, 60),
    #         pos_hint={'center_x': 0.66, 'y': 0.65},
    #         multiline=False
    #     )
    #     self.username_textbox.bind(text=self.on_username_input)
    #     self.username_message = Label(
    #         text="Please create a username with\nat least five characters.",
    #         font_size=18,
    #         color=[1, 1, 0, 1],
    #         pos_hint={'center_x': 0.5, 'center_y': 0.61}
    #     )
    #
    #     # Email Widgets
    #     self.email_label = Label(
    #         text="Email: ",
    #         font_size=24,
    #         pos_hint={'center_x': 0.25, 'center_y': 0.53}
    #     )
    #     self.email_textbox = TextInput(
    #         text="",
    #         font_size=24,
    #         size_hint=(None, None),
    #         size=(200, 60),
    #         pos_hint={'center_x': 0.66, 'y': 0.48},
    #         multiline=False
    #     )
    #
    #     # Email Fields
    #     self.email_revealed = False
    #
    #     # Password Widgets
    #
    #     # Password Fields
    #     self.password_revealed = False
    #
    #     # Confirm Password Widgets
    #
    #     # Confirm Password Fields
    #     self.confirm_password_revealed = False
    #
    #     # Add Widgets
    #     self.add_widget(self.create_account_label)
    #     self.add_widget(self.home_button)
    #     self.add_widget(self.username_label)
    #     self.add_widget(self.username_textbox)
    #     self.add_widget(self.username_message)
    #
    #     self.content = Button(text='Close me!', size_hint=(None, None), size=(150, 100))
    #     self.popup = Popup(content=self.content, size_hint=(None, None), auto_dismiss=False, size=(200, 500))
    #     self.content.bind(on_press=self.popup.dismiss)
    #
    # # Called when the Username TextInput input changes
    # def on_username_input(self, instance, value):
    #     new_username_input_state = None
    #     if self.username_textbox.text == "":
    #         new_username_input_state = InputState.empty
    #         self.username_message.text = "Please create a username with\nat least five characters."
    #         self.username_message.color = [1, 1, 0, 1]
    #     elif len(self.username_textbox.text) < 5:
    #         new_username_input_state = InputState.invalid
    #         self.username_message.text = "Please create a username with\nat least five characters."
    #         self.username_message.color = [1, 1, 0, 1]
    #     elif self.username_textbox.text in self.usernames:
    #         new_username_input_state = InputState.invalid
    #         self.username_message.text = "Username taken!"
    #         self.username_message.color = [1, 0.3, 0.3, 1]
    #     elif " " in self.username_textbox.text:
    #         new_username_input_state = InputState.invalid
    #         self.username_message.text = "Please do not include spaces!"
    #         self.username_message.color = [1, 0.3, 0.3, 1]
    #     else:
    #         new_username_input_state = InputState.valid
    #         self.username_message.text = "Valid username!"
    #         self.username_message.color = [0.3, 1, 0.3, 1]
    #
    #     self.username_input_state = new_username_input_state
    #
    #     if not self.email_revealed and self.username_input_state == InputState.valid:
    #         self.add_widget(self.email_label)
    #         self.add_widget(self.email_textbox)
    #         self.popup.open()
    #         self.email_revealed = True
    #     elif self.email_revealed and not self.password_revealed and self.email_textbox.text == "" and new_username_input_state == InputState.invalid:
    #         self.remove_widget(self.email_label)
    #         self.remove_widget(self.email_textbox)
    #         self.email_revealed = False


    # def cool_function(self, instance):
    #     if self.cool:
    #         self.add_widget(self.create_account_label)
    #     else:
    #         self.remove_widget(self.create_account_label)
    #     self.cool = not self.cool
