from enum import Enum, auto


from kivy.app import App
from kivy.uix.popup import Popup
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.screenmanager import Screen


# from helpers import slide_transition_to_screen


# Enum that represents the state of an input
class InputState(Enum):
    empty: int = 0
    valid: int = 1
    invalid: int = 2


class CreateAccountScreen(Screen):
    def __init__(self, **kwargs):
        super(CreateAccountScreen, self).__init__(**kwargs)
        self.username_input_state = InputState.empty
        self.email_input_state = InputState.empty
        self.password_input_state = InputState.empty
        self.password_confirm_input_state = InputState.empty

    def go_to_sign_in_page(self):
        App.get_running_app().change_screen("sign_in_screen", direction="right")

    def submit_username(self):
        accounts = App.get_running_app().get_accounts()
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
        elif self.ids.username_text_field.text in accounts:
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
        # # Email is taken
        # elif self.ids.email_text_field.text in self.emails:
        #     new_email_input_state = InputState.invalid
        #     self.ids.email_message_label.text = "Email in use!"
        #     self.ids.email_message_label.color = [0.7, 0.3, 0.3, 1]
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

    def screen_entered(self):
        self.ids.username_text_field.text = ""
        self.ids.email_text_field.text = ""
        self.ids.password_text_field.text = ""
        self.ids.password_confirm_text_field.text = ""
        self.ids.username_message_label.text = "Please enter a username."
        self.ids.username_message_label.color = [.5, .5, .5, 1]
        self.ids.email_message_label.text = "Please enter your email."
        self.ids.email_message_label.color = [.5, .5, .5, 1]
        self.ids.password_message_label.text = "Please create a unique password."
        self.ids.password_message_label.color = [.5, .5, .5, 1]
        self.ids.password_confirm_message_label.text = "Please re-type your password."
        self.ids.password_confirm_message_label.color = [.5, .5, .5, 1]
        self.ids.email_prompt_label.opacity = 0
        self.ids.email_text_field.disabled = True
        self.ids.email_text_field.opacity = 0
        self.ids.email_message_label.opacity = 0
        self.ids.password_prompt_label.opacity = 0
        self.ids.password_text_field.disabled = True
        self.ids.password_text_field.opacity = 0
        self.ids.password_message_label.opacity = 0
        self.ids.password_confirm_prompt_label.opacity = 0
        self.ids.password_confirm_text_field.disabled = True
        self.ids.password_confirm_text_field.opacity = 0
        self.ids.password_confirm_message_label.opacity = 0
        self.ids.create_account_button.disabled = True
        self.ids.create_account_button.opacity = 0

    def create_account_attempt(self):
        App.get_running_app().create_account(self.ids.username_text_field.text, self.ids.password_text_field.text)
        App.get_running_app().set_signed_in(True)
        App.get_running_app().change_screen("home_screen", direction="left")
