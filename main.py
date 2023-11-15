# import src.view
# from src.controller import Controller


import uvicorn
from fastapi import FastAPI
from api.view import APIEndpoints

from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.image import Image
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.carousel import Carousel
from kivy.uix.tabbedpanel import TabbedPanel
from kivy.uix.tabbedpanel import TabbedPanelHeader
from kivy.core.window import Window
fixedSize = (Window.size[1] * 0.66*1, Window.size[1]*1)
class MyApp(App):

    def build(self):
        # Set minimum window size for desktop and mobile
        Window.minimum_width = fixedSize[0]
        Window.minimum_height = fixedSize[1]
        Window.size = fixedSize

        # returns a window object with all its widgets
        self.window = BoxLayout(orientation='vertical')
        self.window.cols = 1
        self.window.size_hint = (None, None)  # Disable automatic size_hint
        self.window.width = fixedSize[0]  # Set an initial width
        self.window.height = fixedSize[1]  # Set an initial height
        self.window.pos_hint = {"center_x": 0.5, "center_y": 0.5}

        # Anchor Layout widget at top of window
        self.anchorLayout = AnchorLayout(
            anchor_x='center', anchor_y='top', size_hint=(1, 0.2))
        self.anchbtn1 = Button(text='Profile')
        self.anchorLayout.add_widget(self.anchbtn1)
        self.window.add_widget(self.anchorLayout)

        # BoxLayout widget for central buttons
        self.layout = BoxLayout(orientation='horizontal', size=(2, 1))
        self.btn1 = Button(text='Find a Group')
        self.btn2 = Button(text='Learn a Game')
        self.btn3 = Button(text='Create a Group')
        self.layout.add_widget(self.btn1)
        self.layout.add_widget(self.btn2)
        self.layout.add_widget(self.btn3)
        self.window.add_widget(self.layout)

        # TabbedPanel widget for local events and my groups
        self.tabbed = TabbedPanel()
        self.window.add_widget(self.tabbed)
        # Carousel local events
        self.local_events = Carousel()
        self.event1 = Button(text='Local Event 1')
        self.event2 = Button(text='Local Event 2')
        self.event3 = Button(text='Local Event 3')
        self.event4 = Button(text='Local Event 4')
        self.local_events.add_widget(self.event1)
        self.local_events.add_widget(self.event2)
        self.local_events.add_widget(self.event3)
        self.local_events.add_widget(self.event4)
        self.tab1 = TabbedPanelHeader(text='Local Events')
        self.tab1.content = self.local_events
        self.tabbed.add_widget(self.tab1)
        self.tabbed.default_tab = self.tab1
        # Carousel my groups
        self.my_groups = Carousel()
        self.group1 = Button(text='Group 1')
        self.group2 = Button(text='Group 2')
        self.group3 = Button(text='Group 3')
        self.group4 = Button(text='Group 4')
        self.my_groups.add_widget(self.group1)
        self.my_groups.add_widget(self.group2)
        self.my_groups.add_widget(self.group3)
        self.my_groups.add_widget(self.group4)
        self.tab2 = TabbedPanelHeader(text='My Groups')
        self.tab2.content = self.my_groups
        self.tabbed.add_widget(self.tab2)

        return self.window

    def callback(self, instance):
        # TODO
        print("callback called")

    def reSize(*args):
        # fixedSize = (Window.size[1] * 0.66, Window.size[1])
        Window.size = fixedSize
        return True

    Window.bind(on_resize=reSize)


app = FastAPI()
api_endpoints = APIEndpoints()
app.include_router(api_endpoints.router)


def start_program():
    uvicorn.run("main:app", port=8000, reload="True") # host="10.110.177.171",
    return 0


@app.get("/")
def home_page():
    return {"Message": "You Made"}


if __name__ == "__main__":
    MyApp().run()
    # start_program()
