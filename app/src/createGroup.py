from datetime import datetime

from kivy.app import App
from kivy.metrics import dp
from kivy.uix.popup import Popup
from kivy.uix.screenmanager import Screen, SlideTransition, NoTransition
from kivymd.uix.behaviors.toggle_behavior import MDToggleButton
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.button import MDRaisedButton, MDRectangleFlatButton
from kivymd.uix.chip import MDChip
from kivymd.uix.dropdownitem import MDDropDownItem
from kivymd.uix.label import MDLabel
from kivymd.uix.list import OneLineListItem, OneLineAvatarIconListItem, IconRightWidget
from kivymd.uix.menu import MDDropdownMenu
from kivymd.uix.pickers import MDTimePicker
import math

games_list = ('sorry,monopoly,risk,catan,mancala,gameoflife,chess,gloomhaven,scrabble,jenga,codenames,carcassonne,'
              'campaign').split(',')
tags_list = ('AllLevels,Casual,Hardcore,LGBTQIA+,Food Included,Pet Friendly,21+,Public Location,Private Location,'
             'Long-Term,Short-Term,Frequent Meeting,Free,New Players Welcome,Buy Materials,Materials Included,'
             'Women Only,Easy To Learn,Short-Game Length,Long-Game Length,Cosplay').split(',')
days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

created_groups_list = []

'''
Created Group Dictionary:

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

new_group is for notifying whether to render gameGroupHostScreen with Publish/Edit (true) or with Close/Edit (false)
'''


class CreateGroupScreen(Screen):
    new_created_group = {}
    currPrefPage = 1
    screen_name = ""
    initialized = False

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.screen_name = "create_group_pref1"
        if not self.initialized:
            self.child1 = CreateGroupScreenPref1(self)
            self.child2 = CreateGroupScreenPref2(self)
            self.child3 = CreateGroupScreenPref3(self)
            self.child4 = CreateGroupScreenPref4(self)
            self.child5 = CreateGroupScreenPref5(self)
            self.child6 = CreateGroupScreenPref6(self)

    def on_parent(self, widget, parent):
        if parent:
            # The parent is set, meaning the widget tree is constructed
            if not self.initialized:
                self.ids.create_group_screen_manager.add_widget(self.child1)
                self.ids.create_group_screen_manager.add_widget(self.child2)
                self.ids.create_group_screen_manager.add_widget(self.child3)
                self.ids.create_group_screen_manager.add_widget(self.child4)
                self.ids.create_group_screen_manager.add_widget(self.child5)
                self.ids.create_group_screen_manager.add_widget(self.child6)
                self.initialized = True

    def load_next_pref_page(self, pref_page, direction="left"):
        # Get the screen manager from the kv file
        screen_manager = self.ids.create_group_screen_manager
        # If going left, change the transition. Else make left the default
        if direction == "right":
            self.currPrefPage -= 1
        else:
            self.currPrefPage += 1
        screen_name = f"create_group_pref{self.currPrefPage}"

        if self.currPrefPage > 6:
            self.currPrefPage = 6
            self.new_created_group["new_group"] = True
            self.new_created_group["owner"] = True
            App.get_running_app().change_screen("game_group_screen", direction="left", load_deps=self.new_created_group)
            return

        screen_manager.transition = SlideTransition(direction=direction)
        screen_manager.current = screen_name
        self.ids.progress_bar.value = self.display_progress_bar_value()

    def display_progress_bar_value(self):
        return self.currPrefPage / 6

    def reset_fields(self):
        self.child1.reset_fields()
        self.child2.reset_fields()
        self.child3.reset_fields()
        self.child4.reset_fields()
        self.child5.reset_fields()
        self.child6.reset_fields()
        self.new_created_group = {}
        self.currPrefPage = 1
        self.screen_name = "create_group_pref1"
        screen_manager = self.ids.create_group_screen_manager
        screen_manager.transition = NoTransition()
        screen_manager.current = self.screen_name
        self.ids.progress_bar.value = self.display_progress_bar_value()


