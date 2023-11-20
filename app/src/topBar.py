from kivy.properties import StringProperty
from kivymd.uix.toolbar import MDTopAppBar
from kivy.app import App


class TopBar(MDTopAppBar):
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
        self.title = "BoardGameTopBar"
        # self.homeButtonIcon = "home"
        # self.profileButtonIcon = "account"
        # self.homeButtonDesc = "Home"
        # self.profileButtonDesc = "Sign In"
        # self.questionMark = "???"
        self.left_action_items = [["home",
                             lambda x: App.get_running_app().change_screen("home_screen", direction='right'),
                             "homes",
                             "?"]]

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
