from kivy.metrics import dp
from kivy.properties import StringProperty
from kivy.uix.popup import Popup
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.button import MDRaisedButton
from kivymd.uix.label import MDLabel
from kivymd.uix.toolbar import MDTopAppBar
from kivy.app import App
from kivy.uix.screenmanager import Screen
from kivy.clock import Clock


class TopBar(MDTopAppBar):
    topBarInstance = None

    def __init__(self, **kwargs):
        super(TopBar, self).__init__(**kwargs)
        self.title = "BoardFinder"

        self.pos_hint_y = None
        self.left_action_items = [["home",
                                   lambda x: App.get_running_app().change_screen("home_screen",
                                                                                 direction='right'),
                                   "Home"]]
        self.right_action_items = [["account",
                                    lambda x: App.get_running_app().change_screen("sign_in_screen",
                                                                                  direction='left'),
                                    "Sign In"]]
        Clock.schedule_once(self.delay_init, 1 / 3)

    def delay_init(self, *args):
        if App.get_running_app() is None:
            Clock.schedule_once(self.delay_init(), 1 / 3)
            return
        App.get_running_app().add_top_bar(self)

    def update_actions(self, *args):
        # Left action items, default to the home screen button
        self.left_action_items = [["home",
                                   lambda x: App.get_running_app().change_screen("home_screen",
                                                                                 direction='right'),
                                   "Home"]]
        # If we are at the home screen, no home button
        if App.get_running_app().get_screen_name() == "home_screen":
            self.left_action_items = []
        # If we are creating a group, give a warning popup first
        if App.get_running_app().get_screen_name() == "create_group_screen":
            self.left_action_items = [["home",
                                       lambda x: self.home_warning(),
                                       "Home"]]

        # Right action items
        profile_screens = ["create_account_screen", "sign_in_screen", "profile_screen"]
        if profile_screens.__contains__(App.get_running_app().get_screen_name()):
            # Empty if at a profile related screen
            self.right_action_items = []
        else:
            # If we are signed in, profile button
            if App.get_running_app().get_signed_in():
                self.right_action_items = [["account-check",
                                            lambda x: App.get_running_app().change_screen("profile_screen",
                                                                                          direction='left'),
                                            "My Profile"]]
            else:
                # If we are not signed in, sign in button
                self.right_action_items = [["account",
                                            lambda x: App.get_running_app().change_screen("sign_in_screen",
                                                                                          direction='left'),
                                            "Sign In"]]

    def home_warning(self):
        home_popup = HomePopup()
        home_popup.open()


class HomePopup(Popup):
    def __init__(self, **kwargs):
        super(HomePopup, self).__init__(**kwargs)
        self.title = f"Warning!"
        self.title_size = 36
        self.title_color = (1, 1, 1, 1)
        self.title_align = 'center'
        self.size_hint_y = 0.75
        self.size_hint_x = 0.75
        self.content = MDBoxLayout(orientation="vertical", spacing=dp(10), padding=dp(10))
        popup_label = MDLabel(
            text=f"Returning to home will reset all group creation info.",
            text_size="root.size",
            valign="center", halign="center",
            font_style="H5",
            theme_text_color="Custom", text_color=(1, 1, 1, 1)
        )
        self.content.add_widget(popup_label)
        self.buttons_layout = MDBoxLayout(orientation="horizontal", spacing=dp(10))
        self.buttons_layout.add_widget(MDRaisedButton(text="Go Home Anyways", on_release=self.go_home, size_hint_x=.5))
        self.buttons_layout.add_widget(MDRaisedButton(text="Go Back", on_release=self.stay_here, size_hint_x=.5))
        self.content.add_widget(self.buttons_layout)

    def go_home(self, instance):
        App.get_running_app().change_screen("home_screen")
        App.get_running_app().reset_create_group()
        self.dismiss()

    def stay_here(self, instance):
        self.dismiss()