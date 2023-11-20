from datetime import time

from kivy.clock import Clock
from kivymd.uix.tab import MDTabsBase
from kivy.uix.screenmanager import Screen
from kivymd.uix.floatlayout import MDFloatLayout

from src.localEventCard import LocalEventCard


class Tab(MDFloatLayout, MDTabsBase):
    '''Class implementing content for a tab.'''


class HomeScreen(Screen):
    def __init__(self, **kwargs):
        super(HomeScreen, self).__init__(**kwargs)

    def on_enter(self, *args):
        Clock.schedule_once(self.load_depends)
        return super().on_enter(*args)

    def load_depends(self, load_deps=None):
        print("Loading Depends")
        #TODO: Call endpoint get list of Local events
        local_event1 = LocalEventCard(title= "Swords and Coffee",
            event_link= "link.url.here",
            description= "The error message ImportError: cannot import name TimeProperty means that Kivycannot find the TimeProperty class in the kivy.properties module. This can happen for a few reasons:",
            location_type= "In Person",
            month= '12',
            day= '4',
            time= "1:30 pm",
            location= "Library, Boston MA"
        )
        local_event_l: list = [local_event1]


        # adds widgets 
        for event in local_event_l:
            self.ids.local_event_carou.add_widget(event)
        


    def refresh_local_events(self):
        print("Refreshing local Events")
        pass

    def refresh_groups(self):
        print("Refreshing Groups")
        pass