class CreateGroupScreenPref1(Screen):
    selected_games = []

    def __init__(self, parent, **kwargs):
        super(CreateGroupScreenPref1, self).__init__(**kwargs)
        self.class_parent = parent
        self.generate_all_games()
        self.update_buttons()

    def reset_fields(self):
        self.selected_games = []
        self.ids.selected_games.clear_widgets()
        self.generate_all_games()
        self.update_buttons()

    def generate_all_games(self):
        self.ids.game_results.clear_widgets()
        games_list.sort()
        for game in games_list:
            list_item = OneLineAvatarIconListItem(text=game,id=game)
            # list_item.bind(on_touch_down=self.on_item_touch)
            icon = IconRightWidget(icon="plus", on_release=self.on_item_touch)
            icon.list_item_ref = list_item
            list_item.add_widget(icon)
            # list_item.bind(on_touch_down=self.on_item_touch)
            self.ids.game_results.add_widget(list_item)

    def generate_search_game_options(self, text):
        # if there is an empty field, clear widgets
        # if text == "":
        #    self.ids.game_results.clear_widgets()
        #    return

        # Clear previous search results
        self.ids.game_results.clear_widgets()

        # Filter data based on the search text
        search_results = [item for item in games_list if item.lower().startswith(text.lower())]

        # Display the filtered results
        for result in search_results:
            list_item = OneLineAvatarIconListItem(text=result)
            # list_item.bind(on_touch_down=self.on_item_touch)
            icon = IconRightWidget(icon="plus", on_release=self.on_item_touch)
            icon.list_item_ref = list_item
            list_item.add_widget(icon)
            # list_item.bind(on_touch_down=self.on_item_touch)
            self.ids.game_results.add_widget(list_item)

    def on_item_touch(self, instance):
        # if instance.collide_point(*touch.pos):
        # get reference to list item
        game = getattr(instance, "list_item_ref", None)

        # Check if the item is not already in the selected items list
        if game.text not in self.selected_games:
            # Add the item to the selected items list
            self.selected_games.append(game.text)
            games_list.remove(game.text)
            # Update the selected items MDList
            self.update_selected_games()
            self.generate_all_games()
        self.update_buttons()

    def update_selected_games(self):
        # Clear the selected items MDList
        self.ids.selected_games.clear_widgets()

        if len(self.selected_games) > 0:
            self.ids.selected_games.padding = 0
        else:
            self.ids.selected_games.padding = dp(30)

        # Display the selected items in the MDList
        for item in self.selected_games:
            list_item = OneLineAvatarIconListItem(text=item)
            icon = IconRightWidget(icon="minus", on_release=self.show_delete_popup)
            icon.list_item_ref = list_item
            list_item.add_widget(icon)
            self.ids.selected_games.add_widget(list_item)

    def show_delete_popup(self, instance):
        # Display a popup asking for confirmation to delete the item
        item = getattr(instance, "list_item_ref", None)
        if item:
            delete_popup = DeleteItemPopup(item.text, self.delete_item)
            delete_popup.open()

    def delete_item(self, item_text):
        self.selected_games.remove(item_text)
        games_list.append(item_text)
        self.update_selected_games()
        self.generate_all_games()
        self.update_buttons()

    def add_data_to_final(self, new_page, direction="left"):
        self.class_parent.new_created_group["board_game_list"] = self.selected_games
        self.class_parent.load_next_pref_page(new_page, direction)

    def update_buttons(self):
        if len(self.selected_games) <= 0:
            self.ids.next_pref_button.disabled = True
            self.ids.next_pref_button.opacity = 0
        else:
            self.ids.next_pref_button.disabled = False
            self.ids.next_pref_button.opacity = 1


