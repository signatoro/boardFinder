from kivy.app import App
from kivy.uix.screenmanager import Screen

class ProfileScreen(Screen):

    def __init__(self, **kwargs):
        super(ProfileScreen, self).__init__(**kwargs)

    def sign_out(self):
        App.get_running_app().set_signed_in(False)
        App.get_running_app().change_screen("home_screen")
