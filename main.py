import tkinter
from tkinter import *


root = tkinter.Tk()

root.geometry("250x400+300+300")                    #for size the main (root)

root.resizable(0, 0)                    #to enable/disable maximize

root.title("Calculator")


lbl = Label(                    #for main frame of root 
        root,
        text = "Label",
        anchor = SE,
        font = ("Verdana", 20),
        bg="white",
        )
lbl.pack(expand=True, fill = "both",)

"""

        FOR FRAMES

"""
btnrow1 = Frame(root)
btnrow1.pack(expand=True, fill="both",)

btnrow2 = Frame(root)
btnrow2.pack(expand= True, fill= "both",)

btnrow3 = Frame(root)
btnrow3.pack(expand= True, fill= "both",)

btnrow4 = Frame(root)
btnrow4.pack(expand= True, fill= "both",)

"""

        FOR FRAMES button

"""
"""

        ROW 1

"""
btn1 = Button(
        btnrow1,
        text = "1",
        font = ("Verdana", 22),
        relief = GROOVE,
        border = 0,
        )
btn1.pack(side= LEFT, expand=True, fill = "both",)

btn2 = Button(
        btnrow1,
        text = "2",
        font = ("Verdana", 22),
        relief = GROOVE,
        border = 0,
        )
btn2.pack(side= LEFT, expand=True, fill = "both",)



btn3 = Button(
        btnrow1,
        text = "3",
        font = ("Verdana", 22),
        relief = GROOVE,
        border = 0,
        )
btn3.pack(side= LEFT, expand=True, fill = "both",)


btnplus = Button(
        btnrow1,
        text = "+",
        font = ("Verdana", 22),
        relief = GROOVE,
        border = 0,
        )
btnplus.pack(side= LEFT, expand=True, fill = "both",)

"""

        ROW 2

"""
btn4 = Button(
        btnrow2,
        text = "4",
        font = ("Verdana", 22),
        relief = GROOVE,
        border = 0,
        )
btn4.pack(side= LEFT, expand=True, fill = "both",)

btn5 = Button(
        btnrow2,
        text = "5",
        font = ("Verdana", 22),
        relief = GROOVE,
        border = 0,
        )
btn5.pack(side= LEFT, expand=True, fill = "both",)



btn6 = Button(
        btnrow2,
        text = "6",
        font = ("Verdana", 22),
        relief = GROOVE,
        border = 0,   
        )
btn6.pack(side= LEFT, expand=True, fill = "both",)


btnminus = Button(
        btnrow2,
        text = "-",
        font = ("Verdana", 22),
        relief = GROOVE,
        border = 0,
        )
btnminus.pack(side= LEFT, expand=True, fill = "both",)

"""

        ROW 3

"""
btn7 = Button(
        btnrow3,
        text = "7",
        font = ("Verdana", 22),
        relief = GROOVE,
        border = 0,
        )
btn7.pack(side= LEFT, expand=True, fill = "both",)

btn8 = Button(
        btnrow3,
        text = "8",
        font = ("Verdana", 22),
        relief = GROOVE,
        border = 0,
        )
btn8.pack(side= LEFT, expand=True, fill = "both",)



btn9 = Button(
        btnrow3,
        text = "9",
        font = ("Verdana", 22),
        relief = GROOVE,
        border = 0,
        )
btn9.pack(side= LEFT, expand=True, fill = "both",)


btnmul = Button(
        btnrow3,
        text = "*",
        font = ("Verdana", 22),
        relief = GROOVE,
        border = 0,
        )
btnmul.pack(side= LEFT, expand=True, fill = "both",)

"""
        ROW 4

"""
btn_clear = Button(
        btnrow4,
        text = "C",
        font = ("Verdana", 22),
        relief = GROOVE,
        border = 0,
        )
btn_clear.pack(side= LEFT, expand=True, fill = "both",)

btn_zero = Button(
        btnrow4,
        text = "0",
        font = ("Verdana", 22),
        relief = GROOVE,
        border = 0,
        )
btn_zero.pack(side= LEFT, expand=True, fill = "both",)


btn_equal = Button(
        btnrow4,
        text = "=",
        font = ("Verdana", 22),
        relief = GROOVE,
        border = 0,
        )
btn_equal.pack(side= LEFT, expand=True, fill = "both",)


btn_divide = Button(
        btnrow4,
        text = "/",
        font = ("Verdana", 22),
        relief = GROOVE,
        border = 0,
        )
btn_divide.pack(side= LEFT, expand=True, fill = "both",)

"""
        FRAMES BUTTON END

"""
root.mainloop()
