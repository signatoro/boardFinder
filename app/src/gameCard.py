
from kivymd.uix.card import MDCard
from kivy.properties import StringProperty


class GameCard(MDCard):

    title = StringProperty()

    def on_card_click(self):
        # if self.collide_point(*touch.pos):
            # Perform action when the card is clicked
        print("Card Clicked!")


# class PostCard(MDCard):
#     profile_pic = StringProperty()
#     avatar = StringProperty()
#     username = StringProperty()
#     post = StringProperty()
#     caption = StringProperty()
#     likes = StringProperty()
#     posted_ago = StringProperty()
#     comments = StringProperty()