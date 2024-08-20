from tkinter import*
import random

root = Tk()
root.geometry("360x330")
root.configure(background="teal")
root.title("Name Picker")
#### MODEL ####
list = []

def first_period():
    global list, class_selected
    list = ["Jane","Bennett","Hank","Huey","Donovan","Evan","Boone","Matt","Olivia","Cyrus","Xander","Charles","Nicholas","Joseph","Yuval","Theo","Priya"]
    clase.config(text="First Period")

def second_period():
    global list
    list = ["Seville","Abriel","Iggy","Lily","Nikolai","Sean","Henry","Landen","Jack","Everson","Elijah","Noam","Ian"]
    clase.config(text="Second Period")

def third_period():
    global list
    list = ["Nik","Soren","Max","Sam","Quinn","Julian","Lucas","Joshua","Ethan","Drew","Austin","Anthony","Matthew","William","Nicholas","Torin","Jake","Aidan","Dash","Wyatt","Josiah","Riley","Francisco","Miles","Sal","Ryan","Ray","Kristoff"]
    clase.config(text="Third Period")

def fifth_period():
    global list
    list = ["Alex A.","Jacob B.","Mitchell","Dawson","Frank","Tate","Joseph","Jonathan","Andrew","Ben","Nash","Alex P.","Jacob P.","Aaron","Annika","Quinn","Ava","Victor","Fletcher","Miles"]
    clase.config(text="Fifth Period")

def sixth_period():
    global list
    list = ["Blake Bernstein","Owen Boshart","Elijah Debusk","Caleb Deleon","Owen Fannin","Jordan Freeman","Edgar Garcia-Fajardo","Weston Gardner","Owen Harper","John Hortman","Gavin Kirsch","Madeline Lafollette","Anderson Marin Garcia","Roman Mengarelli","Toby Moffitt","Henry Morris","Christian Morrison","Nathan Nada","Tristan Papworth","Huy Quach","Khang Quach","Danielle Ramirez","Fatima Reyes Duran","Roman Salaz"]
    clase.config(text="Sixth Period")

def seventh_period():
    global list
    list = ["Will Achtermann","Irmoon Batbayar","Soren Benson","Max Brandt","Luke Brittain","Zachary Ciomperlik","Nathaniel Haven","Torin Lanza","Judah Leon","Aidan Makarabooshanam","Kristoff Micske","Iqra Nadeem","Jacques Noguess","Joshua Ortiz","Wyatt Paul","Miles Puthoff","Riley Ricca","Sal Tangaroa"]
    clase.config(text="Seventh Period")


def pick_student():
    global list
    if len(list)>0:
        student.config(text=list.pop(random.randint(0,len(list)-1)))
    else:
        student.config(text="Reset Class")
#### CONTROLLER ####"
title= Label(root,text="Name Picker", font=("Times New Roman",20), bg="teal").place(x=110, y=20, )

class_selected = Label(root,text="Selected class: ",font=("Times New Roman",15),bg="teal")
class_selected.place(x=20, y=200)

clase = Label(root,text="",font=("Times New Roman",20),bg="teal", fg ="white")
clase.place(x=150,y=195)

student_selected = Label(root,text="Selected student: ",font=("Times New Roman",15),bg="teal")
student_selected.place(x=20, y=260)

student = Label(root, text="", font=("Times New Roman",20),bg="teal",fg="white")
student.place(x=167,y=255)

second = Button(root, text="1st Period", command = first_period)
second.place(x=20,y=70,width=100, height=30)

third = Button(root, text="3rd Period",command = second_period)
third.place(x=130,y=70,width=100,height=30)

fourth = Button(root, text="4th Period", command = third_period)
fourth.place(x=240,y=70,width=100,height=30)

fifth = Button(root, text="5th Period", command = fifth_period)
fifth.place(x=20,y=110,width=100, height=30)

seventh = Button(root, text="6th Period", command = sixth_period)
seventh.place(x=130,y=110,width=100, height=30)

eigth = Button(root, text="8th Period", command = seventh_period)
eigth.place(x=240,y=110,width=100, height=30)

student_picker = Button(root, text="Randomly Select A Student", command = pick_student)
student_picker.place(x=20,y=150, width=320, height=30)

#### VIEW ####





root.mainloop()
