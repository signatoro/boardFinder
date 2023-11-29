from kivy.app import App
from kivy.metrics import dp
from kivy.properties import StringProperty, ListProperty, DictProperty
from kivy.tools.packaging.pyinstaller_hooks.pyi_rth_kivy import root
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.popup import Popup
from kivy.uix.screenmanager import Screen
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.button import MDRaisedButton
from kivymd.uix.chip import MDChip
from kivymd.uix.label import MDLabel

'''
Load Deps Dictionary:

"board_game_list": [str]
"group_image": ""
"group_name": ""
"group_general_description: ""
"group_additional_description": ""
"group_mtg_day_and_recurring_info": {"dow": recurring (bool)}
"group_mtg_start_time": ""
"group_mtg_end_time": ""
"group_mtg_location": ""
"group_max_players": ""
"group_host_fname": ""
"group_host_lname": ""
"group_host_email": ""
"group_host_phone_num": ""
"group_tags": [chip]
"new_group": bool

new_group is for notifying whether to render gameGroupHostScreen with Publish/Edit (true) or with Close/Edit (false)
'''


class GameGroupHostScreen(Screen):
    group_title = StringProperty()
    group_image = StringProperty()
    group_general_description = StringProperty()
    group_additional_description = StringProperty()
    group_board_games = ListProperty()
    group_host_fname = StringProperty()
    group_host_lname = StringProperty()
    group_host_email = StringProperty()
    group_host_phone_num = StringProperty()
    group_tags = ListProperty()
    group_max_players = StringProperty()
    group_meeting_location = StringProperty()
    # day_meetings = []
    group_mtg_day_and_recurring_info = DictProperty()
    group_meeting_start_time = StringProperty()
    group_meeting_end_time = StringProperty()

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
        self.group_max_players = load_deps["group_max_players"]
        self.group_meeting_location = load_deps["group_mtg_location"]
        self.group_mtg_day_and_recurring_info = load_deps["group_mtg_day_and_recurring_info"]
        self.group_meeting_start_time = load_deps["group_mtg_start_time"]
        self.group_meeting_end_time = load_deps["group_mtg_end_time"]
        self.add_meeting_days_and_times()
        self.add_board_games()
        self.add_host_to_member_list()
        self.set_looking_for_players()

    def add_meeting_days_and_times(self):
        self.ids.game_group_days_and_times.clear_widgets()
        for dow, recurring in self.group_mtg_day_and_recurring_info.items():
            day_label = MDLabel()
            if recurring:
                day_label.text = f"Every {dow}, {self.group_meeting_start_time} - {self.group_meeting_end_time}"
            else:
                day_label.text = f"This {dow}, {self.group_meeting_start_time} - {self.group_meeting_end_time}"
            day_label.text_color = [1, 1, 1, 1]
            self.ids.game_group_days_and_times.add_widget(day_label)

            meeting_type = MDLabel()
            if recurring:
                meeting_type.text = "RECURRING"
            else:
                meeting_type.text = "ONE-TIME"
            meeting_type.text_color = (1, 1, 1, 1)
            meeting_type.md_bg_color = App.get_running_app().theme_cls.primary_color
            self.ids.game_group_days_and_times.add_widget(meeting_type)

    def add_board_games(self):
        self.ids.game_group_board_games.clear_widgets()

        for bg in self.group_board_games:
            chip = MDChip(
                text=bg
            )
            # chip.size_hint = (1,.3)
            chip.md_bg_color = [.5, .7, .7, 1]
            chip.text_color = [1, 1, 1, 1]
            self.ids.game_group_board_games.add_widget(chip)

    def add_host_to_member_list(self):
        self.ids.game_group_users_list.clear_widgets()

        host_layout = MDBoxLayout(orientation="horizontal", adaptive_width=True)

        # Name Label
        name_label = MDLabel(
            text=f"{self.group_host_fname} {self.group_host_lname}",
            halign="center"
        )
        host_layout.add_widget(name_label)

        # Host/Member Label
        status_label = MDLabel(
            text="Host",
            halign="center"
        )
        host_layout.add_widget(status_label)

        self.ids.game_group_users_list.add_widget(host_layout)

    def set_looking_for_players(self):
        self.ids.game_group_max_players.text = f"Looking for {int(self.group_max_players) - 1} / {self.group_max_players} more players"

    def open_publish_warning_popup(self):
        warning_popup = PublishPostWarningPopup(self)
        warning_popup.open()

    def publish_group(self):
        print("publishing post...")
        # create game group page with class object

        # add class object to groups list

        # create game card for group

        # add to home screen carousel (and give it class object to store)

        # generate popup
        success_popup = PublishSuccessPopup(self)
        success_popup.open()


