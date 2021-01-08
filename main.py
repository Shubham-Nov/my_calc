import tkinter
from tkinter import *
from tkinter import  messagebox


val = ""                        #FOR STORING LABEL VALUES
A = 0
operator = ""

"""
FOR DISPLAYING TEXT ON LABEL
"""

def btn_1_isclicked():
        global val
        val = val + "1"
        data.set(val)

def btn_2_isclicked():
        global val
        val = val + "2"
        data.set(val)

def btn_3_isclicked():
        global val
        val = val + "3"
        data.set(val)

def btn_4_isclicked():
        global val
        val = val + "4"
        data.set(val)

def btn_5_isclicked():
        global val
        val = val + "5"
        data.set(val)

def btn_6_isclicked():
        global val
        val = val + "6"
        data.set(val)

def btn_7_isclicked():
        global val
        val = val + "7"
        data.set(val)

def btn_8_isclicked():
        global val
        val = val + "8"
        data.set(val)

def btn_9_isclicked():
        global val
        val = val + "9"
        data.set(val)

def btn_0_isclicked():
        global val
        val = val + "0"
        data.set(val)

def btn_plus_clicked():
        global A
        global operator
        global val
        A = int(val)
        operator = "+"
        val = val + "+"
        data.set(val)

def btn_minus_clicked():
        global A
        global operator
        global val
        A = int(val)
        operator = "-"
        val = val + "-"
        data.set(val)

def btn_mul_clicked():
        global A
        global operator
        global val
        A = int(val)
        operator = "*"
        val = val + "*"
        data.set(val)

def btn_divide_clicked():
        global A
        global operator
        global val
        A = int(val)
        operator = "/"
        val = val + "/"
        data.set(val)

def c_pressed():
        global A
        global operator
        global val
        val = ""
        A = 0
        operator = ""
        data.set(val)

def result():
        global A
        global operator
        global val
        val2 = val
        if operator == "+":
                x = int((val2.split("+")[1]))
                C = A + x
                data.set(C)
                val = str(C)
        elif operator == "-":
                x = int((val2.split("-")[1]))
                C = A - x
                data.set(C)
                val = str(C)
        elif operator == "*":
                x = int((val2.split("*")[1]))
                C = A * x
                data.set(C)
                val = str(C)
        elif operator == "/":
                x = int((val2.split("/")[1]))
                if x == 0:
                        messagebox.showerror("Error","Division by 0 not supported")
                        A = ""
                        val = ""
                        data.set(val)
                else:
                        C = int(A / x)
                        data.set(C)
                        val = str(C)

root = tkinter.Tk()

root.geometry("250x400+300+300")                    #for size the main (root)

root.resizable(0, 0)                    #to enable/disable maximize

root.title("Calculator")

data = StringVar()
lbl = Label(                    #for main frame of root 
        root,
        text = "Label",
        anchor = SE,
        font = ("Verdana", 20),
        bg="white",
        textvariable = data,
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
        command = btn_1_isclicked,
        )
btn1.pack(side= LEFT, expand=True, fill = "both",)

btn2 = Button(
        btnrow1,
        text = "2",
        font = ("Verdana", 22),
        relief = GROOVE,
        border = 0,
        command = btn_2_isclicked,
        )
btn2.pack(side= LEFT, expand=True, fill = "both",)



btn3 = Button(
        btnrow1,
        text = "3",
        font = ("Verdana", 22),
        relief = GROOVE,
        border = 0,
        command = btn_3_isclicked,
        )
btn3.pack(side= LEFT, expand=True, fill = "both",)


btnplus = Button(
        btnrow1,
        text = "+",
        font = ("Verdana", 22),
        relief = GROOVE,
        border = 0,
        command = btn_plus_clicked,
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
        command = btn_4_isclicked,
        )
btn4.pack(side= LEFT, expand=True, fill = "both",)

btn5 = Button(
        btnrow2,
        text = "5",
        font = ("Verdana", 22),
        relief = GROOVE,
        border = 0,
        command = btn_5_isclicked,
        )
btn5.pack(side= LEFT, expand=True, fill = "both",)

btn6 = Button(
        btnrow2,
        text = "6",
        font = ("Verdana", 22),
        relief = GROOVE,
        border = 0,
        command = btn_6_isclicked,
        )
btn6.pack(side= LEFT, expand=True, fill = "both",)

btnminus = Button(
        btnrow2,
        text = "-",
        font = ("Verdana", 22),
        relief = GROOVE,
        border = 0,
        command = btn_minus_clicked,
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
        command = btn_7_isclicked,
        )
btn7.pack(side= LEFT, expand=True, fill = "both",)

btn8 = Button(
        btnrow3,
        text = "8",
        font = ("Verdana", 22),
        relief = GROOVE,
        border = 0,
        command = btn_8_isclicked,
        )
btn8.pack(side= LEFT, expand=True, fill = "both",)



btn9 = Button(
        btnrow3,
        text = "9",
        font = ("Verdana", 22),
        relief = GROOVE,
        border = 0,
        command = btn_9_isclicked,
        )
btn9.pack(side= LEFT, expand=True, fill = "both",)


btnmul = Button(
        btnrow3,
        text = "*",
        font = ("Verdana", 22),
        relief = GROOVE,
        border = 0,
        command = btn_mul_clicked,
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
        command = c_pressed,
        )
btn_clear.pack(side= LEFT, expand=True, fill = "both",)

btn_zero = Button(
        btnrow4,
        text = "0",
        font = ("Verdana", 22),
        relief = GROOVE,
        border = 0,
        command = btn_0_isclicked,
        )
btn_zero.pack(side= LEFT, expand=True, fill = "both",)


btn_equal = Button(
        btnrow4,
        text = "=",
        font = ("Verdana", 22),
        relief = GROOVE,
        border = 0,
        command = result,
        )
btn_equal.pack(side= LEFT, expand=True, fill = "both",)


btn_divide = Button(
        btnrow4,
        text = "/",
        font = ("Verdana", 22),
        relief = GROOVE,
        border = 0,
        command = btn_divide_clicked,
        )
btn_divide.pack(side= LEFT, expand=True, fill = "both",)

"""
        FRAMES BUTTON END

"""
root.mainloop()