class CreateGroupScreenPref2(Screen):
    image_source = 'images/avatar_stock.png'
    general_description_text = ""
    group_title = ""
    curr_word_count = 0
    max_word_count = 0

    def __init__(self, parent, **kwargs):
        super(CreateGroupScreenPref2, self).__init__(**kwargs)
        self.class_parent = parent
        self.imagePopup = PopupImageSelection(self)
        self.max_word_count = self.ids.general_description_text_field.max_input_size
        self.update_buttons()

    def reset_fields(self):
        self.image_source = 'images/avatar_stock.png'
        self.general_description_text = ""
        self.group_title = ""
        self.curr_word_count = 0

        self.ids.group_image.source = 'images/avatar_stock.png'
        self.ids.group_title.text = ""
        self.ids.general_description_text_field.text = ""
        self.update_and_limit_word_count("")
        self.update_buttons()

    def set_group_title(self, text):
        self.group_title = text
        self.update_buttons()

    def open_image_popup(self):
        self.imagePopup.open()

    def update_and_limit_word_count(self, text):
        self.general_description_text = ' '.join(text.split())
        self.curr_word_count = len(text.split())
        if self.curr_word_count >= self.max_word_count:
            self.general_description_text = self.general_description_text[:self.max_word_count]
            self.ids.general_description_text_field.text = self.general_description_text
            self.curr_word_count = self.max_word_count
            self.ids.general_description_text_field.helper_text = f'Max Word Count Reached: {self.curr_word_count}/{self.max_word_count}'
        else:
            self.ids.general_description_text_field.helper_text = f'{self.curr_word_count}/{self.max_word_count}'
        self.update_buttons()

    def add_data_to_final(self, new_page, direction="left"):
        self.class_parent.new_created_group["group_image"] = self.image_source
        self.class_parent.new_created_group["group_title"] = self.group_title
        self.class_parent.new_created_group["group_general_description"] = self.general_description_text
        self.class_parent.load_next_pref_page(new_page, direction)

    def update_buttons(self):
        if self.group_title == "" or self.curr_word_count <= 0 or self.image_source == "":
            self.ids.next_pref_button.disabled = True
            self.ids.next_pref_button.opacity = 0
        else:
            self.ids.next_pref_button.disabled = False
            self.ids.next_pref_button.opacity = 1


class CreateGroupScreenPref3(Screen):
    meeting_days = {}
    dow = ""
    meeting_start_time = ""
    meeting_end_time = ""
    menu_items = []
    max_players = 0
    recurring_meeting = False
    meeting_location = ""

    def __init__(self, parent, **kwargs):
        super(CreateGroupScreenPref3, self).__init__(**kwargs)
        self.class_parent = parent
        self.setup_dow_menu()
        self.menu = MDDropdownMenu(
            caller=self.ids.dow_button,
            items=self.menu_items,
            width_mult=4,
        )
        self.max_players = 4
        self.ids.recurring_toggle_btn.set_parent(self)
        # self.ids.non_recurring_toggle_btn.set_parent(self)
        # self.update_buttons()

    def reset_fields(self):
        self.meeting_days.clear()
        self.dow = ""
        self.meeting_start_time = ""
        self.meeting_end_time = ""
        self.menu_items = []
        self.max_players = 0
        self.recurring_meeting = False
        self.meeting_location = ""

        self.ids.recurring_toggle_btn.text = "Non-Recurring"
        self.ids.recurring_toggle_btn.state = 'normal'
        self.ids.dow_button.text = "Select Day"
        self.ids.location_text_field.hint_text: "Ex: Boston Public Library"
        self.ids.location_text_field.text = ""
        self.ids.location_text_field.hint_text: "Ex: Boston Public Library"
        self.ids.max_players_slider.value = 4
        self.ids.start_time_button.text = "Select Start Time"
        self.ids.end_time_button.text = "Select End Time"
        self.update_buttons()

    def setup_dow_menu(self):
        for day in days:
            item = {
                "viewclass": "OneLineListItem",
                "text": f"{day}",
                "on_release": lambda x=f"{day}": self.menu_callback(x),
            }
            self.menu_items.append(item)
        # self.update_buttons()

    def menu_callback(self, text_item):
        self.ids.dow_button.text = text_item
        self.dow = text_item
        self.meeting_days.clear()
        self.meeting_days[text_item] = self.recurring_meeting
        self.menu.dismiss()
        self.update_buttons()

    def show_days_dropdown(self):
        self.ids.dow_drop_down_selection.set_item(days)
        self.ids.dow_drop_down_selection.bind(on_release=self.on_dropdown_select)
        self.update_buttons()

    def on_dropdown_select(self, instance_drop):
        selected_day = instance_drop.get_item()
        print(f"in dropdown select - {selected_day}")
        if selected_day:
            self.meeting_days.clear()
            self.ids.dow_drop_down_selection.text = selected_day.text
            self.meeting_days[selected_day.text] = self.recurring_meeting
        self.update_buttons()

    def get_start_time(self, instance, time):
        military_time = datetime.strptime(str(time), "%H:%M:%S")
        # Convert to 12-hour time format
        twelve_hr_time = military_time.strftime("%I:%M:%S %p")
        self.ids.start_time_button.text = str(twelve_hr_time)
        self.meeting_start_time = str(twelve_hr_time)
        self.update_buttons()

    def get_end_time(self, instance, time):
        military_time = datetime.strptime(str(time), "%H:%M:%S")
        # Convert to 12-hour time format
        twelve_hr_time = military_time.strftime("%I:%M:%S %p")
        self.ids.end_time_button.text = str(twelve_hr_time)
        self.meeting_end_time = str(twelve_hr_time)
        self.update_buttons()

    def open_time_button(self, btn_type):
        time_dialog = MDTimePicker()
        if btn_type == "start":
            time_dialog.bind(time=self.get_start_time)
        elif btn_type == "end":
            time_dialog.bind(time=self.get_end_time)
        time_dialog.open()
        self.update_buttons()

    def set_mp_slider_value(self, mp_slider_val):
        new_mp = math.floor(mp_slider_val)
        self.max_players = new_mp
        # self.update_buttons()
        if new_mp == 10:
            return "10+"
        else:
            return str(new_mp)

    def toggle_recurring_meeting(self, state):
        if state:
            self.ids.recurring_toggle_btn.text = "    Recurring    "
        else:
            self.ids.recurring_toggle_btn.text = "Non-Recurring"

        self.recurring_meeting = state
        if self.dow != "":
            self.meeting_days.clear()
            self.meeting_days[self.dow] = self.recurring_meeting
            # self.dow = ""
        self.update_buttons()

    def set_meeting_location(self, text):
        self.meeting_location = text
        self.update_buttons()

    def add_data_to_final(self, new_page, direction="left"):
        self.class_parent.new_created_group["group_mtg_day_and_recurring_info"] = self.meeting_days
        self.class_parent.new_created_group["group_mtg_start_time"] = self.meeting_start_time
        self.class_parent.new_created_group["group_mtg_end_time"] = self.meeting_end_time
        self.class_parent.new_created_group["group_max_players"] = str(self.max_players)
        self.class_parent.new_created_group["group_mtg_location"] = self.meeting_location
        self.class_parent.load_next_pref_page(new_page, direction)

    def update_buttons(self):
        if self.dow == "" \
                or self.meeting_start_time == "" \
                or self.meeting_end_time == "" \
                or self.meeting_location == "":
            self.ids.next_pref_button.disabled = True
            self.ids.next_pref_button.opacity = 0
        else:
            self.ids.next_pref_button.disabled = False
            self.ids.next_pref_button.opacity = 1


