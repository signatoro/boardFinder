from kivy.app import App
from kivy.uix.popup import Popup
from kivy.uix.screenmanager import Screen, SlideTransition

games_list = 'sorry,monopoly,risk,catan,mancala,gameoflife,chess,gloomhaven,scrabble,jenga,codenames'.split(
    ',')


class CreateGroupScreen(Screen):
    # current_progress_bar_window_value = 0
    currPrefPage = 1
    screen_name = ""

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.screen_name = "create_group_pref1"
        self.child1 = CreateGroupScreenPref1(self)
        self.child2 = CreateGroupScreenPref2(self)

    def on_parent(self, widget, parent):
        if parent:
            # The parent is set, meaning the widget tree is constructed
            self.ids.create_group_screen_manager.add_widget(self.child1)
            self.ids.create_group_screen_manager.add_widget(self.child2)
    def load_next_pref_page(self, pref_page):
        # Get the screen manager from the kv file
        screen_manager = self.ids.create_group_screen_manager
        # If going left, change the transition. Else make left the default
        screen_name = ""
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

        screen_manager.transition = SlideTransition(direction="left")

        screen_manager.current = screen_name

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
            return 1


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


class PopupImageSelection(Popup):
    def __init__(self, parent, **kwargs):
        super(PopupImageSelection, self).__init__(**kwargs)
        self.group_screen = parent

    def select_image(self, image_source):
        self.group_screen.ids.group_image.source = image_source
        self.dismiss()



