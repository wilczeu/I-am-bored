#i am bored - mobile 1.4
#from typing_extensions import Self
import random
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
        self.ids.L2.text = " "
        self.B01.bind(on_press=self.bored_bttn)
        global clicks
        clicks += 1
        self.ids.L1.text = f"U r bored x {clicks}"

        if clicks == 20:
            self.ids.L2.text = "Um... Okay"
        
        if clicks == 60:
            self.ids.L2.text = "b_b bro, u ok?"
            self.ids.L2.color = "blue"
        
        if clicks == 69 or clicks == 169 or clicks == 269 or clicks == 369 or clicks == 669 or clicks == 696:
            self.ids.L2.text = "Nothing there. ;-;"
            self.ids.L2.color = "pink"
            self.ids.B01.text = "( ͠° ͟ʖ ͡°) no."

        if clicks == 80:
            self.ids.L2.text = "Broo! Stop!"
            self.ids.L2.color = "red"
        
        if clicks == 100:
            self.ids.L2.text = "THAT'S ENOUGH!"
            self.ids.L2.color = "red"
        
        if clicks == 150 or clicks == 640:
            self.ids.L2.text = ". . ."
            self.ids.L2.color = "violet"
        
        if clicks == 200:
            self.ids.L2.text = "I'm really worried about your mental health."
            self.ids.L2.color = "dark blue"
        
        if clicks == 222:
            self.ids.L2.text = "Yes, that's the sign from God, to stop"
            self.ids.L2.color = "yellow"

        if clicks == 230 or clicks == 340:
            self.ids.L2.text = "Are you atheist or something?\n Well..."
            self.ids.L2.color = "orange"
        
        if clicks == 250:
            self.ids.L2.text = "You sure,\n that you're just bored? \n I know a good therapist..."
            self.ids.B01.text = "J-just click..."
            self.ids.L2.color = "pink"

        if clicks == 300 or clicks == 500:
            self.ids.L2.text = ";__;"

        if clicks == 333:
            self.ids.L2.text = "Next sign, just for sure"
            self.ids.L2.color = "orange"

        if clicks == 360:
            self.ids.L2.text = "That's the end \n and begin of the circle story."
            self.ids.B01.text = "o"
            self.ids.L2.color = "green"

        if clicks == 400:
            self.ids.L2.text = "Damn. Are you still here?"

        if clicks == 404:
            self.ids.L2.text = "You funny, funny. \n Error boom."
            self.ids.L2.color = "red"

        if clicks == 420:
            self.ids.L2.text = "No. No. I am not green. \n Never."
            self.ids.L2.color = "light green"

        if clicks == 440:
            self.ids.L2.text = "Are you a robot or something?\n Why are you still here?"
            self.ids.L2.color = "cyan"

        if clicks == 460:
            self.ids.L2.text = "I am tireeeedddddd... \nWhat about you?"
            self.ids.L2.color = "dark grey"

        if clicks == 520:
            self.ids.L2.text = "911? Um... yes. \n I think this player needs profesional help. \n Yes, yes. \nThanks."
            self.ids.L2.color = "red"

        if clicks == 545:
            self.ids.L2.text = "Oh. Didn't they send help? Well..."
            self.ids.L2.color = "blue"

        if clicks == 570:
            self.ids.L2.text = "HOW?! \n HOW ARE YOU STILL HERE? \n HOW AND WHY?!"
            self.ids.L2.color = "red"

        if clicks == 600:
            self.ids.L2.text = "xd why? \n Why are you still here?"
            self.ids.L2.color = "dark grey"

        if clicks == 620:
            self.ids.L2.text = "I hope you're okay."
            self.ids.L2.color = "light blue"

        if clicks == 700:
            self.ids.L2.text = "Umm....?"

        if clicks == 720:
            self.ids.L2.text = "I am done."

        if clicks == 2022:
            self.ids.L2.text = "Greetings from programist XD"

        t = [";-;", "I am starting to worry about you...", "U good?", "Hahan't", "Want you get therapist..?\n No? \n Okay...", "Bruh- o_o", "Idk what to say anymore-", "Too much caffeine?", "I was wondering...\n ... \n I've forgot, sorry", "Nevermind.", "You shouldn't spending so much time on phone.\n It's unhealthy.", "E-ekhm...", ":)", "Maybe go outside? \n No? \n Hm...", "Maybe you want to talk about this problem..?", "Ouch- \n(Don't worry, I don't know what i meant)", "Too much caffeine???", "Um... Having fun? \n \n Mnom mnom", "<3", "XD???", "If you'll clicking so much, you'll be the ProBored Person, haha\n better not.", "u w u", "Mnom, mnom\n \n If you're having fun", "Maybe just draw a dog and listen to music? \n I think it's better than this...", "Haha\n Idk but I want to be funny, LoL", "Wanna cookie?\n Me too"]

       
        if clicks != 20 and clicks !=60 and clicks !=69 and clicks != 80 and clicks != 100 and clicks != 150 and clicks != 169 and clicks != 269 and clicks != 369 and clicks != 669 and clicks!= 696 and clicks != 360 and clicks != 200 and clicks != 222 and clicks != 230 and clicks != 250 and clicks != 300 and clicks != 333 and clicks != 400 and clicks != 404 and clicks !=420 and clicks != 440 and clicks != 460 and clicks != 520 and clicks != 545 and clicks != 570 and clicks != 600 and clicks != 620 and clicks != 700 and clicks !=720 and clicks != 2022:
            self.ids.L2.text = random.choice(t)
            self.ids.L2.color = "black"
            

    pass

class Bored(App):
    def build(self):


        return MyGrid()
    

if __name__ == "__main__":
    Bored().run()    