class CreateGroupScreenPref4(Screen):
    host_fname = ""
    host_lname = ""
    host_email = ""
    host_phone_num = ""

    def __init__(self, parent, **kwargs):
        super(CreateGroupScreenPref4, self).__init__(**kwargs)
        self.class_parent = parent
        self.update_buttons()

    def reset_fields(self):
        self.host_fname = ""
        self.host_lname = ""
        self.host_email = ""
        self.host_phone_num = ""
        self.ids.first_name_text_field.text = ""
        self.ids.last_name_text_field.text = ""
        self.ids.email_text_field.text = ""
        self.ids.phone_num_text_field.text = ""
        self.update_buttons()

    def set_host_fname(self, text):
        self.host_fname = text
        self.update_buttons()

    def set_host_lname(self, text):
        self.host_lname = text
        self.update_buttons()

    def set_host_email(self, text):
        self.host_email = text
        self.update_buttons()

    def set_host_phone_num(self, text):
        self.host_phone_num = text
        self.update_buttons()

    def on_text_validate(self, current_textfield, next_textfield):
        # Move to the next text field if it exists
        if next_textfield:
            next_textfield.focus = True
        self.update_buttons()


    def add_data_to_final(self, new_page, direction="left"):
        self.class_parent.new_created_group["group_host_fname"] = self.host_fname
        self.class_parent.new_created_group["group_host_lname"] = self.host_lname
        self.class_parent.new_created_group["group_host_email"] = self.host_email
        self.class_parent.new_created_group["group_host_phone_num"] = self.host_phone_num
        self.class_parent.load_next_pref_page(new_page, direction)

    def update_buttons(self):
        if self.host_fname == "" \
                or self.host_lname == "" \
                or self.host_email == "" \
                or self.host_phone_num == "":
            self.ids.next_pref_button.disabled = True
            self.ids.next_pref_button.opacity = 0
        else:
            self.ids.next_pref_button.disabled = False
            self.ids.next_pref_button.opacity = 1


