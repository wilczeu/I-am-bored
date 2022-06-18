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

bttn = Button()

clicks = 0

class MyGrid(Widget):
    def bored_bttn(self):
        self.ids.B01.text = "And you're still bored..?"
        self.B01 = Button()
        self.ids.L2.text = "LoL"
        self.B01.bind(on_press=self.bored_bttn)
        global clicks
        clicks += 1
        self.ids.L1.text = f"U r bored x {clicks}"


    pass

class Bored(App):
    def build(self):


        return MyGrid()
    

if __name__ == "__main__":
    Bored().run()    