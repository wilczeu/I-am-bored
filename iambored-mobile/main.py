#i am bored - mobile 1.2
#from typing_extensions import Self
from kivy import *
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.widget import Widget
from kivy.uix.gridlayout import GridLayout
from kivy.uix.anchorlayout import AnchorLayout
import colorsys
from kivy.uix.relativelayout import RelativeLayout
from kivy.uix.floatlayout import FloatLayout


class MyGrid(Widget):
    pass

class Bored(App):
    def build(self):
        return MyGrid()

if __name__ == "__main__":
    Bored().run()    