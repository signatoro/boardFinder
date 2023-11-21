from kivy.app import App
from kivy.uix.popup import Popup
from kivy.uix.screenmanager import Screen, SlideTransition
from kivymd.uix.menu import MDDropdownMenu
from kivy.clock import Clock
from kivymd.uix.pickers import MDTimePicker

games_list = 'sorry,monopoly,risk,catan,mancala,gameoflife,chess,gloomhaven,scrabble,jenga,codenames'.split(
    ',')
days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]


class FindGroupScreen(Screen):
    # current_progress_bar_window_value = 0
    currPrefPage = 1
    screen_name = ""
    initialized = False
    chosen_genres = []
    free_times = []

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.screen_name = "find_group_pref1"
        self.chosen_genres = []
        self.free_times = []
        if not self.initialized:
            self.child1 = FindGroupScreenPref1(self)
            self.child2 = FindGroupScreenPref2(self)
            self.child3 = FindGroupScreenPref3(self)

    def on_parent(self, widget, parent):
        if parent:
            # The parent is set, meaning the widget tree is constructed
            if not self.initialized:
                self.ids.find_group_screen_manager.add_widget(self.child1)
                self.ids.find_group_screen_manager.add_widget(self.child2)
                self.ids.find_group_screen_manager.add_widget(self.child3)
                self.ids.main_label.text = "Genres"
                self.initialized = True

    def load_next_pref_page(self, pref_page):
        # Get the screen manager from the kv file
        screen_manager = self.ids.find_group_screen_manager

        # If going left, change the transition. Else make left the default
        direction = "left"
        if pref_page < self.currPrefPage:
            direction = "right"

        screen_name = ""
        if pref_page == 0:
            self.currPrefPage = 1
            self.ids.main_label.text = "Genres"
            screen_name = "find_group_pref1"
        if pref_page == 1:
            self.currPrefPage = 2
            self.ids.main_label.text = "Players"
            screen_name = "find_group_pref2"
        elif pref_page == 2:
            self.currPrefPage = 3
            self.ids.main_label.text = "Times"
            screen_name = "find_group_pref3"

        screen_manager.transition = SlideTransition(direction=direction)
        screen_manager.current = screen_name
        # self.ids.progress_bar.value = self.display_progress_bar_value()
        # self.ids.progress_bar_value_label.text = self.display_progress_bar_label()

    def display_progress_bar_value(self):
        return self.currPrefPage / 3

    def display_progress_bar_label(self):
        return str(self.currPrefPage) + " / 3"

    def selected_genre(self, genre_chip):
        if str(genre_chip.text) in self.chosen_genres:
        # if genre_chip.active:
            self.chosen_genres.remove(str(genre_chip.text))
            genre_chip.active = False
            print("active")
        else:
            self.chosen_genres.append(str(genre_chip.text))
            genre_chip.active = True
            print("not active")
        print(self.chosen_genres)

    def player_count_set(self, value):
        self.child2.ids.player_count_label.text = str(value)
        if value > 7:
            self.child2.ids.player_count_label.text = "8+"

    def player_variation_set(self, value):
        self.child2.ids.player_variation_label.text = str(value)
        if value > 4:
            self.child2.ids.player_variation_label.text = "Any Amount"

    def time_pressed(self, button, time):
        if button.text == "Free!":
            button.text = ""
            self.free_times.remove(time)
        else:
            button.text = "Free!"
            self.free_times.append(time)
        print(self.free_times)
    #     self.button_to_set = button
    #     Clock.schedule_once(self.delayed_color_set, 0.1)
    #
    # def delayed_color_set(self, *args):
    #     self.button_to_set.md_bg_color = "black"


class FindGroupScreenPref1(Screen):
    def __init__(self, parent, **kwargs):
        super(FindGroupScreenPref1, self).__init__(**kwargs)
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


class FindGroupScreenPref2(Screen):
    def __init__(self, parent, **kwargs):
        super(FindGroupScreenPref2, self).__init__(**kwargs)
        self.class_parent = parent
        self.imagePopup = PopupImageSelection(self)

    # def open_image_popup(self):
    #     self.imagePopup.open()


class FindGroupScreenPref3(Screen):
    menu_items = []

    def __init__(self, parent, **kwargs):
        super(FindGroupScreenPref3, self).__init__(**kwargs)
        self.class_parent = parent
        # self.setup_dow_menu()
        self.menu = MDDropdownMenu(
            #caller=self.ids.dow_button,
            items=self.menu_items,
            width_mult=4,
        )

    # def setup_dow_menu(self):
    #     for day in days:
    #         item =  {
    #                 "text": f"{day}",
    #                 "viewclass": "MDDropDownItem",
    #                 "on_release": lambda x=f"{day}": self.menu_callback(x),
    #         }
    #         self.menu_items.append(item)
    #
    # def menu_callback(self, text_item):
    #     self.ids.dow_button.text = text_item
    #     self.menu.dismiss()
    #
    # def show_days_dropdown(self):
    #
    #     self.ids.dow_drop_down_selection.set_item(days)
    #     self.ids.dow_drop_down_selection.bind(on_release=self.on_dropdown_select)
    #
    # def on_dropdown_select(self, instance_drop):
    #     selected_day = instance_drop.get_item()
    #     if selected_day:
    #         self.ids.dow_drop_down_selection.text = selected_day
    #
    # def get_start_time(self, instance, time):
    #     self.ids.start_time_button.text = str(time)
    #
    # def get_end_time(self, instance, time):
    #     self.ids.end_time_button.text = str(time)
    #
    # def open_time_button(self, btn_type):
    #     time_dialog = MDTimePicker()
    #     if btn_type == "start":
    #         time_dialog.bind(time=self.get_start_time)
    #     elif btn_type == "end":
    #         time_dialog.bind(time=self.get_end_time)
    #     time_dialog.open()


class PopupImageSelection(Popup):
    def __init__(self, parent, **kwargs):
        super(PopupImageSelection, self).__init__(**kwargs)
        self.group_screen = parent

    def select_image(self, image_source):
        self.group_screen.ids.group_image.source = image_source
        self.dismiss()
