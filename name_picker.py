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
    list = ["Miles Boebel","Luke Busse","Quetzali Rene","Nolan Fowler","Jonah Gysan","Oliver Hanshaw","Abhishek Haridass","Emme Lou Howard","Jose Jaramillo","Lin Khonthongdee","Eshan Lakshmanan-Gulley","AJ Landis","Mary Maebius","Clark McCraw","Henry Palmer","Bodhi Prater","Hutchins Reilly","Emmanuel Rivera","Emma Rock","Kenner Stahlman","Karlin Stansbury","Teika Thomas","Mason Washington Jr.","Vincent Wattenbarger"]
    clase.config(text="First Period")

def second_period():
    global list
    list = ["Kennedy Aleshire","Elizabeth Avila Escobedo", "Delaney Bishop","Ava Borich","Clara Burns","Brianna Cortez","Wendel Dos Santos","Kole Esselstyn","Kirsten Hana", "Trey Hussey","Savannah Hynes","Ocean Jennison","Harper Kelly","Magnolia Kinard","Julien Lavoie","KD Manning","Wynn McConnell","Sophia Medina","Ryder Mejia","Maya Melendez","Gray Morey","Kelson Nichols","Lily Nixon","Marlon Perez-Velasquez","Dario Rangel","Maximiliano Reyes-Duran","Sebatian Sam","Lee Smith","Eline Van Der Steur"]
    clase.config(text="Second Period")

def third_period():
    global list
    list = ["Leia Aguilar","Mackenzie Augspurger","Mason Begley","Carlos Benitez_Ruiz","Avery Billela","Tagore Bose","Catherine Breed","Indira Burden Guevara","Anontion Byrne","Giuliana Carpenter","Maya Castillo","Luys Castro","Zyon Chapman-Garcia","Nataneli Chavez","Jayla Diaz","Charley Emshwiller","Audrey Goodacre","CJ Hernandez","Albert Hernandez-Lopez","Olivia Hollander","Sadie Hurless","Landon Jones","Xander Lecompte","Isaiah Marmolejo","Matthew Martinez","Syriana Martinez","Jose Martinez Rangel","Davis Moon","Noah Ramirez","Jaelyn Rivera","Coryn Rodriguez", "Abraham Ruiz","Natalie Santa Ana"]
    clase.config(text="Third Period")

def fifth_period():
    global list
    list = ["Seville Bohn","Kai Brooks","Dawson Dittmar","Iggy Gillion","Frank Hadlock","Tate Hentrich","Joseph Jeong","Maddy Kaven","Jonathan Lamping","Nikolai Lesak","Jack Padgett","Ben Palmer","Nash Parker","Alex Parsons","Jacob Patt","Aaron Sabisch","Quinn Skidmore","Noam Stewart"]
    clase.config(text="Fifth Period")

def sixth_period():
    global list
    list = ["Blake Sophia Bernstein","Owen Boshart","Elijah Debusk","Caleb Deleon","Owen Fannin","Jordan Freeman","Edgar Garcia-Fajardo","Weston Gardner","Owen Harper","John Hortman","Gavin Kirsch","Madeline Lafollette","Anderson Marin Garcia","Roman Mengarelli","Toby Moffitt","Henry Morris","Luke Morrison","Nathan Nada","Tristan Papworth","Huy Quach","Khang Quach","Danielle Ramirez","Fatima Reyes Duran","Roman Salaz"]
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
