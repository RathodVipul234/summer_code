from tkinter import *
from tkinter import messagebox
import tkinter

window =tkinter.Tk()

label = Label( window, text="Player 1:(O)", font='Times 15 bold', bg='white', fg='black', height=1, width=9)
label.grid(row=0, column=0)
Player1 = tkinter.Entry(window,text="Player 1")
Player1.grid(row=0,column=1)

labe2 = Label( window, text="Player 2:(X)", font='Times 15 bold', bg='white', fg='black', height=1, width=9)
labe2.grid(row=1, column=0)
Player2 = tkinter.Entry(window,text="Player 2")
Player2.grid(row=1,column=1)
def reset():
    global  btnclick
    button1.configure(state=NORMAL)
    button2.configure(state=NORMAL)
    button3.configure(state=NORMAL)
    button4.configure(state=NORMAL)
    button5.configure(state=NORMAL)
    button6.configure(state=NORMAL)
    button7.configure(state=NORMAL)
    button8.configure(state=NORMAL)
    button9.configure(state=NORMAL)
    button1["text"] = " "
    button2["text"] = " "
    button3["text"] = " "
    button4["text"] = " "
    button5["text"] = " "
    button6["text"] = " "
    button7["text"] = " "
    button8["text"] = " "
    button9["text"] = " "
reset = Button(window,text="RESET",width=10,height=2,bg="lightgray",fg="black",font=("Arial",10,"bold"),command = reset)
reset.grid(row=1,column=2)

def disableButton():
    button1.configure(state=DISABLED)
    button2.configure(state=DISABLED)
    button3.configure(state=DISABLED)
    button4.configure(state=DISABLED)
    button5.configure(state=DISABLED)
    button6.configure(state=DISABLED)
    button7.configure(state=DISABLED)
    button8.configure(state=DISABLED)
    button9.configure(state=DISABLED)

btnclick = True
def btnClick(Buttons):
    global btnclick
    if Buttons["text"] == " " and btnclick == True:
        Buttons["text"] = "X"
        btnclick = False
        checkForWin()
    elif Buttons["text"] == " " and btnclick == False:
        Buttons["text"] = "O"
        btnclick = True
        checkForWin()
    else:
        tkinter.messagebox.showinfo("Tic-Tac-Toe", "Button already Clicked!")

def checkForWin():
    if (button1['text'] == 'X' and button2['text'] == 'X' and button3['text'] == 'X' or
        button4['text'] == 'X' and button5['text'] == 'X' and button6['text'] == 'X' or
        button7['text'] =='X' and button8['text'] == 'X' and button9['text'] == 'X' or
        button1['text'] == 'X' and button5['text'] == 'X' and button9['text'] == 'X' or
        button3['text'] == 'X' and button5['text'] == 'X' and button7['text'] == 'X' or
        button1['text'] == 'X' and button4['text'] == 'X' and button7['text'] == 'X' or
        button2['text'] == 'X' and button5['text'] == 'X' and button8['text'] == 'X' or
        button7['text'] == 'X' and button6['text'] == 'X' and button9['text'] == 'X'):
        disableButton()
        p1 = Player1.get() +" Win"
        tkinter.messagebox.showinfo("Tic-Tac-Toe",p1)

    elif (button1['text'] == 'O' and button2['text'] == 'O' and button3['text'] == 'O' or
          button4 ['text'] == 'O' and button5 ['text'] == 'O' and button6 ['text'] == 'O' or
          button7 ['text'] == 'O' and button8 ['text'] == 'O' and button9 ['text'] == 'O' or
          button1 ['text'] == 'O' and button5 ['text'] == 'O' and button9 ['text'] == 'O' or
          button3 ['text'] == 'O' and button5 ['text'] == 'O' and button7 ['text'] == 'O' or
          button1 ['text'] == 'O' and button4 ['text'] == 'O' and button7 ['text'] == 'O' or
          button2 ['text'] == 'O' and button5 ['text'] == 'O' and button8 ['text'] == 'O' or
          button7 ['text'] == 'O' and button6 ['text'] == 'O' and button9 ['text'] == 'O'):
          disableButton()
          p2 = Player2.get() + " Winn"
          tkinter.messagebox.showinfo("Tic-Tac-Toe",p2)
    elif (button1['text'] !=" " and button2['text'] !=" " and button3['text'] !=" " and button4['text'] !=" " and button5['text'] !=" " and button6['text'] !=" " and button7['text'] !=" " and button8['text'] !=" " and button9['text'] !=" " ):
        tkinter.messagebox.showinfo("Tic-Tac-Toe","Match Tied")
        disableButton()

button1 = Button(window, text=' ', font='Times 20 bold', bg='white', fg='black', height=4, width=8, command=lambda: btnClick(button1))
button1.grid(row=3,column=0)

button2 = Button(window, text=' ', font='Times 20 bold', bg='white', fg='black', height=4, width=8, command=lambda: btnClick(button2))
button2.grid(row=3, column=1)

button3 = Button(window, text=' ', font='Times 20 bold', bg='white', fg='black', height=4, width=8, command=lambda: btnClick(button3))
button3.grid(row=3, column=2)

button4 = Button(window, text=' ', font='Times 20 bold', bg='white', fg='black', height=4, width=8, command=lambda: btnClick(button4))
button4.grid(row=4, column=0)

button5 = Button(window, text=' ', font='Times 20 bold', bg='white', fg='black', height=4, width=8, command=lambda: btnClick(button5))
button5.grid(row=4, column=1)

button6 = Button(window, text=' ', font='Times 20 bold', bg='white', fg='black', height=4, width=8, command=lambda: btnClick(button6))
button6.grid(row=4, column=2)

button7 = Button(window, text=' ', font='Times 20 bold', bg='white', fg='black', height=4, width=8, command=lambda: btnClick(button7))
button7.grid(row=5, column=0)

button8 = Button(window, text=' ', font='Times 20 bold', bg='white', fg='black', height=4, width=8, command=lambda: btnClick(button8))
button8.grid(row=5, column=1)

button9 = Button(window, text=' ', font='Times 20 bold', bg='white', fg='black', height=4, width=8, command=lambda: btnClick(button9))
button9.grid(row=5, column=2)

window.mainloop()