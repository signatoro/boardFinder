from kivy.app import App
from kivy.metrics import dp
from kivy.properties import StringProperty, ListProperty, DictProperty, BooleanProperty, ObjectProperty, Clock
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.popup import Popup
from kivy.uix.screenmanager import Screen
from kivy.uix.widget import Widget
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.button import MDRaisedButton
from kivymd.uix.chip import MDChip
from kivymd.uix.label import MDLabel

from src.userCard import UserCard


class SeparatorLine(Widget):
    pass


'''
Load Deps Dictionary:

"board_game_list": [str]
"group_image": ""
"group_title": ""
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
"owner": bool

new_group is for notifying whether to render gameGroupScreen with Publish/Edit (true) or with Close/Edit (false)
'''


class GameGroupScreen(Screen):
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
    new_group = BooleanProperty()
    owner = BooleanProperty()

    warning_popup = None
    success_popup = None
    delete_group_warning_popup = None
    deletion_success_popup = None
    actionButtonEditAndPublishReference = ObjectProperty()
    actionButtonRequestToJoinReference = ObjectProperty()
    actionButtonEditOrDeleteReference = ObjectProperty()
    actionButtonLeaveGroupReference = ObjectProperty()
    home_screen_reference = None
    list_of_members = []
    prev_screen = None

    def __init__(self, **kwargs):
        super(GameGroupScreen, self).__init__(**kwargs)
        self.warning_popup = PublishPostWarningPopup(parent=self)
        self.success_popup = PublishSuccessPopup(parent=self)
        self.delete_group_warning_popup = DeletePostWarningPopup(parent=self)
        self.deletion_success_popup = DeletePostSuccessPopup(parent=self)
        self.actionButtonEditAndPublishReference = GameGroupActionButtonsEditAndPublish()
        self.actionButtonRequestToJoinReference = GameGroupActionButtonsRequestToJoin()
        self.actionButtonEditOrDeleteReference = GameGroupActionButtonsEditOrDelete()
        self.actionButtonLeaveGroupReference = GameGroupActionButtonsLeave()
        Clock.schedule_once(self.setup_action_buttons, 0)

    def on_pre_enter(self, *args):
        print("pre enter called")
        # Access the ScreenManager and get the HomeScreen
        self.home_screen_reference = App.get_running_app().main_screen_manager.get_screen("home_screen")
        print(f"owner: {self.owner}")
        print(f"new_group: {self.new_group}")

        # after create a group
        if self.owner and self.new_group:
            self.add_edit_and_publish_action_buttons()
        # host looks at group after creating
        elif self.owner and not self.new_group:
            self.add_edit_or_delete_action_buttons()
        # member looks at group that is published
        elif not self.owner and not self.new_group:
            self.add_leave_group_action_buttons()
        else:
            self.add_request_to_join_action_button()

    def setup_action_buttons(self, *args):
        self.actionButtonEditAndPublishReference.game_group_screen = self
        self.actionButtonRequestToJoinReference.game_group_screen = self
        self.actionButtonEditOrDeleteReference.game_group_screen = self
        self.actionButtonLeaveGroupReference.game_group_screen = self

    def add_request_to_join_action_button(self):
        if self.ids.game_group_action_button_container:
            self.ids.game_group_action_button_container.clear_widgets()
            self.ids.game_group_action_button_container.add_widget(self.actionButtonRequestToJoinReference)

    def add_edit_and_publish_action_buttons(self):
        if self.ids.game_group_action_button_container:
            self.ids.game_group_action_button_container.clear_widgets()
            self.ids.game_group_action_button_container.add_widget(self.actionButtonEditAndPublishReference)

    def add_edit_or_delete_action_buttons(self):
        if self.ids.game_group_action_button_container:
            self.ids.game_group_action_button_container.clear_widgets()
            self.ids.game_group_action_button_container.add_widget(self.actionButtonEditOrDeleteReference)

    def add_leave_group_action_buttons(self):
        if self.ids.game_group_action_button_container:
            self.ids.game_group_action_button_container.clear_widgets()
            self.ids.game_group_action_button_container.add_widget(self.actionButtonLeaveGroupReference)

    def go_to_page_before(self):
        if self.prev_screen:
            App.get_running_app().change_screen(self.prev_screen)

    def delete_group(self):
        App.get_running_app().remove_group(self)
        if self.home_screen_reference:
            self.home_screen_reference.delete_group_card(game_group_screen_info=self)
        #del self


    def proceed_to_delete(self):
        self.deletion_success_popup.open()

    def load_depends(self, load_deps, prev_screen):
        print("load depends called")
        self.group_title = load_deps["group_title"]
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
        self.new_group = load_deps["new_group"]
        self.owner = load_deps["owner"]
        self.add_meeting_days_and_times()
        self.add_board_games()
        self.add_host_to_member_list()
        self.set_looking_for_players()
        self.render_tags()
        App.get_running_app().add_group(self)
        self.prev_screen = prev_screen


    def load_screen_data(self, game_group_data, prev_screen):
        print("load screen data called")
        self.group_title = game_group_data.group_title
        self.group_image = game_group_data.group_image
        self.group_general_description = game_group_data.group_general_description
        self.group_additional_description = game_group_data.group_additional_description
        self.group_board_games = game_group_data.group_board_games
        self.group_host_fname = game_group_data.group_host_fname
        self.group_host_lname = game_group_data.group_host_lname
        self.group_host_email = game_group_data.group_host_email
        self.group_host_phone_num = game_group_data.group_host_phone_num
        self.group_tags = game_group_data.group_tags
        self.group_max_players = game_group_data.group_max_players
        self.group_meeting_location = game_group_data.group_meeting_location
        self.group_mtg_day_and_recurring_info = game_group_data.group_mtg_day_and_recurring_info
        self.group_meeting_start_time = game_group_data.group_meeting_start_time
        self.group_meeting_end_time = game_group_data.group_meeting_end_time
        self.new_group = game_group_data.new_group
        self.owner = game_group_data.owner
        self.add_meeting_days_and_times()
        self.add_board_games()
        self.add_host_to_member_list()
        self.set_looking_for_players()
        self.render_tags()
        self.prev_screen = prev_screen

    def render_tags(self):
        self.ids.group_tags_list.clear_widgets()
        for tag in self.group_tags:
            # clear former parent of tag
            tag.parent = None
            self.ids.group_tags_list.add_widget(tag)

    def add_meeting_days_and_times(self):
        self.ids.game_group_days_and_times.clear_widgets()
        for dow, recurring in self.group_mtg_day_and_recurring_info.items():
            day_label = MDLabel()
            if recurring:
                day_label.text = f"Every {dow}, {self.group_meeting_start_time} - {self.group_meeting_end_time}"
            else:
                day_label.text = f"This {dow}, {self.group_meeting_start_time} - {self.group_meeting_end_time}"
            day_label.text_color = [0, 0, 0, 1]
            self.ids.game_group_days_and_times.add_widget(day_label)

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

        '''
        UserCard: 
            first_name: str
            last_name: str
            avatar_path: str
            member_type: str
        '''

        host_card = UserCard(
            first_name=self.group_host_fname,
            last_name=self.group_host_lname,
            avatar_path="images/avatar_stock.png",
            member_type="Host",
        )
        self.ids.game_group_users_list.add_widget(host_card)
        self.list_of_members.append(host_card)

    def set_looking_for_players(self):
        self.ids.game_group_max_players.text = f"Looking for {int(self.group_max_players) - 1} / {self.group_max_players} more players"

    def open_publish_warning_popup(self):
        self.warning_popup.open()

    def publish_group(self):
        print("publish group called")
        self.new_group = False

        # send info to home screen for it to create a game card
        self.home_screen_reference.add_created_group_card(game_group_screen_info=self)

        # generate popup
        self.success_popup.open()

    def request_to_join(self):
        print("request to join called")
        #self.new_group = False

        # send info to home screen for it to create a game card
        #self.home_screen_reference.add_created_group_card(game_group_screen_info=self)

        # generate popup
        #self.success_popup.open()


