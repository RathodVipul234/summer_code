import tkinter
from tkinter import messagebox
from tkinter import *

window = tkinter.Tk()
window.title("Calculator")
e = tkinter.Entry(window, text="", width=25,font=('arial',18) ,borderwidth=5)
e.grid(row=0, column=0, columnspan=10, padx=10, pady=10)
def button_click(n):
    current = e.get()
    e.delete(0, END)
    e.insert(0, str(current) + str(n))

def button_clear():
    e.delete(0, END)

def button_dot():
    e.insert(END)

def button_backspace():
        length = len(e.get())
        e.delete(length-1,END)

def button_equ():
    Expression = re.fullmatch(r'^[0-9]+|[.]?([-+*/%]?[0-9]+|[.]?)+$',e.get())
    if Expression:
        divide_Ziro = Expression.group().split("/0")
        divide_Ziro_length = len(divide_Ziro)
        if divide_Ziro_length > 1:
            messagebox.showerror("error", "Can't Divide By Zero")
        else:
            Result = eval(Expression.group())
            print(Expression)
            print(Expression.group())
            type(Expression.group())
            e.delete(0,END)
            e.insert(0, Expression.group() + " =")
            e.insert(END, Result)
    else:
        messagebox.showerror("error", "Invalid Expression")

def button_plus(n):
    e.insert(END,n)

def button_minus(n):
    e.insert(END,n)

def button_divide(n):
    e.insert(END,n)

def button_multiplication(n):
    e.insert(END,n)

def button_modulo(n):
    e.insert(END,n)

Button_clear = tkinter.Button(window, text="CE", bg="black", fg="White", padx=14,pady=6,bd=8,font=("Arial",16,"bold"), command=button_clear)
Button_backspace = tkinter.Button(window, text="C", bg="black", fg="White", padx=20,pady=6,bd=8,font=("Arial",16,"bold"), command=button_backspace)
Button_equ = tkinter.Button(window, text="=", bg="green", fg="White",padx=20,pady=3,bd=8,font=("Arial",18,"bold"), command= button_equ)
Button_plus = tkinter.Button(window, text="+",  bg="orange", fg="black",padx=16,pady=3,bd=8,font=("Arial",18,"bold"), command=lambda: button_plus("+"))

Button_7 = tkinter.Button(window, text="7", bg="Red", fg="White", padx=16,pady=8,bd=8,font=("Arial",22,"bold"), command=lambda: button_click(7))
Button_8 = tkinter.Button(window, text="8", bg="Red", fg="White", padx=16,pady=8,bd=8,font=("Arial",22,"bold"), command=lambda: button_click(8))
Button_9 = tkinter.Button(window, text="9", bg="Red", fg="White", padx=16,pady=8,bd=8,font=("Arial",22,"bold"), command=lambda: button_click(9))
Button_minus = tkinter.Button(window, text="-",  bg="orange", fg="black",padx=16,pady=8,bd=8,font=("Arial",22,"bold"), command=lambda: button_minus("-"))


Button_4 = tkinter.Button(window, text="4",  bg="Red", fg="White",padx=16,pady=8,bd=8,font=("Arial",22,"bold"), command=lambda: button_click(4))
Button_5 = tkinter.Button(window, text="5",  bg="Red", fg="White",padx=16,pady=8,bd=8,font=("Arial",22,"bold"), command=lambda: button_click(5))
Button_6 = tkinter.Button(window, text="6",  bg="Red", fg="White",padx=16,pady=8,bd=8,font=("Arial",22,"bold"), command=lambda: button_click(6))
Button_multiplication = tkinter.Button(window, bg="orange", fg="black",text="*", padx=16,pady=8,bd=8,font=("Arial",22,"bold"),  command=lambda: button_multiplication("*"))

Button_1 = tkinter.Button(window, text="1", bg="Red", fg="White",padx=16,pady=8,bd=8,font=("Arial",22,"bold"), command=lambda: button_click(1))
Button_2 = tkinter.Button(window, text="2", bg="Red", fg="White",padx=16,pady=8,bd=8,font=("Arial",22,"bold"), command=lambda: button_click(2))
Button_3 = tkinter.Button(window, text="3", bg="Red", fg="White",padx=16,pady=8,bd=8,font=("Arial",22,"bold"), command=lambda: button_click(3))
Button_divide = tkinter.Button(window, text="/", bg="orange", fg="black", padx=17,pady=8,bd=8,font=("Arial",22,"bold"), command=lambda: button_divide("/"))

Button_0 = tkinter.Button(window, text="0",  bg="Red", fg="White",padx=16,pady=5,bd=8,font=("Arial",20,"bold"), command=lambda: button_click(0))
Button_00 = tkinter.Button(window, text="00",  bg="Red", fg="White",padx=14,pady=8,bd=8,font=("Arial",18,"bold"), command=lambda: button_click("00"))
Button_dot = tkinter.Button(window, text=".",  bg="Red", fg="White",padx=16,pady=3,bd=8,font=("Arial",23,"bold"), command=lambda: button_click("."))
Button_modulo = tkinter.Button(window, text="%",  bg="orange", fg="black",padx=14,pady=8,bd=8,font=("Arial",18,"bold"), command=lambda: button_modulo("%"))


# Show Button
Button_clear.grid(row=1, column=1)
Button_backspace.grid(row=1, column=2)
Button_equ.grid(row=1, column=3)
Button_plus.grid(row=1, column=4)

Button_1.grid(row=4, column=1)
Button_2.grid(row=4, column=2)
Button_3.grid(row=4, column=3)
Button_divide.grid(row=4, column=4)

Button_4.grid(row=3, column=1)
Button_5.grid(row=3, column=2)
Button_6.grid(row=3, column=3)
Button_multiplication.grid(row=3, column=4)

Button_7.grid(row=2, column=1)
Button_8.grid(row=2, column=2)
Button_9.grid(row=2, column=3)
Button_minus.grid(row=2, column=4)


Button_0.grid(row=5, column=1)
Button_dot.grid(row=5, column=3)
Button_00.grid(row=5, column=2)
Button_modulo.grid(row=5, column=4)

tkinter.mainloop()
