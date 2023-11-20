from kivy.uix.screenmanager import Screen

from kivymd.uix.tab import MDTabsBase
from kivymd.uix.floatlayout import MDFloatLayout


class Tab(MDFloatLayout, MDTabsBase):
    '''Class implementing content for a tab.'''


class HomeScreen(Screen):
    def __init__(self, **kwargs):
        super(HomeScreen, self).__init__(**kwargs)