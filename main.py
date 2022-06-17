#computer ver 1.1 - demo
from cgitb import reset
from ctypes import alignment
from tkinter import *
from random import *

root = Tk()
root.title("I'm bored")
root.geometry("850x1000")

label = Label(text="Hello")
label.pack()
label2 = Label(text=" ")
label2.pack()

clicked = 0
    #main bored
def bored():
    global clicked
    clicked += 1
    bttn.config(text="And you are still bored? Bruh...")
    bttn.place(x=500, y=650)
    label.config(text=f"U r bored x {clicked}")
    label.pack()
    if clicked == 20:
        label2.config(text="Umm...okay")
    if clicked == 60:
        label2.config(text="b_b bro, u ok?")
        label2.pack()
    if clicked == 69:
        label2.config(text="Nothing there, you dumb h-")
    label2.pack()
    if clicked == 80:
        label2.config(text="Broo! Stop!", foreground="Dark Red")
        label2.pack()
    if clicked == 100:
        label2.config(text="THATS ENOUGH", foreground="Red")
        label2.pack()
    if clicked == 150:
        label2.config(text=". . .", foreground="Dark Violet")
    if clicked == 200:
        label2.config(text="I'm really worried about your mental health.", foreground="Dark Blue")
        label2.pack()
    if clicked == 222:
        label2.config(text="Yes, that's the sign from God, to stop")
        label2.pack()
    if clicked == 230:
        label2.config(text="Are you atheist or something?\n Well...")
        label2.pack()
    if clicked == 250:
        label2.config(text="You sure,\n that you're just bored? \n I know a good therapist...")
        label2.pack()
        bttn.config(text="J-just click...", activebackground="Pink")
        bttn.pack()
    if clicked == 300 or clicked == 500:
        label2.config(text=";__;")
        label2.pack()
        bttn.config(text="o__o")
        bttn.pack()
    if clicked == 333:
        label2.config(text="Next sign, just for sure", foreground="Orange")
        label2.pack()
    if clicked == 360:
        label2.config(text="That's the end \n and begin of the circle story.", foreground="Dark Brown")
        label2.pack()
    if clicked == 400:
        label2.config(text="Damn. Are you still here?", foreground="Blue")
        label2.pack()
    if clicked == 404:
        label2.config(text="You funny, funny. \n Error boom.", foreground="Red")
        label2.pack()
    if clicked == 420:
        label2.config(text="No. No. I am not green. \n Never.", foreground="Green")
        label2.pack()
        bttn.config(text="U-um.", bg="Orange", activebackground="Pink")
        bttn.pack()
    if clicked == 440:
        label2.config(text="Are you a robot or something?\n Why are you still here?", foreground="Black")
        label2.pack()
    if clicked == 460:
        label2.config(text="I am tireeeedddddd... \nWhat about you?", foreground="Violet")
        label2.pack()
        bttn.config(text="X D", bg="Light blue", activebackground="Blue")
        bttn.pack()
    if clicked == 520:
        label2.config(text="911? Um... yes. \n I think this player needs profesional help. \n Yes, yes. \nThanks.", foreground="Red")
        label2.pack()
        bttn.config(text="Idk")
        bttn.pack()
    if clicked == 545:
        label2.config(text="Oh. Didn't they send help? Well...", foreground="Black")
        label2.pack()
    if clicked == 570:
        label2.config(text="HOW?! \n HOW ARE YOU STILL HERE? \n HOW AND WHY?!", foreground="Red")
        label2.pack()
        bttn.config(text=":)")
        bttn.pack()
    if clicked == 600:
        label2.config(text="xd why? \n Why are you still here?", foreground="Dark Grey")
        label2.pack()
    if clicked == 620:
        label2.config(text="I hope you're okay.", foreground="Dark Grey")
        label2.pack()
    if clicked == 640:
        label2.config(text=". . .", foreground="Violet")
        label2.pack()
    if clicked == 669 or clicked == 690 or clicked == 699 or clicked == 969:
        label2.config(text="I'm not sure if you are +18, so... \n nothing here")
        label2.pack()
    if clicked == 700:
        label2.config(text="Umm....?", foreground="Black")
        label2.pack()
    if clicked == 720:
        label2.config(text="I am done.")
        label2.pack()

cclicks = 0

    #colors change
def color_bttn():
    global cclicks
    cclicks += 1
    kol = ["Green", "Red", "Blue", "Dark Blue", "Pink", "Violet", "Light Grey", "Grey", "Orange", "Light Blue"]
    root.config(bg=choice(kol))
    label.config(bg=choice(kol))
    label.pack()
    label2.config(bg=choice(kol), text=f"You just changed backgrounds' color! x {cclicks}")
    label2.pack()
    if cclicks == 20:
        label2.config(text="Oh? Party? Now?\n YAY!!!")
    if cclicks == 30:
        label2.config(text="Epilepsy warning..?")
    if cclicks == 45:
        label2.config(text="Ouch... My eyes...\n too much colors changes for me!")
    if cclicks == 60:
        label2.config(text=". . .")
    if cclicks == 69 or cclicks == 169 or cclicks == 269 or cclicks == 369:
        label2.config(text="If you have hope for something dumb...\n No.\n Are you more than 18yo? ;-;")
    if cclicks == 80:
        label2.config(text="Like... why?\n you good?")
    if cclicks == 100:
        label2.config(text="Oh, man-")   

def reset_all():
    global cclicks, clicked
    cclicks = 0
    clicked = 0
    label.config(text="Hello!", bg="Light Grey")
    label2.config(text="Just reseted!", bg="Light Grey")
    root.config(bg="Light Grey")
    return()


    #actions
bttn = Button(text="Click me, if you're bored", activebackground="Light Blue", command=bored)
bttn.place(x=495, y=650)

c_bttn = Button(command=color_bttn, text="If you are THAT bored, you can change color of background.")
c_bttn.place(x=20, y=650)

r_bttn = Button(text="Reset all", command=reset_all)
r_bttn.place(x=750, y=650)


root.mainloop() 