class PublishPostWarningPopup(Popup):
    def __init__(self, parent, **kwargs):
        super(PublishPostWarningPopup, self).__init__(**kwargs)
        self.parent = parent
        self.title = f"Publish Post Warning"
        self.size_hint_y = 0.5
        self.content = MDBoxLayout(orientation="vertical", spacing=dp(10), padding=dp(10))
        popup_label = MDLabel(
            text=f"Please ensure the information on the page is accurate. These edits can be changed at any point by "
                 f"you, the host. Press Publish! if you are ready to publish your group posting.",
            theme_text_color="Custom", text_color=(1, 1, 1, 1)
        )
        self.content.add_widget(popup_label)
        self.buttons_layout = MDBoxLayout(orientation="horizontal", spacing=dp(10))
        self.buttons_layout.add_widget(MDRaisedButton(text="Go Back", on_release=self.on_go_back))
        self.buttons_layout.add_widget(MDRaisedButton(text="Publish!", on_release=self.on_publish))
        self.content.add_widget(self.buttons_layout)

    def on_publish(self, instance):
        self.dismiss()
        self.parent.publish_group()

    def on_go_back(self, instance):
        self.dismiss()


class PublishSuccessPopup(Popup):
    def __init__(self, parent, **kwargs):
        super(PublishSuccessPopup, self).__init__(**kwargs)
        self.parent = parent
        self.title = f"Publish Success!"
        self.size_hint_y = 0.5
        self.content = MDBoxLayout(orientation="vertical", spacing=dp(10), padding=dp(10))
        popup_label = MDLabel(
            text=f"Your group posting was successfully published! You can view it on the Find Group Listings or "
                 f"through the group cards in the MyGroup slides on the Home Page! Be on the lookout for users "
                 f"requesting to join!",
            theme_text_color="Custom", text_color=(1, 1, 1, 1)
        )
        self.content.add_widget(popup_label)
        self.buttons_layout = AnchorLayout(anchor_x='center', anchor_y='bottom')
        self.buttons_layout.add_widget(MDRaisedButton(text="Ok", on_release=self.on_ok))
        self.content.add_widget(self.buttons_layout)

    def on_ok(self, instance):
        self.dismiss()


class DOWMeeting:
    dow = None
    recurring = None
    start_time = None
    end_time = None

    def __init__(self, **kwargs):
        super(DOWMeeting, self).__init__(**kwargs)

    def add_to_game_group_day_stack(self):
        day_label = MDLabel()
        if self.recurring:
            day_label.text = f"Every {self.dow}, {self.start_time} - {self.end_time}"
        else:
            day_label.text = f"This {self.dow}, {self.start_time} - {self.end_time}"
        day_label.text_color = [1, 1, 1, 1]
        root.ids.game_group_days_and_times.add_widget(day_label)

        meeting_type = MDLabel()
        if self.recurring:
            meeting_type.text = "RECURRING"
        else:
            meeting_type.text = "ONE-TIME"
        meeting_type.text_color = (1, 1, 1, 1)
        meeting_type.md_bg_color = App.get_running_app().theme_cls.primary_color
        root.ids.game_group_days_and_times.add_widget(meeting_type)
