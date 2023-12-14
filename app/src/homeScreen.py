from datetime import time, datetime, timedelta

from kivy.app import App
from kivy.metrics import dp
from kivy.clock import Clock
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.popup import Popup
from kivymd.uix.chip import MDChip
from kivymd.uix.label import MDLabel
from kivymd.uix.tab import MDTabsBase
from kivy.uix.screenmanager import Screen
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.button import MDRaisedButton
from kivymd.uix.floatlayout import MDFloatLayout
from kivy.properties import StringProperty



from src.localEventCard import LocalEventCard
from src.groupCard import GroupCard

from src import createGroup
from src.gameGroupScreen import GameGroupScreen

from app.src.groupListCard import GroupListCard


class Tab(MDFloatLayout, MDTabsBase):
    '''Class implementing content for a tab.'''


class HomeScreen(Screen):

    carol_index = StringProperty()

    local_event_l: list = []
    group_cards: list = []

    days = []

    successful_card_delete_popup = None

    dummy_group_data_1 = None

    group_list_screen_reference = None

    def __init__(self, **kwargs):
        
        # self.local_event_l: list = []
        super(HomeScreen, self).__init__(**kwargs)
        self.days = [day.lower() for day in createGroup.days]
        self.generate_one_game_group()  # TODO: Delete for testing
        self.add_dummy_cards_to_group_list() # TODO: delete eventually
        self.add_dummy_local_events_to_list() # TODO: delete eventually
        self.successful_card_delete_popup = SuccessPopup(self, "delete card")

    def on_enter(self, *args):
        Clock.schedule_once(self.load_depends)
        return super().on_enter(*args)

    def load_depends(self, load_deps=None):
        self.ids.local_event_carou.bind(on_slide_complete=self.on_carousel_slide)
        self.ids.group_card_carou.bind(on_slide_complete=self.on_carousel_slide)
        self.ids.home_tabs.bind(on_tab_switch=self.on_thing_switch)
        self.ids.tab_local.bind(on_tab_switch=self.on_thing_switch)
        self.ids.tab_group.bind(on_tab_switch=self.on_thing_switch)
        self.group_list_screen_reference = App.get_running_app().main_screen_manager.get_screen("group_list_screen")
        self.carol_index = "1/3"
        self.load_local_events()
        self.load_group_cards()

    def generate_one_game_group(self):
        tags_list = []
        for i in range(3):
            chip = MDChip(
                text=f"tag {i}",
                text_color=(0, 0, 0, 1),
            )
            chip.md_bg_color = "teal"
            tags_list.append(chip)

        game_data = {
            "board_game_list": ["catan", "monopoly"],
            "group_image": "images/piplup.jpg",
            "group_title": "test group",
            "group_general_description": "Come have a grand ol' time with your boi, chef Rish",
            "group_additional_description": "this is addy info",
            "group_mtg_day_and_recurring_info": {"Saturday": True},
            "group_mtg_start_time": "4:00:00 PM",
            "group_mtg_end_time": "8:00:00 PM",
            "group_mtg_location": "BPD",
            "group_max_players": "8",
            "group_host_fname": "alice",
            "group_host_lname": "bobol",
            "group_host_email": "bobol.alice@gmail.com",
            "group_host_phone_num": "911-991-1000",
            "group_tags": tags_list,
            "new_group": False,
            "owner": False,
        }
        game_group_1 = GameGroupScreen()
        game_group_1.load_depends(game_data, 'home_screen')

        dow = ""
        for key in game_group_1.group_mtg_day_and_recurring_info.keys():
            dow = key
        next_date_of_meeting = self.get_updated_date_of_next_meeting(dow)
        session_length = self.get_hours_between_times(game_group_1.group_meeting_start_time,
                                                      game_group_1.group_meeting_end_time)

        created_group_card = GroupCard(
            parent=self,
            game_group=game_group_1,
            title=game_group_1.group_title,
            description=game_group_1.group_general_description,
            user_status="Open To New Members",
            month=str(next_date_of_meeting.month),
            day=str(next_date_of_meeting.day),
            dow=dow,
            time=f"{game_group_1.group_meeting_start_time} - {game_group_1.group_meeting_end_time}",
            location=game_group_1.group_meeting_location,
            image_path=game_group_1.group_image,
            session_length=f"{str(int(session_length))} Hrs",
            participant=f'1/{game_group_1.group_max_players} Attending',
        )

        self.group_cards.insert(0, created_group_card)

    def add_dummy_cards_to_group_list(self):
        group_card_2 = GroupCard(
            parent=self,
            game_group=None,  # Dummy Group Card
            title="Scott's Group",
            description="By the end of it we might hate each other, but boy will we have fun!",
            user_status="Request Pending",
            month='2',
            day='5',
            dow="Friday",
            time="5:30 pm",
            location="Library, Boston MA",
            image_path='images/pikachu.jpg',
            session_length="4 - 6 Hrs",
            participant='1/4 Attending',
        )

        group_card_3 = GroupCard(
            parent=self,
            game_group=None,  # Dummy Group Card
            title="Matty's Group",
            description="We give free stuff!! Please come! Free food, water, new dice set!!! ~Join now~",
            user_status="Request Pending",
            month='1',
            day='0',
            dow="Sunday",
            time="1:30 pm",
            location="Library, Boston MA",
            image_path='images/piplup.jpg',
            session_length="4 - 6 Hrs",
            participant='3/6 Attending',
        )

        self.group_cards.append(group_card_2)
        self.group_cards.append(group_card_3)

    def add_dummy_local_events_to_list(self):
        local_event1 = LocalEventCard(
            parent=self,
            title="Rolling Dice Delight",
            event_link="rolling_dice_delight.eventbrite.com",
            description="Join us for an afternoon of strategic board gaming and fun! Bring your favorite board game or try one of ours. All skill levels welcome!",
            location_type="In Person",
            month='12',
            day='15',
            time="2:00 pm",
            location="Boston Library, Boston, MA"
        )

        local_event2 = LocalEventCard(
            parent=self,
            title="Cards & Conversations",
            event_link="cards_and_conversations.meetup.com",
            description="Unplug and unwind with a night of card games and engaging conversations. Whether you're a seasoned gamer or a newbie, there's a game for everyone!",
            location_type="In Person",
            month='1',
            day='8',
            time="7:00 pm",
            location="Boston Library, Boston, MA"
        )

        local_event3 = LocalEventCard(
            parent=self,
            title="Puzzle Palooza",
            event_link="puzzle_palooza_tickets.io",
            description="Calling all puzzle enthusiasts! Test your puzzle-solving skills and enjoy a friendly competition. Prizes for the fastest solving times!",
            location_type="In Person",
            month='1',
            day='20',
            time="6:30 pm",
            location="Boston Library, Boston, MA"
        )

        self.local_event_l.append(local_event1)
        self.local_event_l.append(local_event2)
        self.local_event_l.append(local_event3)

    def load_local_events(self):
        self.ids.local_event_carou.clear_widgets()
        # print("Loading Depends")
        #TODO: Call endpoint get list of Local events

        # adds widgets 
        for event in self.local_event_l:
            # event.add_parent(self)
            self.ids.local_event_carou.add_widget(event)

    def remove_group_card_and_refresh(self, group):
        self.group_cards.remove(group)
        self.successful_card_delete_popup.open()

    def get_updated_date_of_next_meeting(self, next_dow):
        current_date = datetime.now()

        current_day = current_date.weekday()

        target_day = self.days.index(
            next_dow.lower())

        days_until_next = (target_day - current_day + 7) % 7
        return current_date + timedelta(days=days_until_next)

    def get_hours_between_times(self, start_time, end_time):
        time_format = "%I:%M:%S %p"

        datetime1 = datetime.strptime(start_time, time_format)
        datetime2 = datetime.strptime(end_time, time_format)

        time_difference = datetime2 - datetime1

        total_hours = time_difference.total_seconds() / 3600

        return total_hours

    def add_created_group_card(self, game_group_screen_info):
        dow = ""
        for key in game_group_screen_info.group_mtg_day_and_recurring_info.keys():
            dow = key
        next_date_of_meeting = self.get_updated_date_of_next_meeting(dow)
        session_length = self.get_hours_between_times(game_group_screen_info.group_meeting_start_time,
                                                      game_group_screen_info.group_meeting_end_time)

        created_group_card = GroupCard(
            parent=self,
            game_group=game_group_screen_info,
            title=game_group_screen_info.group_title,
            description=game_group_screen_info.group_general_description,
            user_status="Open To New Members",
            month=str(next_date_of_meeting.month),
            day=str(int(next_date_of_meeting.day)),
            dow=dow,
            time=f"{game_group_screen_info.group_meeting_start_time} - {game_group_screen_info.group_meeting_end_time}",
            location=game_group_screen_info.group_meeting_location,
            image_path=game_group_screen_info.group_image,
            session_length=f"{str(int(session_length))} Hrs",
            participant=f'1/{game_group_screen_info.group_max_players} Attending',
        )

        # adding new group to group list
        created_group_list_card = GroupListCard(
            title=game_group_screen_info.group_title,
            description=game_group_screen_info.group_general_description,
            user_status="Open To New Members",
            month=str(next_date_of_meeting.month),
            day=str(int(next_date_of_meeting.day)),
            dow=dow,
            time=f"{game_group_screen_info.group_meeting_start_time} - {game_group_screen_info.group_meeting_end_time}",
            location=game_group_screen_info.group_meeting_location,
            image_path=game_group_screen_info.group_image,
            session_length=f"{str(int(session_length))} Hrs",
            participant=f'1/{game_group_screen_info.group_max_players} Attending',
        )
        self.group_list_screen_reference.add_new_group(created_group_list_card)

        self.group_cards.insert(0, created_group_card)
        self.load_group_cards()
    
    def load_group_cards(self):
        self.ids.group_card_carou.clear_widgets()

        # adds widgets
        for group in self.group_cards:
            # event.add_parent(self)
            self.ids.group_card_carou.add_widget(group)
        pass

    def delete_group_card(self, game_group_screen_info):
        for group in self.group_cards:
            if group.title == game_group_screen_info.group_title:
                self.group_cards.remove(group)
        print(f"game group not found")
        self.load_group_cards()

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

    def try_find_group(self):
        if App.get_running_app().get_signed_in():
            App.get_running_app().change_screen("find_group_screen")
        else:
            sign_in_popup = SignInPopup()
            sign_in_popup.open()
        pass

    def try_create_group(self):
        if App.get_running_app().get_signed_in():
            App.get_running_app().change_screen("create_group_screen")
        else:
            sign_in_popup = SignInPopup()
            sign_in_popup.open()
        pass

    def on_back_button(self):
        print(self.ids.home_tabs.get_current_tab().tab_label_text)
        tab_id = self.ids.home_tabs.get_current_tab().tab_label_text
        
        if tab_id == "Local Events":
            self.ids.local_event_carou.load_previous()
        elif tab_id == "My Groups":
            self.ids.group_card_carou.load_previous()
    
    def on_forward_button(self):
        tab_id = self.ids.home_tabs.get_current_tab().tab_label_text
        
        if tab_id == "Local Events":
            self.ids.local_event_carou.load_next()
        elif tab_id == "My Groups":
            self.ids.group_card_carou.load_next()

    def on_thing_switch(self, *args):
        tab_id = self.ids.home_tabs.get_current_tab().tab_label_text

        current_car = None
        if tab_id == "Local Events":
            current_car = self.ids.local_event_carou
        elif tab_id == "My Groups":
            current_car = self.ids.group_card_carou

        current_index = current_car.index + 1
        total_index = len(current_car.slides)
        self.carol_index = f"{current_index}/{total_index}"

    def on_tab_switch(self, *args):
        tab_id = self.ids.home_tabs.get_current_tab().tab_label_text

        current_car = None
        if tab_id == "My Groups":
            current_car = self.ids.local_event_carou
        elif tab_id == "Local Events":
            current_car = self.ids.group_card_carou

        current_index = current_car.index + 1
        total_index = len(current_car.slides)
        self.carol_index = f"{current_index}/{total_index}"

    def on_carousel_slide(self, *args):

        tab_id = self.ids.home_tabs.get_current_tab().tab_label_text

        current_car = None
        if tab_id == "Local Events":
            current_car = self.ids.local_event_carou
        elif tab_id == "My Groups":
            current_car = self.ids.group_card_carou

        current_index = current_car.index + 1
        total_index = len(current_car.slides)
        self.carol_index = f"{current_index}/{total_index}"