class PublishPostWarningPopup(Popup):
    def __init__(self, parent, **kwargs):
        super(PublishPostWarningPopup, self).__init__(**kwargs)
        self.class_parent = parent
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
        self.class_parent.publish_group()

    def on_go_back(self, instance):
        self.dismiss()


class PublishSuccessPopup(Popup):
    def __init__(self, parent, **kwargs):
        super(PublishSuccessPopup, self).__init__(**kwargs)
        self.class_parent = parent
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
        App.get_running_app().change_screen("home_screen")


class DeletePostWarningPopup(Popup):
    def __init__(self, parent, **kwargs):
        super(DeletePostWarningPopup, self).__init__(**kwargs)
        self.class_parent = parent
        self.title = f"Delete Post Warning"
        self.size_hint_y = 0.5
        self.content = MDBoxLayout(orientation="vertical", spacing=dp(10), padding=dp(10))
        popup_label = MDLabel(
            text=f"Pressing Delete will permanently delete this group! Please ensure this is what you want to do before proceeding!",
            theme_text_color="Custom", text_color=(1, 1, 1, 1)
        )
        self.content.add_widget(popup_label)
        self.buttons_layout = MDBoxLayout(orientation="horizontal", spacing=dp(10))
        self.buttons_layout.add_widget(MDRaisedButton(text="Go Back", on_release=self.on_go_back))
        self.buttons_layout.add_widget(MDRaisedButton(text="Delete", on_release=self.on_delete))
        self.content.add_widget(self.buttons_layout)

    def on_delete(self, instance):
        self.dismiss()
        self.class_parent.proceed_to_delete()

    def on_go_back(self, instance):
        self.dismiss()


