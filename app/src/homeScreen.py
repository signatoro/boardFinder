from kivy.uix.screenmanager import Screen

from kivymd.uix.tab import MDTabsBase
from kivymd.uix.floatlayout import MDFloatLayout


class Tab(MDFloatLayout, MDTabsBase):
    '''Class implementing content for a tab.'''


class HomeScreen(Screen):
    def __init__(self, **kwargs):
        super(HomeScreen, self).__init__(**kwargs)

    def load_depends(self, load_deps=None):
        #TODO: Call endpoint get list of Local events
        local_event_l: list = {}
        pass


    def refresh_local_events(self):
        print("Refreshing local Events")
        pass

    def refresh_groups(self):
        print("Refreshing Groups")
        pass


