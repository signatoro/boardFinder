
from kivymd.uix.card import MDCard
from kivymd.uix.chip import MDChip
from kivy.properties import StringProperty, ListProperty


class GameCard(MDCard):

    id: str

    title = StringProperty()
    image_path = StringProperty()
    general_description = StringProperty()
    main_description = StringProperty()
    tutorial_video_link = StringProperty()

    tags = ListProperty([])
    helpful_links = ListProperty([])


    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
    
    def pre_load(self, load_deps=None):

        self.add_tags()
        #self.title = "Catan"
        # self.image_path = 'images/pikachu.jpg'
        # self.general_description = 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam.'
        # self.main_description= 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Integer nec odio. Praesent libero. Sed cursus ante dapibus diam. Sed nisi. Nulla quis sem at nibh elementum imperdiet. Duis sagittis ipsum. Praesent mauris. Fusce nec tellus sed augue semper porta. Mauris massa. Vestibulum lacinia arcu eget nulla. Class aptent taciti sociosqu ad litora torquent per conubia nostra, per inceptos himenaeos.'
        # self.tutorial_video_link = 'videos/Videotemp1.mp4'

        # self.tags: list[str] = ['Helpful', 'Awesome', 'Cool']
        # self.helpful_links: list[str] = ['Long.link.1', 'Long.link.2', 'Long.link.3']
        pass

            #label: 'Pill Shape'
            #     text: "Family Game"
            #     font_size: self.width/5  
            #     icon: 'pill'
            #     type: 'outline'
            #     pos_hint: {'center_x': 0.5}
            #     size_hint_y: 0.5# 

    def add_tags(self):
        self.ids.tags_box.clear_widgets()
        for tag in self.tags:
            chip = MDChip(
                    text=tag
                )
            # chip.size_hint = (1,.3)
            chip.md_bg_color= [.5,.7,.7,1]
            chip.text_color = [1,1,1,1]
            chip.size_hint_max_y = 0.25
            self.ids.tags_box.add_widget(chip)


    def on_card_click(self):
        # if self.collide_point(*touch.pos):
            # Perform action when the card is clicked
        print("Card Clicked!")
