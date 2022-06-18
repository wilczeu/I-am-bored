#i am bored - mobile 1.2
#from typing_extensions import Self
from kivy import *
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.widget import Widget

class gl(Widget):
    pass

class Bored(App):
    def build(self):
        return gl()

if __name__ == "__main__":
    Bored().run()
    