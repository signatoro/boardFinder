from datetime import time

from kivy.metrics import dp
from kivy.clock import Clock
from kivy.uix.popup import Popup
from kivymd.uix.label import MDLabel
from kivymd.uix.tab import MDTabsBase
from kivy.uix.screenmanager import Screen
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.button import MDRaisedButton
from kivymd.uix.floatlayout import MDFloatLayout
from kivy.properties import StringProperty



from src.localEventCard import LocalEventCard
from src.groupCard import GroupCard
from src.topBar import TopBar


class Tab(MDFloatLayout, MDTabsBase):
    '''Class implementing content for a tab.'''


class HomeScreen(Screen):

    carol_index = StringProperty()

    local_event_l: list = []
    def __init__(self, **kwargs):
        
        # self.local_event_l: list = []
        super(HomeScreen, self).__init__(**kwargs)
        

    def on_enter(self, *args):
        
        Clock.schedule_once(self.load_depends)
        return super().on_enter(*args)
    
    def on_carousel_slide(self, *args):
        current_index = args[0].index + 1
        total_index = len(args)-1
        self.carol_index = f"{current_index}/{total_index}"
        


    def load_depends(self, load_deps=None):
        self.ids.local_event_carou.bind(on_slide_complete=self.on_carousel_slide)
        self.ids.group_card_carou.bind(on_slide_complete=self.on_carousel_slide)
        self.carol_index = "1/3"
        self.load_local_events()
        self.load_group_cards()


    def load_local_events(self):
        self.local_event_l.clear()
        self.ids.local_event_carou.clear_widgets()
        # print("Loading Depends")
        #TODO: Call endpoint get list of Local events
        local_event1 = LocalEventCard(parent=self, title= "Swords and Coffee",
            event_link= "link.url.here",
            description= "The error message ImportError: cannot import name TimeProperty means that Kivycannot find the TimeProperty class in the kivy.properties module. This can happen for a few reasons:",
            location_type= "In Person",
            month= '12',
            day= '4',
            time= "1:30 pm",
            location= "Library, Boston MA"
        )
        local_event2 = LocalEventCard(parent=self, title= "Cards and Coffee",
            event_link= "link.url.here",
            description= "The error message ImportError: cannot import name TimeProperty means that Kivycannot find the TimeProperty class in the kivy.properties module. This can happen for a few reasons:",
            location_type= "In Person",
            month= '12',
            day= '15',
            time= "3:45 pm",
            location= "Library, Boston MA"
        )
        local_event3 = LocalEventCard(parent=self, title= "Magic The Gathering: New Release",
            event_link= "link.url.here",
            description= "The error message ImportError: cannot import name TimeProperty means that Kivycannot find the TimeProperty class in the kivy.properties module. This can happen for a few reasons:",
            location_type= "In Person",
            month= '1',
            day= '31',
            time= "5:00 pm",
            location= "Library, Boston MA"
        )
        local_event_l: list = [local_event1, local_event2, local_event3]


        # adds widgets 
        for event in local_event_l:
            # event.add_parent(self)
            self.ids.local_event_carou.add_widget(event)
    
    def load_group_cards(self):
        '''
        title= StringProperty()
        description= StringProperty()

        month= NumericProperty()
        day= NumericProperty()
        time= StringProperty()
        location= StringProperty()

        session_length= StringProperty()
        participant = StringProperty()

        parent_screen = ObjectProperty() 
        '''

        self.local_event_l.clear()
        self.ids.group_card_carou.clear_widgets()

        
        local_event1 = GroupCard(parent=self, title= "Rishav's Group",
            description= "The error message ImportError: cannot import name TimeProperty means that Kivycannot find the TimeProperty class in the kivy.properties module. This can happen for a few reasons:",
            user_status = "Request Pending",
            month= '12',
            day= '4',
            time= "1:30 pm",
            location= "Library, Boston MA",
            image_path = 'images/celebi.png',
            session_length= "4 - 6 Hrs",
            participant = '1/4 Attending',
        )

        local_event2 = GroupCard(parent=self, title= "Scott's Group",
            description= "The error message ImportError: cannot import name TimeProperty means that Kivycannot find the TimeProperty class in the kivy.properties module. This can happen for a few reasons:",
            user_status = "Request Pending",
            month= '2',
            day= '5',
            time= "5:30 pm",
            location= "Library, Boston MA",
            image_path = 'images/pikachu.jpg',
            session_length= "4 - 6 Hrs",
            participant = '1/4 Attending',
        )

        local_event3 = GroupCard(parent=self, title= "Matty's Group",
            description= "The error message ImportError: cannot import name TimeProperty means that Kivycannot find the TimeProperty class in the kivy.properties module. This can happen for a few reasons:",
            user_status = "Request Pending",
            month= '1',
            day= '0',
            time= "1:30 pm",
            location= "Library, Boston MA",
            image_path = 'images/piplup.jpg',
            session_length= "4 - 6 Hrs",
            participant = '3/6 Attending',
            
        )

        local_event_l: list = [local_event1, local_event2, local_event3]


        # adds widgets 
        for event in local_event_l:
            # event.add_parent(self)
            self.ids.group_card_carou.add_widget(event)

        pass
        
    def create_redirect_popup(self, url: str):
        delete_popup = RedirectSitePopup(url)
        delete_popup.open()
        pass

    def refresh_local_events(self):
        # print("Refreshing local Events")
        pass

    def refresh_groups(self):
        # print("Refreshing Groups")
        pass


class RedirectSitePopup(Popup):
    def __init__(self, item_text, **kwargs):
        super(RedirectSitePopup, self).__init__(**kwargs)
        self.item_text = item_text
        self.title = f"!!  Warning  !! You are being redirected !!  Warning  !!"
        self.title_size = 42
        self.title_color = (1, 0, 0, 1)
        self.title_align = 'center'
        self.size_hint_y = 0.5
        self.size_hint_x = 0.5
        self.content = MDBoxLayout(orientation="vertical", spacing=dp(10), padding=dp(10))
        popup_label = MDLabel(
            text=f"You are going to '{item_text}'. This website is not controlled by us!?",
            text_size= "root.size",
            valign ="center", halign = "center",
            font_style = "H5",
            theme_text_color="Custom", text_color=(1, 1, 1, 1)
        )
        self.content.add_widget(popup_label)
        self.buttons_layout = MDBoxLayout(orientation="horizontal", spacing=dp(10))
        self.buttons_layout.add_widget(MDRaisedButton(text="Stay Here", on_release=self.on_no, size_hint_x=.5))
        self.buttons_layout.add_widget(MDRaisedButton(text="Go To Site", on_release=self.on_yes, size_hint_x=.5))
        self.content.add_widget(self.buttons_layout)

    def on_yes(self, instance):
        print("You are being redirected")
        self.dismiss()
        

    def on_no(self, instance):
        self.dismiss()