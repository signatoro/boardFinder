from kivy.app import App
from kivy.uix.popup import Popup
from kivy.uix.screenmanager import Screen, SlideTransition
from kivymd.uix.menu import MDDropdownMenu
from kivymd.uix.pickers import MDTimePicker

games_list = 'sorry,monopoly,risk,catan,mancala,gameoflife,chess,gloomhaven,scrabble,jenga,codenames'.split(
    ',')
days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]


class CreateGroupScreen(Screen):
    # current_progress_bar_window_value = 0
    currPrefPage = 1
    screen_name = ""

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.screen_name = "create_group_pref1"
        self.child1 = CreateGroupScreenPref1(self)
        self.child2 = CreateGroupScreenPref2(self)
        self.child3 = CreateGroupScreenPref3(self)
        self.child4 = CreateGroupScreenPref4(self)
        self.child5 = CreateGroupScreenPref5(self)
        self.child6 = CreateGroupScreenPref6(self)

    def on_parent(self, widget, parent):
        if parent:
            # The parent is set, meaning the widget tree is constructed
            self.ids.create_group_screen_manager.add_widget(self.child1)
            self.ids.create_group_screen_manager.add_widget(self.child2)
            self.ids.create_group_screen_manager.add_widget(self.child3)
            self.ids.create_group_screen_manager.add_widget(self.child4)
            self.ids.create_group_screen_manager.add_widget(self.child5)
            self.ids.create_group_screen_manager.add_widget(self.child6)

    def load_next_pref_page(self, pref_page, direction="left"):
        # Get the screen manager from the kv file
        screen_manager = self.ids.create_group_screen_manager
        # If going left, change the transition. Else make left the default
        screen_name = ""
        if pref_page == 0:
            self.currPrefPage = 1
            screen_name = "create_group_pref1"
        if pref_page == 1:
            self.currPrefPage = 2
            screen_name = "create_group_pref2"
        elif pref_page == 2:
            self.currPrefPage = 3
            screen_name = "create_group_pref3"
        elif pref_page == 3:
            self.currPrefPage = 4
            screen_name = "create_group_pref4"
        elif pref_page == 4:
            self.currPrefPage = 5
            screen_name = "create_group_pref5"
        elif pref_page == 5:
            self.currPrefPage = 6
            screen_name = "create_group_pref6"

        screen_manager.transition = SlideTransition(direction=direction)
        screen_manager.current = screen_name
        self.ids.progress_bar.value = self.display_progress_bar_value()
        self.ids.progress_bar_value_label.text = self.display_progress_bar_label()

    def display_progress_bar_value(self):
        if self.currPrefPage == 1:
            return 1 / 6
        elif self.currPrefPage == 2:
            return 2 / 6
        elif self.currPrefPage == 3:
            return 3 / 6
        elif self.currPrefPage == 4:
            return 4 / 6
        elif self.currPrefPage == 5:
            return 5 / 6
        elif self.currPrefPage == 6:
            return 6 / 6

    def display_progress_bar_label(self):
        if self.currPrefPage == 1:
            return "1 / 6"
        elif self.currPrefPage == 2:
            return "2 / 6"
        elif self.currPrefPage == 3:
            return "3 / 6"
        elif self.currPrefPage == 4:
            return "4 / 6"
        elif self.currPrefPage == 5:
            return "5 / 6"
        elif self.currPrefPage == 6:
            return "6 / 6"


class CreateGroupScreenPref1(Screen):
    def __init__(self, parent, **kwargs):
        super(CreateGroupScreenPref1, self).__init__(**kwargs)
        self.class_parent = parent

    def generate_search_game_options(self, value):
        # filtered_option_list = list(set(option_list + value[:value.rfind(' ')].split(' ')))
        # val = value[value.rfind(' ') + 1:]
        # if not val:
        #     return
        # try:
        #     option_data = []
        #     for i in range(len(option_list)):
        #         word = [word for word in option_list if word.startswith(val)][0][len(val):]
        #         if not word:
        #             return
        #         if self.text + word in option_list:
        #             if self.text + word not in app.option_data:
        #                 popped_suggest = option_list.pop(option_list.index(str(self.text + word)))
        #                 app.option_data.append(popped_suggest)
        #         app.update_data(app.option_data)
        #
        #     except IndexError:
        #
        #         pass
        return


class CreateGroupScreenPref2(Screen):
    def __init__(self, parent, **kwargs):
        super(CreateGroupScreenPref2, self).__init__(**kwargs)
        self.class_parent = parent
        self.imagePopup = PopupImageSelection(self)

    def open_image_popup(self):
        self.imagePopup.open()


class CreateGroupScreenPref3(Screen):
    menu_items = []

    def __init__(self, parent, **kwargs):
        super(CreateGroupScreenPref3, self).__init__(**kwargs)
        self.class_parent = parent
        self.setup_dow_menu()
        self.menu = MDDropdownMenu(
            caller=self.ids.dow_button,
            items=self.menu_items,
            width_mult=4,
        )

    def setup_dow_menu(self):
        for day in days:
            item =  {
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


class CreateGroupScreenPref4(Screen):
    def __init__(self, parent, **kwargs):
        super(CreateGroupScreenPref4, self).__init__(**kwargs)
        self.class_parent = parent


class CreateGroupScreenPref5(Screen):
    def __init__(self, parent, **kwargs):
        super(CreateGroupScreenPref5, self).__init__(**kwargs)
        self.class_parent = parent


class CreateGroupScreenPref6(Screen):
    def __init__(self, parent, **kwargs):
        super(CreateGroupScreenPref6, self).__init__(**kwargs)
        self.class_parent = parent


class PopupImageSelection(Popup):
    def __init__(self, parent, **kwargs):
        super(PopupImageSelection, self).__init__(**kwargs)
        self.group_screen = parent

    def select_image(self, image_source):
        self.group_screen.ids.group_image.source = image_source
        self.dismiss()