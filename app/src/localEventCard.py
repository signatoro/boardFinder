
from kivymd.uix.card import MDCard
from kivy.properties import StringProperty, ListProperty, IntProperty



class LocalEventCard(MDCard):

    title= StringProperty()
    event_link= StringProperty()
    description= StringProperty()

    location_type= StringProperty()

    month: IntProperty()
    day: int

    # TODO: figure out how to do this.
    # Time 7:00pm or 11:00am
    time: IntProperty()
    location= StringProperty()

    def load_depends(self, load_deps=None):
        pass
    pass