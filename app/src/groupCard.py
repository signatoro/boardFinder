
from kivymd.uix.card import MDCard
from kivy.properties import StringProperty, NumericProperty, ObjectProperty


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

    title= StringProperty()
    description= StringProperty()

    user_status = StringProperty()
    month= NumericProperty()
    day= NumericProperty()
    time= StringProperty()
    location= StringProperty()

    image_path = StringProperty()

    session_length= StringProperty()
    participant = StringProperty()

    parent_screen = ObjectProperty() 

    def __init__(self, parent, *args, **kwargs):
        self.parent_screen = parent
        super().__init__(*args, **kwargs)

    def load_depends(self, load_deps=None):
        pass

    def get_month(self, month_n: int):
        return MONTHS[month_n]
    
    def get_day_of_week(self, day_n:int):
        return DAYS_OF_WEEK[day_n] 
    