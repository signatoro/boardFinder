from kivy.properties import StringProperty
from kivymd.uix.toolbar import MDTopAppBar


class TopBar(MDTopAppBar):
    title = StringProperty()
    homeButtonIcon = StringProperty()
    profileButtonIcon = StringProperty()
    homeButtonDesc = StringProperty()
    profileButtonDesc = StringProperty()
    questionMark = StringProperty()

    def __init__(self, **kwargs):
        super(TopBar, self).__init__(**kwargs)
        self.title = "BoardGameTopBar"
        self.homeButtonIcon = "home"
        self.profileButtonIcon = "account"
        self.homeButtonDesc = "Home"
        self.profileButtonDesc = "Sign In"
        self.questionMark = "???"
