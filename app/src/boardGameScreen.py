# from kivy.uix import webview
import asyncio
from kivy.app import App
from kivymd.uix.screen import MDScreen
from kivy.properties import StringProperty, ListProperty

from kivy.app import App
from kivy.metrics import dp
from kivy.clock import Clock
from kivy.uix.popup import Popup
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.button import MDRaisedButton
from kivymd.uix.label import MDLabel
from kivymd.uix.chip import MDChip


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

    def load_depends(self, load_deps=None):

        data = asyncio.run(App.get_running_app().make_get_api_call(f"/boardFinder/boardgames/{load_deps}"))

        print("Loading Deps")
        self.title: str = data["title"]
        self.image_path: str = data["image_path"]
        self.general_description: str = data["general_description"]
        self.main_description: str = data["main_description"]
        self.tutorial_video_link: str = data["tutorial_video_link"]

        self.tags: list[str] = data["tags"]
        self.helpful_links: list[str] = data["helpful_links"]

        self.add_urls()
        self.add_tags()

    def add_urls(self):
        self.ids.url_stack.clear_widgets()
        
        for url in self.helpful_links:
            chip = MDChip(
                text=url,
                on_release= lambda x=f"{url}": self.create_redirect_popup(x),
            )
            chip.size_hint = (1,.3)
            chip.text_color = App.get_running_app().theme_cls.primary_color
            self.ids.url_stack.add_widget(chip)

        pass

    def add_tags(self):
        self.ids.tags_stack.clear_widgets()
        for tag in self.tags:
            chip = MDChip(
                    text=tag
                )
            # chip.size_hint = (1,.3)
            chip.md_bg_color= [.5,.7,.7,1]
            chip.text_color = [1,1,1,1]
            self.ids.tags_stack.add_widget(chip)

    def create_redirect_popup(self, url:str):
        delete_popup = RedirectSitePopup(url.text)
        delete_popup.open()
        pass



class RedirectSitePopup(Popup):
    def __init__(self, item_text, **kwargs):
        super(RedirectSitePopup, self).__init__(**kwargs)
        self.item_text = item_text
        self.title = f"!!  Warning  !! You are being redirected !!  Warning  !!"
        self.title_size = 42
        self.title_color = (1, 0, 0, 1)
        self.title_align = 'center'
        self.size_hint_y = 0.5
        self.size_hint_x = 0.5
        self.content = MDBoxLayout(orientation="vertical", spacing=dp(10), padding=dp(10))
        popup_label = MDLabel(
            text=f"You are going to '{item_text}. This website is not controlled by us!'?",
            text_size= "root.size",
            valign ="center", halign = "center",
            font_style = "H5",
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