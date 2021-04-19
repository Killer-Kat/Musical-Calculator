from tkinter import *
from playsound import playsound

result_number = 0
num_str = ""

sound_library = { #This dictionary holds the numbers and what songs they play
    "8675309" : r"Musical Calculator\Music\8675_309.mp3",
    "925" : r"Musical Calculator\Music\925.mp3",
    "3000" : r"Musical Calculator\Music\3000.mp3",
    "8" : r"Musical Calculator\Music\sk8rboi.mp3",
    "69" : r"Musical Calculator\Music\69.mp3",
    "420" : r"Musical Calculator\Music\420.mp3",
    "1158" : r"Musical Calculator\Music\1158.mp3",
    "2001" : r"Musical Calculator\Music\2001.mp3",
    "5" : r"Musical Calculator\Music\5.mp3",
    "9" : r"Musical Calculator/Music/9.mp3",
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
    try:
        eval("playsound(" + 'r"C:/Users/Goldkat/source/repos/' + sound_library[num_str] + '"' + ")") # Put your own path here
        print("playsound(r" + sound_library[num_str] + ")")
    except Exception:
        var = 1

#GUI 
root = Tk()
root.title("WIP MUSIC CALC")
root.geometry("100x200")

output_display = StringVar()
output_display_label = Label(root, textvariable=output_display)
output_display_label.grid(row=0, column=0, columnspan=50)


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

output_display.set("TEST")

root.mainloop()