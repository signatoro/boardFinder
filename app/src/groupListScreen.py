from kivy.lang import Builder
from kivymd.uix.screen import MDScreen
from kivymd.uix.button import MDFlatButton
from kivymd.uix.list import OneLineListItem

from src.fake_base import Database
from src.groupListCard import GroupListCard



# Builder.load_file('/kv')
class GroupListScreen(MDScreen):
    group_lists = {}

    def on_pre_enter(self, *args):

        self.update_groups_list()

        return super().on_pre_enter(*args)

    def __init__(self, **kwargs):
        super(GroupListScreen, self).__init__(**kwargs)
        #self.add_game_card()
        self.database = Database()
        # self.update_groups_list()

    def on_enter(self, *args):
        self.update_groups_list()

    def load_depends(self, load_deps=None):
        # TODO call the endpoint to get data
        self.update_groups_list()
        pass

    

    # def add_new_group(self, new_group):
    #     self.ids.group_list.add_widget(new_group)
    #     self.group_lists[new_group.title] = new_group
    #     self.update_groups_list()

    def update_groups_list(self):
        self.group_lists = self.database.get_group_list_cards()
        self.ids.group_list.clear_widgets()

        for group in self.group_lists.values():
            self.ids.group_list.add_widget(group)

    def search_games(self, text):
        # Clear previous search results

        self.ids.search_board_game.clear_widgets()
        self.ids.group_list.clear_widgets()

        # Filter data based on the search text
        search_results = [item for item in self.group_lists.keys() if item.lower().startswith(text.lower())]

        # Display the filtered results
        for result in search_results:
            game_card = self.group_lists[result]
            self.ids.group_list.add_widget(game_card)
