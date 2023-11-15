from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen, SlideTransition, NoTransition
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.core.window import Window


# Static method that transitions between screens with no transition animation
def transition_to_screen(self, screen_name):
    self.manager.transition = NoTransition()
    self.manager.current = screen_name


# Static method that transitions between screens with a slide transition given a direction
def slide_transition_to_screen(self, screen_name, transition_direction):
    self.manager.transition = SlideTransition()
    if transition_direction != "right" and transition_direction != "left":
        transition_direction = "left"
    self.manager.transition.direction = transition_direction
    self.manager.current = screen_name


# Transition types:
# NoTransition - switches screens instantly with no animation
# SlideTransition - slide the screen in/out, from any direction
# CardTransition - new screen slides on the previous or the old one slides off the new one depending on the mode
# SwapTransition - implementation of the iOS swap transition
# FadeTransition - shader to fade the screen in/out
# WipeTransition - shader to wipe the screens from right to left
# FallOutTransition - shader where the old screen ‘falls’ and becomes transparent, revealing the new one behind it.
# RiseInTransition - shader where the new screen rises from the screen centre while fading from transparent to opaque.
