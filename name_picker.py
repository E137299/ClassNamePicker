from tkinter import*
import random

root = Tk()
root.geometry("360x330")
root.configure(background="teal")
root.title("Name Picker")
#### MODEL ####
list = []

def second_period():
    global list, class_selected
    list = ["Alejandro Valadez","AnnaMaria Parten","Lucian Minnigerode","Joshia Milewski","Gideon Head","Willie Chuter","Priya Wallace","Theo Volk","Henry Rabenberg","Nicholas Potoplyak","Matt Green","Donovan Fox","Huey Choo","Leo Camacho","Kai Brooks"]
    clase.config(text="Second Period")

def third_period():
    global list
    list = ["Fletcher Wilson","Victor Wattenbarger","Annika Singh","Ethan Shade-Shell","Aaron Sabisch","Jacob Patt","Alex Parsons","Dellorian Mrotek","Nikolai Lesak","Izzy Krieg","Jonathon Lampling","Connor Angelone","Jacob Baird","Lizzie Banda","Antonio Byrne","Em Chang","Dawson Dittmar","Aaron Fox","Blake Fyda","Sarah Garrison","Frank Hadlock","Thomas Keely"]
    clase.config(text="Third Period")

def fourth_period():
    global list
    list = ["Emily Alpuche","Kellen Brooks","Abriel Castro","Mitchell Crain","Elliot Day","Rafael Gangishetti","Iggy Gillion","Lily Gottlieb","Isah Graves","Devin McKinley","Andrew Moyseos","Ben Palmer","Rylan Parker","Quinn Skidmore","Jack Wagoner","Dash Wilcox","Miles Wyatt","Ian Zavalney","Lin Zaw"]
    clase.config(text="Fourth Period")

def fifth_period():
    global list
    list = ["Alex Antone","Nadia Benitez","Seville Bohn","Jonathan Brackin","Ford Campbell","Tate Hentrich","Emma Hernandez","Austin Hoffman","Joseph Jeong","Owen Joos","Jennifer Mendoza","Jesus Morales-Tudon","Megan O'Leary","Nash Parker","Marko Perez-Osorio","Eliud Pozos","Jesse Quezada","Landen Schipper","Jack Sharin","Everson Smith","Noam Stewart","Ava Taylor","Hunter Thompson"]
    clase.config(text="Fifth Period")

def seventh_period():
    global list
    list = ["Amaya Baker","Janie Barnard","Luke Bone","Hank Brown","Owen DeYoung","Jack Doherty","Matt Green","Isaac Guzman","Wren Heinley","Olivia Hollander","Cooper Scogin","James Scott","Will Simek","Sonia Spitz","Zach Bateman","Bennett Bond","Wyatt Ecton","Evan Gonin","Boone Goodgame","Maddie Greene","Xander Lecompte","Charles Mounce","Miles Nguyen","William Rosenbaum","Joseph Sondgeroth","Yuval Tsechansky"]
    clase.config(text="Seventh Period")

def eight_period():
    global list
    list = ["Tae Lee","Hudson Maebius","Elijah Smykla","Cooper Buch","Cooper Falk","Weston Hash","Alex Miranda","Annika Solotko","Ryan Vauk"]
    clase.config(text="Eight Period")


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

second = Button(root, text="2nd Period", command = second_period)
second.place(x=20,y=70,width=100, height=30)

third = Button(root, text="3rd Period",command = third_period)
third.place(x=130,y=70,width=100,height=30)

fourth = Button(root, text="4th Period", command = fourth_period)
fourth.place(x=240,y=70,width=100,height=30)

fifth = Button(root, text="5th Period", command = fifth_period)
fifth.place(x=20,y=110,width=100, height=30)

seventh = Button(root, text="7th Period", command = seventh_period)
seventh.place(x=130,y=110,width=100, height=30)

eigth = Button(root, text="8th Period", command = eight_period)
eigth.place(x=240,y=110,width=100, height=30)

student_picker = Button(root, text="Randomly Select A Student", command = pick_student)
student_picker.place(x=20,y=150, width=320, height=30)

#### VIEW ####





root.mainloop()