class SignInPopup(Popup):
    def __init__(self, **kwargs):
        super(SignInPopup, self).__init__(**kwargs)
        self.title = f"Sign in first!"
        self.title_size = 36
        self.title_color = (1, 1, 1, 1)
        self.title_align = 'center'
        self.size_hint_y = 0.5
        self.size_hint_x = 0.5
        self.content = MDBoxLayout(orientation="vertical", spacing=dp(10), padding=dp(10))
        popup_label = MDLabel(
            text=f"Please sign in before proceeding!",
            text_size="root.size",
            valign="center", halign="center",
            font_style="H5",
            theme_text_color="Custom", text_color=(1, 1, 1, 1)
        )
        self.content.add_widget(popup_label)
        self.buttons_layout = MDBoxLayout(orientation="horizontal", spacing=dp(10))
        self.buttons_layout.add_widget(MDRaisedButton(text="Sign In!", on_release=self.go_sign_in, size_hint_x=.5))
        self.buttons_layout.add_widget(MDRaisedButton(text="Go Back", on_release=self.stay_here, size_hint_x=.5))
        self.content.add_widget(self.buttons_layout)

    def go_sign_in(self, instance):
        App.get_running_app().change_screen("sign_in_screen")
        self.dismiss()

    def stay_here(self, instance):
        self.dismiss()