class DeletePostSuccessPopup(Popup):
    def __init__(self, parent, **kwargs):
        super(DeletePostSuccessPopup, self).__init__(**kwargs)
        self.class_parent = parent
        self.title = f"Deletion Success!"
        self.size_hint_y = 0.5
        self.content = MDBoxLayout(orientation="vertical", spacing=dp(10), padding=dp(10))
        popup_label = MDLabel(
            text=f"Your group posting was successfully deleted. You can recreate it again by going through Create A Group.",
            theme_text_color="Custom", text_color=(1, 1, 1, 1)
        )
        self.content.add_widget(popup_label)
        self.buttons_layout = AnchorLayout(anchor_x='center', anchor_y='bottom')
        self.buttons_layout.add_widget(MDRaisedButton(text="Ok", on_release=self.on_ok))
        self.content.add_widget(self.buttons_layout)

    def on_ok(self, instance):
        self.dismiss()
        self.class_parent.delete_group()
        App.get_running_app().change_screen("home_screen")


class GameGroupActionButtonsEditAndPublish(MDBoxLayout):
    game_group_screen = ObjectProperty()

    def __init__(self, **kwargs):
        super(GameGroupActionButtonsEditAndPublish, self).__init__(**kwargs)

    def open_publish_warning_popup(self):
        self.game_group_screen.warning_popup.open()


class GameGroupActionButtonsRequestToJoin(MDBoxLayout):
    game_group_screen = ObjectProperty()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def request_to_join(self):
        self.game_group_screen.request_to_join()


class GameGroupActionButtonsEditOrDelete(MDBoxLayout):
    game_group_screen = ObjectProperty()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def open_delete_group_popup(self):
        self.game_group_screen.delete_group_warning_popup.open()


class GameGroupActionButtonsLeave(MDBoxLayout):
    game_group_screen = ObjectProperty()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def open_leave_group_popup(self):
        self.game_group_screen.leave_group_popup.open()


