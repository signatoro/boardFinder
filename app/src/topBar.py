from kivy.properties import StringProperty
from kivymd.uix.toolbar import MDTopAppBar
from kivy.app import App
from kivy.uix.screenmanager import Screen
from kivy.clock import Clock

class TopBar(MDTopAppBar):
    topBarInstance = None
    # title = StringProperty()
    # homeButtonIcon = StringProperty()
    # profileButtonIcon = StringProperty()
    # homeButtonDesc = StringProperty()
    # profileButtonDesc = StringProperty()
    # questionMark = StringProperty()
    # left_action_item = [["home",
    #              lambda x: App.get_running_app().change_screen("home_screen", direction='right'),
    #              "homes",
    #              "?"]]

    def __init__(self, **kwargs):
        super(TopBar, self).__init__(**kwargs)
        self.title = "BoardFinder"
        # self.homeButtonIcon = "home"
        # self.profileButtonIcon = "account"
        # self.homeButtonDesc = "Home"
        # self.profileButtonDesc = "Sign In"
        # # self.questionMark = "???"
        # self.left_action_items = [["home",
        #                      lambda x: App.get_running_app().change_screen("home_screen", direction='right'),
        #                      "homes",
        #                      "?"]]

        self.pos_hint_y = None
        self.left_action_items = \
            [["home", lambda x: App.get_running_app().change_screen("home_screen", direction='right'), "Home"]]
        # self.right_action_items = \
        #     [["account", lambda x: App.get_running_app().change_screen("create_account_screen", direction='left'), "Create Account"],
        #      ["account", lambda x: App.get_running_app().change_screen("sign_in_screen", direction='left'), "Sign In"]]
        self.right_action_items = \
            [["account", lambda x: App.get_running_app().change_screen("sign_in_screen", direction='left'),
              "Sign In"]]
        Clock.schedule_once(self.delay_init, 1 / 3)
        # self.bind(on_pre_enter=self.update_actions)

    def delay_init(self, *args):
        if App.get_running_app() is None:
            Clock.schedule_once(self.delay_init(), 1 / 3)
            return
        App.get_running_app().add_top_bar(self)

    def update_actions(self, *args):
        if App.get_running_app().get_screen_name() != "home_screen":
            self.left_action_items = \
                [["home", lambda x: App.get_running_app().change_screen("home_screen", direction='right'), "Home"]]
        else:
            self.left_action_items = \
                []

        if App.get_running_app().get_screen_name() == "create_account_screen" or App.get_running_app().get_screen_name() == "sign_in_screen":
            self.right_action_items = []
        else:
            if App.get_running_app().get_signed_in():
                self.right_action_items = \
                    [["account", lambda x: App.get_running_app().change_screen("profile_screen", direction='left'),
                      "My Profile"]]
            else:
                self.right_action_items = \
                    self.right_action_items = \
                    [["account", lambda x: App.get_running_app().change_screen("sign_in_screen", direction='left'),
                      "Sign In"]]

    # def get_homeButtonIcon(self):
    #     return self.homeButtonIcon
    # def get_profileButtonIcon(self):
    #     return self.profileButtonIcon
    #
    # def get_homeButtonDesc(self):
    #     return self.homeButtonDesc
    #
    # def get_profileButtonDesc(self):
    #     return self.profileButtonDesc
    #
    # def get_left_action_item(self):
    #     print("hi")
    #     print(self.get_homeButtonIcon())
    #     print(self.get_homeButtonDesc())
    #     print(self.get_profileButtonIcon())
    #     print(self.get_profileButtonDesc())
    #     print("h!@i")
    #     return [[self.get_homeButtonIcon(),
    #              lambda x: App.get_running_app().change_screen("home_screen", direction='right'),
    #              self.get_homeButtonDesc(),
    #              "?"]]

