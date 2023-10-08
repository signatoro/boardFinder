from kivy.app import App
from kivy.lang import Builder


class Controller(App):

    GUI = None

    def build(self):
        self.GUI = Builder.load_file("src/kv/main.kv")
        return self.GUI
    

    