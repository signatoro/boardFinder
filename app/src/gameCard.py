from kivymd.uix.chip import MDChip
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
        self.add_tags()

    def on_kv_post(self, *args):
        self.add_tags()

    def add_tags(self):
        self.ids.tag_box.clear_widgets()
        for tag in self.tags:
            chip = MDChip(
                    text=tag
                )
            # chip.size_hint = (1,.3)
            chip.md_bg_color= [.5,.7,.7,1]
            chip.text_color = [1,1,1,1]
            self.ids.tag_box.add_widget(chip)

    def on_card_click(self):

        pass
