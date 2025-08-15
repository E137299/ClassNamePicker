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
    list = ["Miles","Luke","Elijah","Quinn","Emme","Jose","Maddie","AJ","Toby","Henry","Hutchins","Emmanuel","Dash"]
    clase.config(text="First Period")

def second_period():
    global list
    list = ["Genevieve B.","Adrian B.","Miles B.","Caleb C","Diego C.G.","Malko C.","Matthew C.","Cason D.","Fisher D.","Zyad E.","Farah F.G.","Luca F.","Harry G.","Virgil G.","Connor H.","Sarai I.","Katherine J.","Clark K.","Torin L.","Sabine L.","Arav M.","Caven M.","Miquel M.V.","Fabiola R.D.","Dexter R.","Noah S.","Vladyslav S.","Leslie S.","Christin T.","Eliza T.","Omar V."]
    clase.config(text="Second Period")

def fourth_period():
    global list
    list = []
    clase.config(text="Third Period")

def fifth_period():
    global list
    list = []
    clase.config(text="Fifth Period")

def sixth_period():
    global list
    list = []
    clase.config(text="Sixth Period")

def seventh_period():
    global list
    list = []
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

third = Button(root, text="2nd Period",command = second_period)
third.place(x=130,y=70,width=100,height=30)

fourth = Button(root, text="4th Period", command = fourth_period)
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
