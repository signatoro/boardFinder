from kivymd.uix.screen import MDScreen

'''
Load Deps Dictionary:

"board_game_list": [str]
"group_image": ""
"group_name": ""
"group_general_description: ""
"group_additional_description": ""
"group_mtg_day_and_recurring_info": {"dow": recurring (bool)}
"group_mtg_start_time": int
"group_mtg_end_time": int
"group_mtg_location": ""
"group_max_players": int
"group_host_fname": ""
"group_host_lname": ""
"group_host_email": ""
"group_host_phone_num": ""
"group_tags": [chip]
"new_group": bool

new_group is for notifying whether to render gameGroupHostScreen with Publish/Edit (true) or with Close/Edit (false)
'''


class GameGroupHostScreen(MDScreen):
    group_title = ""
    group_image = ""
    group_general_description = ""
    group_additional_description = ""
    group_board_games = []
    group_host_fname = ""
    group_host_lname = ""
    group_host_email = ""
    group_host_phone_num = ""
    group_tags = []
    group_max_players = 0
    group_meeting_location = ""
    group_meeting_dow = []
    group_meeting_start_times = {}
    group_meeting_end_times = {}
    group_meeting_recurring = False

    def load_depends(self, load_deps):
        self.group_title = load_deps["group_name"]
        self.group_image = load_deps["group_image"]
        self.group_general_description = load_deps["group_general_description"]
        self.group_additional_description = load_deps["group_additional_description"]
        self.group_board_games = load_deps["board_game_list"]
        self.group_host_fname = load_deps["group_host_fname"]
        self.group_host_lname = load_deps["group_host_lname"]
        self.group_host_email = load_deps["group_host_email"]
        self.group_host_phone_num = load_deps["group_host_phone_num"]
        self.group_tags = load_deps["group_tags"]
        group_max_players = 0
        group_meeting_location = ""
        group_meeting_dow = []
        group_meeting_start_times = {}
        group_meeting_end_times = {}
        group_meeting_recurring = False

    def add_urls(self):
        self.ids.url_stack.clear_widgets()

        for url in self.helpful_links:
            chip = MDChip(
                text=url,
                on_release=lambda x=f"{url}": self.create_redirect_popup(x),
            )
            chip.size_hint = (1, .3)
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
            chip.md_bg_color = [.5, .7, .7, 1]
            chip.text_color = [1, 1, 1, 1]
            self.ids.tags_stack.add_widget(chip)

    def create_redirect_popup(self, url: str):
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
            text_size="root.size",
            valign="center", halign="center",
            font_style="H5",
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