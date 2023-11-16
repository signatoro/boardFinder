from kivy.uix.screenmanager import Screen
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.carousel import Carousel
from kivy.uix.tabbedpanel import TabbedPanel
from kivy.uix.tabbedpanel import TabbedPanelHeader

from helpers import slide_transition_to_screen

# The home screen
class HomeScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.window = BoxLayout(orientation='vertical')
        self.window.cols = 1
        # self.window.size_hint = (None, None)
        self.add_widget(self.window)

        # Anchor Layout widget at top of window
        self.anchorLayout = AnchorLayout(
            anchor_x='center', anchor_y='top', size_hint=(1, .2))
        self.profile_button = Button(text='Profile',
                                     on_press=lambda func: slide_transition_to_screen(self, "create_account", "left"))
        self.anchorLayout.add_widget(self.profile_button)
        self.window.add_widget(self.anchorLayout)

        # BoxLayout widget for central buttons
        self.layout = BoxLayout(orientation='horizontal', size_hint=(1, 0.6))
        self.btn1 = Button(text='Find a Group', on_press=self.find_a_group)
        self.btn2 = Button(text='Learn a Game')
        self.btn3 = Button(text='Create a Group')
        self.layout.add_widget(self.btn1)
        self.layout.add_widget(self.btn2)
        self.layout.add_widget(self.btn3)
        self.window.add_widget(self.layout)

        # TabbedPanel widget for local events and my groups
        self.tabbed = TabbedPanel(size_hint=(1, 0.8))
        self.window.add_widget(self.tabbed)
        # Carousel local events
        self.local_events = Carousel()
        self.event1 = Button(text='Local Event 1')
        self.event2 = Button(text='Local Event 2')
        self.event3 = Button(text='Local Event 3')
        self.event4 = Button(text='Local Event 4')
        self.local_events.add_widget(self.event1)
        self.local_events.add_widget(self.event2)
        self.local_events.add_widget(self.event3)
        self.local_events.add_widget(self.event4)
        self.tab1 = TabbedPanelHeader(text='Local Events')
        self.tab1.content = self.local_events
        self.tabbed.add_widget(self.tab1)
        self.tabbed.default_tab = self.tab1
        # Carousel my groups
        self.my_groups = Carousel()
        self.group1 = Button(text='Group 1')
        self.group2 = Button(text='Group 2')
        self.group3 = Button(text='Group 3')
        self.group4 = Button(text='Group 4')
        self.my_groups.add_widget(self.group1)
        self.my_groups.add_widget(self.group2)
        self.my_groups.add_widget(self.group3)
        self.my_groups.add_widget(self.group4)
        self.tab2 = TabbedPanelHeader(text='My Groups')
        self.tab2.content = self.my_groups
        self.tabbed.add_widget(self.tab2)

    def find_a_group(self, instance):
        slide_transition_to_screen(self, "profile", "left")