class RedirectSitePopup(Popup):
    def __init__(self, item_text, **kwargs):
        super(RedirectSitePopup, self).__init__(**kwargs)
        self.item_text = item_text
        self.title = f"Warning! You are being redirected!"
        self.title_size = (self.size[0] + self.size[1]) / 15  # 42
        self.title_color = (1, 0, 0, 1)
        self.title_align = 'center'
        self.size_hint_y = 0.7
        self.size_hint_x = 0.7
        self.content = MDBoxLayout(orientation="vertical", spacing=dp(10), padding=dp(10))
        popup_label = MDLabel(
            text=f"You are going to '{item_text}'. This website is not controlled by us.",
            # text_size= "root.size",
            #text_size=root.size,#(self.size[0] + self.size[1]) / 15,  # 42
            valign="center", halign="center",
            #font_style="H5",
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


class SuccessPopup(Popup):
    type_response = ""

    def __init__(self, parent, type, **kwargs):
        super(SuccessPopup, self).__init__(**kwargs)
        self.class_parent = parent
        self.popup_type = type
        self.set_type_response(self.popup_type)
        self.title = f"Success!!!"
        self.size_hint_y = 0.5
        self.content = MDBoxLayout(orientation="vertical", spacing=dp(10), padding=dp(10))
        popup_label = MDLabel(
            text=self.type_response,
            theme_text_color="Custom", text_color=(1, 1, 1, 1)
        )
        self.content.add_widget(popup_label)
        self.buttons_layout = AnchorLayout(anchor_x='center', anchor_y='bottom')
        self.buttons_layout.add_widget(MDRaisedButton(text="Ok", on_release=self.on_ok))
        self.content.add_widget(self.buttons_layout)

    def set_type_response(self, popup_type):
        if popup_type == "delete card":
            self.type_response = "You successfully deleted the group!"

    def on_ok(self, instance):
        self.dismiss()
        self.class_parent.load_group_cards()