class CreateGroupScreenPref5(Screen):
    added_tags = {}
    group_tags = []

    def __init__(self, parent, **kwargs):
        super(CreateGroupScreenPref5, self).__init__(**kwargs)
        self.class_parent = parent
        self.display_database_tags()

    def reset_fields(self):
        self.added_tags = {}
        self.group_tags = []
        self.ids.common_tags.clear_widgets()
        self.display_database_tags()
        # self.update_buttons()

    def display_database_tags(self):
        # Display the filtered results
        for tag in tags_list:
            chip = MDChip(
                text=tag,
                on_release=self.on_tag_click
            )
            chip.md_bg_color = (0.74, 0.74, 0.74, 1)
            self.ids.common_tags.add_widget(chip)

    def search_tags(self, text):
        # if there is an empty field, clear widgets
        unique_tag = False
        if text == "":
            self.ids.tag_results.clear_widgets()
            return

        # Clear previous search results
        self.ids.tag_results.clear_widgets()

        # Filter data based on the search text
        search_results = [item for item in tags_list if item.lower().startswith(text.lower())]

        # add user created tag
        if len(search_results) == 0:
            search_results.append(text)
            unique_tag = True

        # Display the filtered results
        for result in search_results:
            list_item = OneLineListItem(text=result)
            if unique_tag:
                list_item.text_color = (1, 0, 1, 1)
            list_item.bind(on_release=self.on_list_item_clicked)
            self.ids.tag_results.add_widget(list_item)

    def on_tag_click(self, instance):
        if instance.text not in self.added_tags:
            # Add the item to the selected items list
            if self.is_tag_unique(instance.text):
                self.added_tags[instance.text] = True
                self.update_common_tags(instance)#self.group_tags.append(instance)
            else:
                self.added_tags[instance.text] = False
                self.group_tags.append(instance)
            instance.md_bg_color = "teal"
            #if self.added_tags[instance.text]:
            #    self.update_common_tags(instance)
        else:
            instance.md_bg_color = (0.74, 0.74, 0.74, 1)
            if self.added_tags[instance.text]:
                self.ids.common_tags.remove_widget(instance)
            del self.added_tags[instance.text]
            self.group_tags.remove(instance)

    def on_list_item_clicked(self, instance):
        self.ids.tag_results.clear_widgets()
        # self.ids.search_tags.text = ""
        if instance.text not in self.added_tags:
            # Add the item to the selected items list
            if self.is_tag_unique(instance.text):
                self.added_tags[instance.text] = True
                # self.group_tags.append(instance)
                self.update_common_tags(instance)
            else:
                self.added_tags[instance.text] = False
                self.group_tags.append(instance)
                for chip in self.ids.common_tags.children:
                    if chip.text == instance.text:
                        chip.md_bg_color = "teal"
        else:
            for chip in self.ids.common_tags.children:
                if chip.text == instance.text:
                    chip.md_bg_color = (0.74, 0.74, 0.74, 1)
            del self.added_tags[instance.text]
            self.group_tags.remove(instance)

    def is_tag_unique(self, tag):
        return tag not in tags_list

    def update_common_tags(self, instance):
        # Display the selected items in the MDList
        chip = MDChip(
            text=instance.text,
            on_release=self.on_tag_click,
        )
        chip.md_bg_color = "teal"
        self.group_tags.append(chip)
        self.ids.common_tags.add_widget(chip)

    def add_data_to_final(self, new_page, direction="left"):
        self.class_parent.new_created_group["group_tags"] = self.group_tags
        self.class_parent.load_next_pref_page(new_page, direction)


