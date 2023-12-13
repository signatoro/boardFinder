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

    def __init__(self, game_group, *args, **kwargs):
        self.game_group_screen = game_group
        super().__init__(*args, **kwargs)
        

    def on_pre_enter(self, *args):
        if not self.delete_group_popup:
            self.delete_group_popup = DeleteGroupCardPopup(self, self.game_group_screen, App.get_running_app().main_screen_manager.get_screen("home_screen"))


    def load_depends(self, load_deps=None):
        pass

    def get_month(self, month_n: int):
        return MONTHS[month_n]

    def open_delete_card_popup(self):
        self.delete_group_popup.open()

    def open_game_group_screen(self):
        App.get_running_app().change_screen("game_group_screen", direction="right", load_deps=self.game_group_screen)


class DeleteGroupCardPopup(Popup):
    def __init__(self, game_card, game_group, home_screen, **kwargs):
        super(DeleteGroupCardPopup, self).__init__(**kwargs)
        self.card_parent = game_card
        self.game_group_ref = game_group
        self.app_home_screen = home_screen
        self.title = f"Delete Group Card Warning"
        self.size_hint_y = 0.5
        self.content = MDBoxLayout(orientation="vertical", spacing=dp(10), padding=dp(10))
        popup_label = MDLabel(
            text=f"Are you sure you want to delete '{self.card_parent.title}'?\nThis will also delete the group "
                 f"page! This action cannot be undone!",
            theme_text_color="Custom", text_color=(1, 1, 1, 1)
        )
        self.content.add_widget(popup_label)
        self.buttons_layout = MDBoxLayout(orientation="horizontal", spacing=dp(10))
        self.buttons_layout.add_widget(MDRaisedButton(text="Cancel", on_release=self.on_go_back))
        self.buttons_layout.add_widget(MDRaisedButton(text="Delete Group", on_release=self.on_delete_group))
        self.content.add_widget(self.buttons_layout)

    def on_delete_group(self, instance):
        self.dismiss()
        if self.game_group_ref:
            self.game_group_ref.delete_group()
        self.app_home_screen.remove_group_card_and_refresh(self.card_parent)

    def on_go_back(self, instance):
        self.dismiss()