from kivymd.uix.card import MDCard
from kivy.properties import StringProperty

'''
parent: Screen
first_name: str
last_name: str
avatar_path: str
member_type: str
'''
class UserCard(MDCard):
    first_name = StringProperty()
    last_name = StringProperty()
    avatar_path = StringProperty()
    #member_type = None

    def __init__(self,*args, **kwargs):
        super().__init__(*args, **kwargs)

    def load_depends(self, load_deps=None):
        pass

    def on_card_click(self):
        # Perform action when the card is clicked
        print("Card Clicked!")

    def get_full_name(self):
        return f"{self.first_name} {self.last_name}"

    def get_first_name(self):
        return self.first_name
