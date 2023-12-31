
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
        print("Loading Deps")
        # TODO: Get the board game json data and fill it out
        
        data = App.get_running_app().get_database().get_board_game(load_deps)

        print("This is the data for the board game screen.")
        print(data['title'])
        print(data['image_path'])
        print(data['general_description'])

        self.title: str = data['title']
        self.image_path = data["image_path"]
        self.general_description = data['general_description']
        self.main_description = data["main_description"]
        self.tutorial_video_link = data["tutorial_video_link"]

        self.tags = data["tags"]
        self.helpful_links = data["helpful_links"]

        self.add_urls()
        self.add_tags()
        

    def add_urls(self):
        self.ids.url_stack.clear_widgets()
        
        for url in self.helpful_links:
            # MDLabel:
                        #     id: game_group_host_name
                        #     text: f"Name: {root.group_host_fname} {root.group_host_lname}"
                        #     color: [.2, .2, .2, 1]
                        #     font_size: 24
                        #     size_hint_x: 1
                        #     size_hint_y: None
                        #     halign: "left"
                        #     height: self.texture_size[1]
            # chip = MDChip(
            #     text=url,
            #     on_release= lambda x=f"{url}": self.create_redirect_popup(x),
            # )
            chip = MDChip(text= url,
                # theme_text_color= "Custom",
                text_color = [.2,.2,.8,1],
                # underline = True,
                font_size= 24,
                size_hint_x = 1,
                size_hint_y = None,
                halign = "left",
                on_release= lambda x=f"{url}": self.create_redirect_popup(x),
            )

            # chip.size_hint = (1,.3)
            # chip.text_color = App.get_running_app().theme_cls.primary_color
            self.ids.url_stack.add_widget(chip)

        pass

    def add_tags(self):
        self.ids.tags_list.clear_widgets()
        for tag in self.tags:
            chip = MDChip(
                    text=tag
                )
            # chip.size_hint = (1,.3)
            chip.md_bg_color= [.5,.7,.7,1]
            chip.text_color = [1,1,1,1]
            self.ids.tags_list.add_widget(chip)

    def create_redirect_popup(self, url:str):
        delete_popup = RedirectSitePopup(url.text)
        delete_popup.open()
        pass


class RedirectSitePopup(Popup):
    def __init__(self, item_text, **kwargs):
        super(RedirectSitePopup, self).__init__(**kwargs)
        self.item_text = item_text
        self.title = f"Warning! You are being redirected!"
        self.title_size = (self.size[0] + self.size[1]) / 15  # 42
        self.title_color = (1, 0, 0, 1)
        self.title_align = 'center'
        self.size_hint_y = 0.7
        self.size_hint_x = 0.7
        self.content = MDBoxLayout(orientation="vertical", spacing=dp(10), padding=dp(10))
        popup_label = MDLabel(
            text=f"You are going to '{item_text}. This website is not controlled by us.",
            #text_size= "root.size",
            valign ="center", halign = "center",
            #font_style = "H5",
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