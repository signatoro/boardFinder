from kivy.app import App
from kivy.metrics import dp
from kivy.uix.popup import Popup
from kivy.uix.screenmanager import Screen, SlideTransition
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.button import MDRaisedButton
from kivymd.uix.chip import MDChip
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


class CreateGroupScreen(Screen):
    # current_progress_bar_window_value = 0
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
            App.get_running_app().change_screen("home_screen")
            return

        screen_manager.transition = SlideTransition(direction=direction)
        screen_manager.current = screen_name
        self.ids.progress_bar.value = self.display_progress_bar_value()

    def display_progress_bar_value(self):
        return self.currPrefPage / 6


class CreateGroupScreenPref1(Screen):
    selected_games = []

    def __init__(self, parent, **kwargs):
        super(CreateGroupScreenPref1, self).__init__(**kwargs)
        self.class_parent = parent

    def generate_search_game_options(self, text):
        # if there is an empty field, clear widgets
        if text == "":
            self.ids.game_results.clear_widgets()
            return

        # Clear previous search results
        self.ids.game_results.clear_widgets()

        # Filter data based on the search text
        search_results = [item for item in games_list if item.lower().startswith(text.lower())]

        # Display the filtered results
        for result in search_results:
            list_item = OneLineAvatarIconListItem(text=result)
            list_item.bind(on_touch_down=self.on_item_touch)
            icon = IconRightWidget(icon="plus")
            list_item.add_widget(icon)
            # list_item.bind(on_touch_down=self.on_item_touch)
            self.ids.game_results.add_widget(list_item)

    def on_item_touch(self, instance, touch):
        if instance.collide_point(*touch.pos):
            # Check if the item is not already in the selected items list
            if instance.text not in self.selected_games:
                # Add the item to the selected items list
                self.selected_games.append(instance.text)
                # Update the selected items MDList
                self.update_selected_games()

    def update_selected_games(self):
        # Clear the selected items MDList
        self.ids.selected_games.clear_widgets()

        # Display the selected items in the MDList
        for item in self.selected_games:
            list_item = OneLineAvatarIconListItem(text=item)
            icon = IconRightWidget(icon="minus", on_release=self.show_delete_popup)
            icon.list_item_ref = list_item
            list_item.add_widget(icon)
            self.ids.selected_games.add_widget(list_item)

    def on_search_focus(self, value):
        # Clear the search results when the text field loses focus
        if not value:
            self.ids.game_results.clear_widgets()
            self.ids.search_board_game.text = ""

    def show_delete_popup(self, instance):
        # Display a popup asking for confirmation to delete the item
        item = getattr(instance, "list_item_ref", None)
        if item:
            delete_popup = DeleteItemPopup(item.text, self.delete_item)
            delete_popup.open()

    def delete_item(self, item_text):
        self.selected_games.remove(item_text)
        self.update_selected_games()


class CreateGroupScreenPref2(Screen):
    image_source = ""

    def __init__(self, parent, **kwargs):
        super(CreateGroupScreenPref2, self).__init__(**kwargs)
        self.class_parent = parent
        self.imagePopup = PopupImageSelection(self)

    def open_image_popup(self):
        self.imagePopup.open()


class CreateGroupScreenPref3(Screen):
    menu_items = []
    max_players = 0

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

    def setup_dow_menu(self):
        for day in days:
            item = {
                "text": f"{day}",
                "viewclass": "MDDropDownItem",
                "on_release": lambda x=f"{day}": self.menu_callback(x),
            }
            self.menu_items.append(item)

    def menu_callback(self, text_item):
        self.ids.dow_button.text = text_item
        self.menu.dismiss()

    def show_days_dropdown(self):

        self.ids.dow_drop_down_selection.set_item(days)
        self.ids.dow_drop_down_selection.bind(on_release=self.on_dropdown_select)

    def on_dropdown_select(self, instance_drop):
        selected_day = instance_drop.get_item()
        if selected_day:
            self.ids.dow_drop_down_selection.text = selected_day

    def get_start_time(self, instance, time):
        self.ids.start_time_button.text = str(time)

    def get_end_time(self, instance, time):
        self.ids.end_time_button.text = str(time)

    def open_time_button(self, btn_type):
        time_dialog = MDTimePicker()
        if btn_type == "start":
            time_dialog.bind(time=self.get_start_time)
        elif btn_type == "end":
            time_dialog.bind(time=self.get_end_time)
        time_dialog.open()

    def set_mp_slider_value(self, mp_slider_val):
        new_mp = math.floor(mp_slider_val)
        self.max_players = new_mp

        if new_mp == 10:
           return "10+"
        else:
            return str(new_mp)



class CreateGroupScreenPref4(Screen):
    def __init__(self, parent, **kwargs):
        super(CreateGroupScreenPref4, self).__init__(**kwargs)
        self.class_parent = parent


class CreateGroupScreenPref5(Screen):
    def __init__(self, parent, **kwargs):
        super(CreateGroupScreenPref5, self).__init__(**kwargs)
        self.class_parent = parent


class CreateGroupScreenPref6(Screen):
    added_tags = {}

    def __init__(self, parent, **kwargs):
        super(CreateGroupScreenPref6, self).__init__(**kwargs)
        self.class_parent = parent
        self.display_database_tags()

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
            else:
                self.added_tags[instance.text] = False
            instance.md_bg_color = (0.2, 0.7, 0.2, 1)
            if self.added_tags[instance.text]:
                self.update_common_tags(instance)
        else:
            instance.md_bg_color = (0.74, 0.74, 0.74, 1)
            if self.added_tags[instance.text]:
                self.ids.common_tags.remove_widget(instance)
            del self.added_tags[instance.text]

    def on_list_item_clicked(self, instance):
        self.ids.tag_results.clear_widgets()
        self.ids.search_tags.text = ""
        if instance.text not in self.added_tags:
            # Add the item to the selected items list
            if self.is_tag_unique(instance.text):
                self.added_tags[instance.text] = True
                self.update_common_tags(instance)
            else:
                self.added_tags[instance.text] = False
                for chip in self.ids.common_tags.children:
                    if chip.text == instance.text:
                        chip.md_bg_color = (0.2, 0.7, 0.2, 1)
        else:
            for chip in self.ids.common_tags.children:
                if chip.text == instance.text:
                    chip.md_bg_color = (0.74, 0.74, 0.74, 1)
            del self.added_tags[instance.text]


    def is_tag_unique(self, tag):
        return tag not in tags_list

    def update_common_tags(self, instance):
        # Display the selected items in the MDList
        chip = MDChip(
            text=instance.text,
            on_release=self.on_tag_click,
        )
        chip.md_bg_color = (0.2, 0.7, 0.2, 1)
        self.ids.common_tags.add_widget(chip)


class PopupImageSelection(Popup):
    def __init__(self, parent, **kwargs):
        super(PopupImageSelection, self).__init__(**kwargs)
        self.group_screen = parent
        self.title = f"Select Group Image"

    def select_image(self, image_source):
        self.group_screen.image_source = image_source
        self.group_screen.ids.group_image.source = image_source
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
