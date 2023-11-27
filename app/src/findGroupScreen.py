from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.popup import Popup
from kivy.uix.screenmanager import Screen, SlideTransition
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.button import MDFillRoundFlatIconButton
from kivymd.uix.label import MDLabel
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
        else:
            self.chosen_genres.append(str(genre_chip.text))
            genre_chip.active = True

    def player_count_set(self, value):
        self.child2.ids.player_count_label.text = str(value)
        if value > 7:
            self.child2.ids.player_count_label.text = "8+"

    def player_variation_set(self, value):
        self.child2.ids.player_variation_label.text = str(int(value))
        if value > 4:
            self.child2.ids.player_variation_label.text = "Any Amount"
        if value < 1:
            self.child2.ids.player_variation_label.text = "Exact Number"

    def time_pressed(self, button, time):
        if button.text == "Free!":
            button.text = ""
            self.free_times.remove(time)
        else:
            button.text = "Free!"
            self.free_times.append(time)
    #     self.button_to_set = button
    #     Clock.schedule_once(self.delayed_color_set, 0.1)
    #
    # def delayed_color_set(self, *args):
    #     self.button_to_set.md_bg_color = "black"


class FindGroupScreenPref1(Screen):
    def __init__(self, parent, **kwargs):
        super(FindGroupScreenPref1, self).__init__(**kwargs)
        self.class_parent = parent
        self.genrePopup = GenrePopup(self)

    def open_genre_popup(self):
        self.genrePopup.open()


class FindGroupScreenPref2(Screen):
    def __init__(self, parent, **kwargs):
        super(FindGroupScreenPref2, self).__init__(**kwargs)
        self.class_parent = parent


class FindGroupScreenPref3(Screen):
    menu_items = []

    def __init__(self, parent, **kwargs):
        super(FindGroupScreenPref3, self).__init__(**kwargs)
        self.class_parent = parent
        self.menu = MDDropdownMenu(
            items=self.menu_items,
            width_mult=4,
        )


class GenrePopup(Popup):
    def __init__(self, parent, **kwargs):
        super(GenrePopup, self).__init__(**kwargs)
        self.group_screen = parent
        self.title = 'Genre Explanations'
        self.size_hint_x = 0.85
        self.size_hint_y = 0.9

        info_text = "Genre Definitions: \n\n" + \
                    "TTRPG: Table Top Role-Playing Games like Dungeons and Dragons where players act as characters in a story. \n\n" + \
                    "Strategy: A broad genre that includes any games where players must strategize and plan their actions to achieve victory. \n\n" + \
                    "Euro Games: Typically strategy-focused games designed around player choice over randomness, with passive competition over aggressive conflict. \n\n" + \
                    "Competitive: All encompassing category for games with competition between players as a main factor. \n\n" + \
                    "Social Deduction: Games with social interactions between players where deceiving your opponents is key to victory. \n\n" + \
                    "Family Games: Any family-friendly board games for adults and kids. \n\n" + \
                    "Card Games: Typically simple games that revolve around playing with a deck of cards, including both the common deck or something more like Uno. \n\n" + \
                    "TCG: Trading Card Games are games like Magic the Gathering and Yu-Gi-Oh, where players collect cards and create decks to play with. \n\n" + \
                    "War Games: Usually complex games where players control armies of units in a battle to take victory over the other army. \n\n"
        self.add_widget(
            MDBoxLayout(
                MDLabel(
                    valign='center',
                    halign='center',
                    markup=True,
                    text='[color=ffffff]'+info_text,
                    size_hint_x=1,
                    size_hint_y=1
                ),
                Button(
                    text="Ok",
                    on_release=self.dismiss,
                    size_hint_x=1, size_hint_y=0.1
                ),
                orientation='vertical',
            )
        )

    def select_image(self, image_source):
        self.group_screen.ids.group_image.source = image_source
        self.dismiss()
