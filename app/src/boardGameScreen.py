# from kivy.uix import webview
from kivymd.uix.screen import MDScreen
from kivy.properties import StringProperty, ListProperty
from kivy.uix.videoplayer import VideoPlayer

'''
play_time: int
    max_players: int

    title: str
    image_path: str
    general_description: str
    tutorial_video_link: str

    tags: list[str]
    helpful_links: list[str]
'''
class BoardGameScreen(MDScreen):
    # max_players: int

    title = StringProperty()
    image_path = StringProperty()
    general_description = StringProperty()
    main_description = StringProperty()
    tutorial_video_link = StringProperty()

    tags = ListProperty([])
    helpful_links = ListProperty([])

    def load_depends(self, load_deps):
        print("Loading Deps")
        self.title: str = load_deps
        self.image_path: str = 'images/HELLOTHERE.jpg'
        self.general_description: str = 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam.'
        self.main_description: str = 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Integer nec odio. Praesent libero. Sed cursus ante dapibus diam. Sed nisi. Nulla quis sem at nibh elementum imperdiet. Duis sagittis ipsum. Praesent mauris. Fusce nec tellus sed augue semper porta. Mauris massa. Vestibulum lacinia arcu eget nulla. Class aptent taciti sociosqu ad litora torquent per conubia nostra, per inceptos himenaeos.'
        self.tutorial_video_link: str = 'videos/Videotemp1.mp4'

        self.tags: list[str] = ['Helpful', 'Awesome', 'Cool']
        self.helpful_links: list[str] = ['Long.link.1', 'Long.link.2', 'Long.link.3']
