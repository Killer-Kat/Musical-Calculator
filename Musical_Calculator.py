from tkinter import *


result_number = 0
num_str = ""
has_decimal = False

def NumberKey (number):
    global num_str
    num_str = num_str + str(number)
    output_display.set(num_str)

def DecimalKey():
    global has_decimal, num_str
    #if has_decimal == False:
     #   has_decimal = True
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
def FunctionKey(type):
    global num_str
    num_str = num_str + str(type)
    output_display.set(num_str)
def ClearKey():
    global num_str
    num_str = ""
    output_display.set(num_str)

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