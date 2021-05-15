from tkinter import *
from playsound import playsound
import os

cwd = os.getcwd() + "/"
result_number = 0
num_str = ""

sound_library = { #This dictionary holds the numbers and what songs they play
    "8675309" : r"Music\8675_309.mp3",
    "925" : r"Music\925.mp3",
    "3000" : r"Music\3000.mp3",
    "8" : r"Music\sk8rboi.mp3",
    "69" : r"Music\69.mp3",
    "420" : r"Music\420.mp3",
    "1158" : r"Music\1158.mp3",
    "2001" : r"Music\2001.mp3",
    "5" : r"Music\5.mp3",
    "9" : r"Music/9.mp3",
    "1" : r"Music/1.mp3",
    "182" : r"Music/182.mp3",
    "23" : r"Music/23.mp3",
    "41" : r"Music/41.mp3",
    }

def NumberKey (number):
    global num_str
    num_str = num_str + str(number)
    output_display.set(num_str)

def DecimalKey(): 
    global num_str
    num_str = num_str + "."
    output_display.set(num_str)
def EqualsKey():
    global num_str
    try:
        num_str = str(eval(num_str))
        output_display.set(num_str)
        
    except ZeroDivisionError:
        ClearKey()
        output_display.set("You cant divide by 0")
    except Exception:
        ClearKey()
        output_display.set("ERROR")
    GetSound()
def FunctionKey(type):
    global num_str
    num_str = num_str + str(type)
    output_display.set(num_str)
def ClearKey():
    global num_str
    num_str = ""
    output_display.set(num_str)

def GetSound():
    global num_str
    print("playsound(" + 'r"' + cwd + sound_library[num_str] + '"' + ")") #For debug, can remove later
    try:
        eval("playsound(" + 'r"' + cwd + sound_library[num_str] + '"' + ")") #If for some reason the app cant find the song mp3's you can give it the path by altering this.
        
    except Exception:
        var = 1

def ChangeTheme():
    print("SDAFSDAFSDAFSDF")

#GUI 
root = Tk()
root.title("WIP MUSIC CALC")
root.geometry("150x200")

current_theme = StringVar()
current_theme.set("Light") #Default theme
theme_menu = OptionMenu(root, current_theme, "Light", "Dark")
theme_menu.grid(row=1, column=4,columnspan=2)

output_display = StringVar()
output_display_label = Label(root, textvariable=output_display)
output_display_label.grid(row=0, column=0, columnspan=50, sticky = W)


seven_key = Button(root, text="7", command= lambda: NumberKey(7))
seven_key.grid(row=1, column=0)
eight_key = Button(root, text="8", command= lambda: NumberKey(8))
eight_key.grid(row=1, column=1)
nine_key = Button(root, text="9", command= lambda: NumberKey(9))
nine_key.grid(row=1, column=2)
four_key = Button(root, text="4", command= lambda: NumberKey(4))
four_key.grid(row=2, column=0)
five_key = Button(root, text="5", command= lambda: NumberKey(5))
five_key.grid(row=2, column=1)
six_key = Button(root, text="6", command= lambda: NumberKey(6))
six_key.grid(row=2, column=2)
one_key = Button(root, text="1", command= lambda: NumberKey(1))
one_key.grid(row=3, column=0)
two_key = Button(root, text="2", command= lambda: NumberKey(2))
two_key.grid(row=3, column=1)
three_key = Button(root, text="3", command= lambda: NumberKey(3))
three_key.grid(row=3, column=2)

zero_key = Button(root, text="0", command= lambda: NumberKey(0))
zero_key.grid(row=4, column=0)
decimal_key = Button(root, text=".", command=DecimalKey)
decimal_key.grid(row=4, column=1)
equals_key = Button(root, text="=", command=EqualsKey)
equals_key.grid(row=4, column=2)

division_key = Button(root, text="/", command= lambda: FunctionKey("/"))
division_key.grid(row=1, column=3)
multiplication_key = Button(root, text="*", command= lambda: FunctionKey("*"))
multiplication_key.grid(row=2, column=3)
subtraction_key = Button(root, text="-", command= lambda: FunctionKey("-"))
subtraction_key.grid(row=3, column=3)
addition_key = Button(root, text="+", command= lambda: FunctionKey("+"))
addition_key.grid(row=4, column=3)

clear_key = Button(root, text="Clear", command=ClearKey)
clear_key.grid(row=5, column=0,columnspan=3)

output_display.set("TEST") #debug

root.mainloop()