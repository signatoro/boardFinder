



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

class GroupListCard(MDCard):

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

    def __init__(self, *args, **kwargs):
  
        super().__init__(*args, **kwargs)


    def load_depends(self, load_deps=None):
        pass

    def get_month(self, month_n: int):
        return MONTHS[month_n]

    def open_game_group_screen(self):
        App.get_running_app().change_screen("game_group_screen", direction="right", load_deps=self.game_group_screen)


