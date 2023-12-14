from kivy.app import App
from kivy.metrics import dp
from kivy.uix.popup import Popup
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.button import MDRaisedButton
from kivymd.uix.card import MDCard
from kivy.properties import StringProperty, NumericProperty, ObjectProperty
from kivymd.uix.label import MDLabel

MONTHS = {
    1: "Jan",
    2: "Feb",
    3: "Mar",
    4: "Apr",
    5: "May",
    6: "Jun",
    7: "Jul",
    8: "Aug",
    9: "Sep",
    10: "Oct",
    11: "Nov",
    12: "Dec"
}

DAYS_OF_WEEK = {
    0: "Monday",
    1: "Tuesday",
    2: "Wednesday",
    3: "Thursday",
    4: "Friday",
    5: "Saturday",
    6: "Sunday",
}

class GroupCard(MDCard):

    title = StringProperty()
    description = StringProperty()

    user_status = StringProperty()
    month = NumericProperty()
    day = NumericProperty()
    dow = StringProperty()
    time = StringProperty()
    location = StringProperty()

    image_path = StringProperty()

    session_length = StringProperty()
    participant = StringProperty()

    home_screen = ObjectProperty()
    game_group_screen = ObjectProperty()

    delete_group_popup = None

    def __init__(self, game_group, database_ref, *args, **kwargs):
        self.game_group_screen = game_group
        self.delete_group_popup = DeleteGroupCardPopup(self.game_group_screen.group_title, database_ref)
        super().__init__(*args, **kwargs)
        

    def on_pre_enter(self, *args):
        pass


    def load_depends(self, load_deps=None):
        pass

    def get_month(self, month_n: int):
        return MONTHS[month_n]

    def open_delete_card_popup(self):
        if not self.delete_group_popup.home_screen_set:
            home_screen_ref = App.get_running_app().main_screen_manager.get_screen("home_screen")
            self.delete_group_popup.set_home_screen(home_screen_ref)
        self.delete_group_popup.open()


    def open_game_group_screen(self):
        App.get_running_app().change_screen("game_group_screen", direction="right", load_deps=self.game_group_screen)

    def create_group_card(self, group_card_info, home_screen):
        return GroupCard(
            title=group_card_info.title,
            description=group_card_info.description,
            user_status=group_card_info.user_status,
            month=group_card_info.month,
            day=group_card_info.day,
            dow=group_card_info.dow,
            time=group_card_info.time,
            location=group_card_info.location,
            image_path=group_card_info.image_path,
            session_length=group_card_info.session_length,
            participant=group_card_info.participant,
            home_screen=home_screen,
            game_group=group_card_info.game_group_screen,
        )


class DeleteGroupCardPopup(Popup):
    home_screen_ref = None
    home_screen_set = False
    def __init__(self, card_title, database, **kwargs):
        super(DeleteGroupCardPopup, self).__init__(**kwargs)
        self.group_card_title = card_title
        self.database_ref = database
        self.title = f"Delete Group Card Warning"
        self.size_hint_y = 0.5
        self.content = MDBoxLayout(orientation="vertical", spacing=dp(10), padding=dp(10))
        popup_label = MDLabel(
            text=f"Are you sure you want to delete '{self.group_card_title}'?\nThis will also delete the group "
                 f"page! This action cannot be undone!",
            theme_text_color="Custom", text_color=(1, 1, 1, 1)
        )
        self.content.add_widget(popup_label)
        self.buttons_layout = MDBoxLayout(orientation="horizontal", spacing=dp(10))
        self.buttons_layout.add_widget(MDRaisedButton(text="Cancel", on_release=self.on_go_back))
        self.buttons_layout.add_widget(MDRaisedButton(text="Delete Group", on_release=self.on_delete_group))
        self.content.add_widget(self.buttons_layout)

    def set_home_screen(self, home_screen):
        self.home_screen_ref = home_screen
        self.home_screen_set = True

    def on_delete_group(self, instance):
        self.dismiss()
        self.database_ref.remove_group_card_info(self.group_card_title)
        self.home_screen_ref.deletion_successful()

    def on_go_back(self, instance):
        self.dismiss()