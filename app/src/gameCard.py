
from kivymd.uix.card import MDCard
from kivy.properties import StringProperty, ListProperty


class GameCard(MDCard):

    title = StringProperty()
    image_path = StringProperty()
    general_description = StringProperty()
    main_description = StringProperty()
    tutorial_video_link = StringProperty()

    tags = ListProperty([])
    helpful_links = ListProperty([])


    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
    
    def pre_load(self):
        self.title = self.title
        self.image_path = 'images/pikachu.jpg'
        self.general_description = 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam.'
        self.main_description= 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Integer nec odio. Praesent libero. Sed cursus ante dapibus diam. Sed nisi. Nulla quis sem at nibh elementum imperdiet. Duis sagittis ipsum. Praesent mauris. Fusce nec tellus sed augue semper porta. Mauris massa. Vestibulum lacinia arcu eget nulla. Class aptent taciti sociosqu ad litora torquent per conubia nostra, per inceptos himenaeos.'
        self.tutorial_video_link = 'videos/Videotemp1.mp4'

        self.tags: list[str] = ['Helpful', 'Awesome', 'Cool', 'Fun', 'Engaging', 'Fun']
        self.helpful_links: list[str] = ['Long.link.1', 'Long.link.2', 'Long.link.3']

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