class CreateGroupScreenPref6(Screen):
    field_default_text = ""
    additional_description_text = ""
    curr_word_count = 0
    max_word_count = 1000

    def __init__(self, parent, **kwargs):
        super(CreateGroupScreenPref6, self).__init__(**kwargs)
        self.curr_word_count = 0
        self.class_parent = parent
        self.field_default_text = ("Enter additional information: -rules to follow, -what to expect, "
                                   + "-what to bring, -will food be served?")
        self.ids.additional_info_text_field.text = ("Enter additional information: -rules to follow, -what to expect, "
                                                    + "-what to bring, -will food be served?")
        self.ids.additional_info_text_field.helper_text = f'0/{self.max_word_count}'
        # self.update_buttons()

    def reset_fields(self):
        self.ids.additional_info_text_field.text = ""
        self.clear_text(False)
        # self.update_buttons()

    def clear_text(self, is_focused):
        if is_focused and self.ids.additional_info_text_field.text == self.field_default_text:
            self.ids.additional_info_text_field.text = ""
        elif not is_focused and len(self.ids.additional_info_text_field.text) == 0:
            self.ids.additional_info_text_field.text = self.field_default_text
            self.ids.additional_info_text_field.helper_text = f'0/{self.max_word_count}'
        elif not is_focused and self.ids.additional_info_text_field.text == self.field_default_text:
            self.curr_word_count = 0
            self.ids.additional_info_text_field.helper_text = f'0/{self.max_word_count}'
        # self.update_buttons()

    def update_and_limit_word_count(self, text):
        self.additional_description_text = ' '.join(text.split())
        self.curr_word_count = len(text.split())
        if self.curr_word_count >= self.max_word_count:
            self.additional_description_text = self.additional_description_text[:self.max_word_count]
            self.ids.additional_info_text_field.text = self.additional_description_text
            self.curr_word_count = self.max_word_count
            self.ids.additional_info_text_field.helper_text = f'Max Word Count Reached: {self.curr_word_count}/{self.max_word_count}'
        else:
            self.ids.additional_info_text_field.helper_text = f'{self.curr_word_count}/{self.max_word_count}'
        # self.update_buttons()

    def add_data_to_final(self, new_page, direction="left"):
        self.class_parent.new_created_group["group_additional_description"] = self.additional_description_text
        self.class_parent.load_next_pref_page(new_page, direction)

    def update_buttons(self):
        if self.ids.additional_info_text_field.text == ""\
                or self.ids.additional_info_text_field.text == self.field_default_text:
            self.ids.next_pref_button.disabled = True
            self.ids.next_pref_button.opacity = 0
        else:
            self.ids.next_pref_button.disabled = False
            self.ids.next_pref_button.opacity = 1


class PopupImageSelection(Popup):
    def __init__(self, parent, **kwargs):
        super(PopupImageSelection, self).__init__(**kwargs)
        self.group_screen = parent
        self.title = f"Select Group Image"

    def select_image(self, img_source):
        print(f"img source - {img_source}")
        self.group_screen.image_source = img_source
        self.group_screen.ids.group_image.source = img_source
        self.group_screen.update_buttons()
        self.dismiss()


class DeleteItemPopup(Popup):
    def __init__(self, item_text, delete_callback, **kwargs):
        super(DeleteItemPopup, self).__init__(**kwargs)
        self.item_text = item_text
        self.delete_callback = delete_callback
        self.title = f"Delete Game From Added List"
        self.size_hint_y = 0.5
        self.content = MDBoxLayout(orientation="vertical", spacing=dp(10), padding=dp(10))
        popup_label = MDLabel(
            text=f"Are you sure you want to delete '{item_text}'?",
            theme_text_color="Custom", text_color=(1, 1, 1, 1)
        )
        self.content.add_widget(popup_label)
        self.buttons_layout = MDBoxLayout(orientation="horizontal", spacing=dp(10))
        self.buttons_layout.add_widget(MDRaisedButton(text="Yes", on_release=self.on_yes))
        self.buttons_layout.add_widget(MDRaisedButton(text="No", on_release=self.on_no))
        self.content.add_widget(self.buttons_layout)

    def on_yes(self, instance):
        self.dismiss()
        self.delete_callback(self.item_text)

    def on_no(self, instance):
        self.dismiss()


class MyToggleButton(MDRectangleFlatButton, MDToggleButton):
    def __init__(self, **kwargs):
        super(MyToggleButton, self).__init__(**kwargs)
        self.parent_instance = None
        self.background_down = "teal"

    def set_parent(self, pref_parent):
        self.parent_instance = pref_parent

    def on_toggle(self, text):
        if text == "    Recurring    ":
            self.parent_instance.toggle_recurring_meeting(False)
        else:
            self.parent_instance.toggle_recurring_meeting(True)

