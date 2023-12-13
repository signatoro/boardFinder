from enum import Enum, auto


from kivy.app import App
from kivy.uix.popup import Popup
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.screenmanager import Screen


# Enum that represents the state of an input
class InputState(Enum):
    empty: int = 0
    valid: int = 1
    invalid: int = 2


class SignInScreen(Screen):
    def __init__(self, **kwargs):
        super(SignInScreen, self).__init__(**kwargs)
        self.username_input_state = InputState.empty
        self.password_input_state = InputState.empty

    def screen_entered(self):
        self.ids.username_text_field.text = ""
        self.ids.password_text_field.text = ""
        self.ids.username_message_label.text = "Please enter your username."
        self.ids.username_message_label.color = [.5, .5, .5, 1]
        self.ids.password_message_label.text = "Please enter your password."
        self.ids.password_message_label.color = [.5, .5, .5, 1]
        self.ids.password_message_label.opacity = 0
        self.ids.password_message_label.disabled = True
        self.ids.password_prompt_label.opacity = 0
        self.ids.password_text_field.disabled = True
        self.ids.password_text_field.opacity = 0
        self.ids.create_account_button.disabled = False
        self.ids.create_account_button.opacity = 1
        self.ids.sign_in_button.disabled = True
        self.ids.sign_in_button.opacity = 0

    def submit_username(self):
        accounts = App.get_running_app().get_accounts()
        new_username_input_state = None
        # Empty username was input
        if self.ids.username_text_field.text == "":
            new_username_input_state = InputState.empty
            self.ids.username_message_label.text = "Please enter your username."
            self.ids.username_message_label.color = [0.7, 0.5, 0.5, 1]
        # Username exists
        elif self.ids.username_text_field.text in accounts:
            new_username_input_state = InputState.valid
            self.ids.username_message_label.text = "Valid Username!"
            self.ids.username_message_label.color = [0.15, 0.8, 0.15, 1]
        # Username is invalid
        else:
            new_username_input_state = InputState.invalid
            self.ids.username_message_label.text = "User not found!"
            self.ids.username_message_label.color = [0.7, 0.3, 0.3, 1]

        self.username_input_state = new_username_input_state

        # Sign In and Create Account buttons
        if new_username_input_state != InputState.valid:
            self.ids.create_account_button.disabled = False
            self.ids.create_account_button.opacity = 1
            self.ids.sign_in_button.disabled = True
            self.ids.sign_in_button.opacity = 0
        else:
            self.ids.create_account_button.disabled = True
            self.ids.create_account_button.opacity = 0
            self.ids.sign_in_button.disabled = True
            self.ids.sign_in_button.opacity = 0

        # Do not hide password if it contains input
        if self.ids.password_text_field.text != "":
            self.submit_password()
            return
        # Reveal password if it is disabled and username given is valid
        if self.ids.password_text_field.disabled and self.username_input_state == InputState.valid:
            self.ids.password_prompt_label.opacity = 1
            self.ids.password_text_field.disabled = False
            self.ids.password_text_field.opacity = 1
            self.ids.password_message_label.opacity = 1
        # Hide password if it is enabled and the username given is invalid
        elif not self.ids.password_text_field.disabled and new_username_input_state != InputState.valid:
            self.ids.password_prompt_label.opacity = 0
            self.ids.password_text_field.disabled = True
            self.ids.password_text_field.opacity = 0
            self.ids.password_message_label.opacity = 0

    def submit_password(self):
        new_password_confirm_input_state = None
        # Given empty password
        if self.ids.password_text_field.text == "":
            new_password_input_state = InputState.empty
            self.ids.password_message_label.text = "Please enter your Password!"
            self.ids.password_message_label.color = [0.8, 0.4, 0.4, 1]
        else:
            accounts = App.get_running_app().get_accounts()
            password = ""
            if self.ids.username_text_field.text in accounts:
                password = accounts[self.ids.username_text_field.text]
            # Password does not match
            if self.ids.password_text_field.text != password:
                new_password_input_state = InputState.invalid
                self.ids.password_message_label.text = "Incorrect Password!"
                self.ids.password_message_label.color = [0.8, 0.4, 0.4, 1]
            # Password is valid
            else:
                new_password_input_state = InputState.valid
                self.ids.password_message_label.text = "Correct Password!"
                self.ids.password_message_label.color = [0.15, 0.8, 0.15, 1]

        self.password_input_state = new_password_input_state

        # Reveal sign in button if it is disabled and passwords match
        if self.ids.sign_in_button.disabled and self.password_input_state == InputState.valid and self.username_input_state == InputState.valid:
            self.ids.sign_in_button.disabled = False
            self.ids.sign_in_button.opacity = 1
        # Hide sign in button if it is enabled and the passwords do not match
        elif not self.ids.sign_in_button.disabled and new_password_input_state != InputState.valid:
            self.ids.sign_in_button.disabled = True
            self.ids.sign_in_button.opacity = 0

    def sign_in_attempt(self):
        accounts = App.get_running_app().get_accounts()
        password = ""
        if self.ids.username_text_field.text in accounts:
            password = accounts[self.ids.username_text_field.text]
        if password == "" or self.ids.password_text_field.text != password:
            self.ids.username_text_field.text = ""
            self.ids.username_message_label.text = "Incorrect Username!"
            self.ids.username_message_label.color = [0.8, 0.4, 0.4, 1]
            self.username_input_state = InputState.invalid
            self.ids.password_text_field.text = ""
            self.ids.password_message_label.text = "Incorrect Password!"
            self.ids.password_message_label.color = [0.8, 0.4, 0.4, 1]
            self.password_input_state = InputState.invalid
        else:
            App.get_running_app().set_signed_in(True)
            App.get_running_app().change_screen("home_screen", direction="left")

    def create_account_button_pressed(self):
        App.get_running_app().change_screen("create_account_screen", direction="left")
