import tkinter
from tkinter import *
from tkinter import messagebox
windows =Tk()
windows.title("Weight Converion")


def final_result():
    global first_value
    try:
        first_value = float(input_entry.get())
    except ValueError:
        messagebox.showinfo("Error","Please Enter Only Number")


    # ["gram","kilogram","milligram","pound"]
    input_unit = variable_input.get()
    output_unit = variable_output.get()

    if input_unit == "gram":
        if output_unit == "gram":
            Answer = GramToAll.gmTogm(first_value)
            output_result.delete(0,END)
            output_result.insert(0,Answer)

        elif output_unit == "kilogram":
            Answer = GramToAll.gmTokg(first_value)
            output_result.delete(0,END)
            output_result.insert(0,Answer)

        elif output_unit == "milligram":
            Answer = GramToAll.gmTomili(first_value)
            output_result.delete(0 ,END)
            output_result.insert(0 ,Answer)

        elif output_unit == "pound":
            Answer = GramToAll.gmTopound(first_value)
            output_result.delete(0 ,END)
            output_result.insert(0 ,Answer)


    elif input_unit =="kilogram":
        if output_unit == "gram":
            Answer = KillogramToAll.kgTogm(first_value)
            output_result.delete(0,END)
            output_result.insert(0 ,Answer)

        elif output_unit == "kilogram":
            Answer = KillogramToAll.kgTokg(first_value)
            output_result.delete(0 ,END)
            output_result.insert(0 ,Answer)

        elif output_unit == "milligram":
            Answer = KillogramToAll.KgTomill(first_value)
            output_result.delete(0 ,END)
            output_result.insert(0 ,Answer)

        elif output_unit == "pound":
            Answer = KillogramToAll.kgTopound(first_value)
            output_result.delete(0 ,END)
            output_result.insert(0 ,Answer)


    elif input_unit == "milligram":
        if output_unit == "gram":
            Answer = MiligramToAll.miliTogm(first_value)
            output_result.delete(0,END)
            output_result.insert(0 ,Answer)

        elif output_unit == "kilogram":
            Answer = MiligramToAll.miliTokg(first_value)
            output_result.delete(0 ,END)
            output_result.insert(0 ,Answer)

        elif output_unit == "milligram":
            Answer = MiligramToAll.miliTomilli(first_value)
            output_result.delete(0 ,END)
            output_result.insert(0 ,Answer)

        elif output_unit == "pound":
            Answer = MiligramToAll.miliTopound(first_value)
            output_result.delete(0 ,END)
            output_result.insert(0 ,Answer)


    elif input_unit == "pound":
        if output_unit == "gram":
            Answer = PoundToAll.poundTogm(first_value)
            output_result.delete(0 ,END)
            output_result.insert(0 ,Answer)

        elif output_unit == "kilogram":
            Answer = PoundToAll.poundTokg(first_value)
            output_result.delete(0 ,END)
            output_result.insert(0 ,Answer)

        elif output_unit == "milligram":
            Answer = PoundToAll.poundTomili(first_value)
            output_result.delete(0 ,END)
            output_result.insert(0 ,Answer)

        elif output_unit == "pound":
            Answer = PoundToAll.poundTopound(first_value)
            output_result.delete(0 ,END)
            output_result.insert(0 ,Answer)


#Two Labels
Label1 = Label(windows,width=20,font='Times 15 bold',borderwidth = 5,relief="solid", bg='orange', fg='black',height=5)
Label1.grid(row= 0,column=1)

Label3 = Label(windows,font='Times 15 bold', bg='orange',borderwidth = 5,relief="solid", fg='black',width=20,height=5)
Label3.grid(row= 0,column=3)


#Button
output = Button(windows,text="=",font='Times 30 bold',bd=8, bg='Black',fg='red',command = final_result)
output.grid(row= 0,column=2)


#Input And Output Entry Boxes
input_entry = Entry(windows,borderwidth=5)
input_entry.config(font=("Arial",12,"bold"))
input_entry.place(x=50, y=80)
input_entry.bind("<Return>", (lambda event: final_result())) #This Is For Geting Result From Entry Box When You Click Enter

output_result = Entry(windows,borderwidth=5)
output_result.place(x=370, y=80)
output_result.config(font=("Arial",12,"bold"))


#Drop-Down Otion Input $ Output
OptionList_input = ["gram","kilogram","milligram","pound"]
variable_input = StringVar()
variable_input.set(OptionList_input[0])

OptionList_output = ["gram","kilogram","milligram","pound"]
variable_output = StringVar()
variable_output.set(OptionList_output[0])

#Create DropDown Menu
drop_down_input = OptionMenu(windows,variable_input,*OptionList_input)
drop_down_input.config(font=("Arial",20,"bold"),bd=5,bg="black",fg="white")
drop_down_input.place(x=50,y=10)

drop_down_output = OptionMenu(windows,variable_output,*OptionList_output)
drop_down_output.config(font=("Arial",20,"bold"),bd=5,bg="black",fg="white")
drop_down_output.place(x=370,y=10)

#All Mathamatics Function Wich You Want To perfor Task

class GramToAll:
    global first_value
    first_value = input_entry.get()
    def __init__(self,first_value):
        self.first_value = first_value

    def gmTogm(self):
        Answer =  first_value
        return Answer

    def gmTokg(self):
        Answer = first_value / 1000
        return Answer

    def gmTomili(self):
        Answer = first_value * 1000
        return Answer

    def gmTopound(self):
        Answer = first_value / 454
        return Answer

class KillogramToAll:
    def __init__(self ,first_value):
        self.first_value = first_value

    def kgTogm(self):
        Answer = first_value * 1000
        return Answer

    def kgTokg(self):
        Answer = first_value
        return Answer

    def KgTomill(self):
        Answer = first_value * 1000000
        return Answer

    def kgTopound(self):
        Answer = first_value *  2.205
        return Answer

class MiligramToAll:
    def __init__(self ,first_value):
        self.first_value = first_value

    def miliTogm(self):
        Answer = first_value / 1000
        return Answer

    def miliTokg(self):
        Answer = first_value / 1000000
        return Answer

    def miliTomilli(self):
        Answer = first_value
        return Answer

    def miliTopound(self):
        Answer = first_value / 453592
        return Answer

class PoundToAll:
    def __init__(self ,first_value):
        self.first_value = first_value

    def poundTogm(self):
        Answer = first_value * 454
        return Answer

    def poundTokg(self):
        Answer = first_value / 2.205
        return Answer

    def poundTomili(self):
        Answer = first_value * 453592
        return Answer

    def poundTopound(self):
        Answer = first_value
        return Answer

windows.mainloop()