from tkinter import *
from tkinter import ttk
import tkinter as tk
import sqlite3
import tkinter.messagebox

root=Tk()
root.geometry("600x600")
root.title("STUDENT DATABASE MANAGEMENT SYSTEM")
labelt=Label(root,text="SELECT YOUR OCCUPATION",font=("algerian",15))
labelt.grid(row=2,column=10,padx=(30,30),pady=(30,0))


connection=sqlite3.connect("Student4.db")
print("Database created Successfully")


TABLE_NAME = "student_table"
STUDENT_SAPID = "student_sapid"
STUDENT_NAME = "student_name"
STUDENT_COLLEGE = "student_college"
STUDENT_ADDRESS = "student_address"
STUDENT_PHONE = "student_phone"

TABLE_NAME5 = 'marks_table'
STUDENT_SAPID = 'student_sapid'
PHYSICS_MARKS = 'physics_marks'
CHEM_MARKS = 'chem_marks'
MATHS_MARKS = 'maths_marks'
ENGLISH_MARKS = 'english_marks'


def a1():

    firstWindow=tk.Tk()
    firstWindow.geometry("800x800")
    firstWindow.resizable(0,0)

    firstWindow.title("STUDENT DATABASE")
    label1=Label(firstWindow,text="Welcome",font=("Algerian",15),fg="Green")
    label1.grid(row=0,column=1,padx=(30,30),pady=(30,30))
    sap = Label(firstWindow, text="ENTER YOUR SAPID", font=("Sylfaen,15"))
    sap.grid(row=1, column=0, padx=(20, 20), pady=(30, 30))
    namelabel = Label(firstWindow, text="ENTER YOUR NAME", font=("Sylfaen,15"))
    namelabel.grid(row=2, column=0, padx=(20, 20), pady=(30, 30))
    collegelabel = Label(firstWindow, text="ENTER YOUR COLLEGE", font=("Sylfaen,15"))
    collegelabel.grid(row=3, column=0, padx=(20, 20), pady=(30, 30))
    addresslabel = Label(firstWindow, text="ENTER YOUR ADDRESS", font=("Sylfaen,15"))
    addresslabel.grid(row=4, column=0, padx=(20, 20), pady=(30, 30))
    phonelabel = Label(firstWindow, text="ENTER YOUR PHONE NUMBER", font=("Sylfaen,15"))
    phonelabel.grid(row=5, column=0, padx=(20, 20), pady=(30, 30))


    e1 = Entry(firstWindow)
    e1.grid(row=1, column=1)
    e2 = Entry(firstWindow)
    e2.grid(row=2, column=1)
    e3 = Entry(firstWindow)
    e3.grid(row=3, column=1)
    e4 = Entry(firstWindow)
    e4.grid(row=4, column=1)
    e5 = Entry(firstWindow)
    e5.grid(row=5, column=1)



    if connection.execute(" CREATE TABLE IF NOT EXISTS " + TABLE_NAME + " ( " + STUDENT_SAPID +" INTEGER PRIMARY KEY , " +STUDENT_NAME + " TEXT, " + STUDENT_COLLEGE + " TEXT, " +  STUDENT_ADDRESS + " TEXT, " + STUDENT_PHONE + " NUMERIC);"):
        print("StudentTable created sucessfully ")

    def student():
        sap=e1.get()
        e1.delete(0,END)
        name = e2.get()
        e2.delete(0, END)
        college = e3.get()
        e3.delete(0, END)
        address = e4.get()
        e4.delete(0, END)
        phone = e5.get()
        e5.delete(0, END)


        connection.execute("INSERT INTO " + TABLE_NAME + " ( " + STUDENT_SAPID + ", " + STUDENT_NAME + ", " +
                           STUDENT_COLLEGE + ", " + STUDENT_ADDRESS + ", " +
                           STUDENT_PHONE + " ) VALUES (  '" + sap + " ', '"
                           + name + "', '" + college + "', '" +
                           address + "', " + str(phone) + " ); ")
        connection.commit()

        cursor1 = connection.execute("SELECT * FROM " + TABLE_NAME + " WHERE " + STUDENT_SAPID + " = '" + sap + "';")
        print(cursor1)
        a=""

    b1 = Button(firstWindow, text="SUBMIT", font=("Sylfaen", 10), command=student, fg="blue")
    b1.grid(row=9, column=0)

    dButton = Button(firstWindow, text="Display result", font=("Sylfaen", 10), command=submit,
                     fg="blue",bg="pink")
    dButton.grid(row=9, column=2)
    dButton = Button(firstWindow, text="Display data", font=("Sylfaen", 10), command=result,
                     fg="blue",bg='pink')
    dButton.grid(row=9, column=3)
    firstWindow.mainloop()


def result():

    mainWindow = tk.Tk()
    mainWindow.title("Display results")
    appLabel = tk.Label(mainWindow, text="Student Management System", fg="purple", width=40)
    appLabel.config(font=("Algerian", 30))
    appLabel.pack()

    tree = ttk.Treeview(mainWindow)
    tree["columns"] = ("one", "two", "three", "four", "five", "six")
    tree.column("one", width=200)
    tree.column("two", width=200)
    tree.column("three", width=200)
    tree.column("four", width=200)
    tree.column("five", width=200)
    tree.column("six", width=200)

    tree.heading("one", text="Student Enrollment Number")
    tree.heading("two", text="Student Name")
    tree.heading("three", text="College Name")
    tree.heading("four", text="Address")
    tree.heading("five", text="Phone Number")
    tree.heading("six", text="GENDER")

    cursor = connection.execute("SELECT * FROM " + TABLE_NAME + " ;")
    i = 0

    for row in cursor:
        tree.insert('', i, text="Student Data",values=(row[0], row[1],row[2], row[3], row[4]))
        i = i + 1

    tree.pack()

    mainWindow.mainloop()


def teacher():
    thirdWindow=tk.Tk()
    thirdWindow.title("Marks")
    thirdWindow.geometry("800x800")
    label4=Label(thirdWindow,text="Student Grade Card Marking System",font=("Sylfaen,15"),fg="purple")
    label4.grid(row=0,column=1,padx=(30,30),pady=(30,30))
    idelabel = Label(thirdWindow, text="ENTER SAPID", font=("Sylfaen,15"))
    idelabel.grid(row=1, column=0, padx=(20, 20), pady=(30, 30))
    phylabel = Label(thirdWindow, text="ENTER PHYSICS MARKS", font=("Sylfaen,15"))
    phylabel.grid(row=2, column=0, padx=(20, 20), pady=(30, 30))
    chemlabel = Label(thirdWindow, text="ENTER CHEMISTRY MARKS", font=("Sylfaen,15"))
    chemlabel.grid(row=3, column=0, padx=(20, 20), pady=(30, 30))
    mathlabel = Label(thirdWindow, text="ENTER MATHS MARKS", font=("Sylfaen,15"))
    mathlabel.grid(row=4, column=0, padx=(20, 20), pady=(30, 30))
    englishlabel = Label(thirdWindow, text="ENTER ENGLISH MARKS", font=("Sylfaen,15"))
    englishlabel.grid(row=5, column=0, padx=(20, 20), pady=(30, 30))

    ei = Entry(thirdWindow)
    ei.grid(row=1, column=1)
    ep = Entry(thirdWindow)
    ep.grid(row=2, column=1)
    ec = Entry(thirdWindow)
    ec.grid(row=3, column=1)
    em = Entry(thirdWindow)
    em.grid(row=4, column=1)
    ee = Entry(thirdWindow)
    ee.grid(row=5, column=1)

    if connection.execute(
            " CREATE TABLE IF NOT EXISTS " + TABLE_NAME5 + " ( " + STUDENT_SAPID + " INTEGER PRIMARY KEY , " + PHYSICS_MARKS + " INTEGER, " + CHEM_MARKS + " INTEGER, " + MATHS_MARKS + " INTEGER, " + ENGLISH_MARKS + " INTEGER);"):
        print("MarksTable created sucessfully ")

    def submit2():
        ide=ei.get()
        ei.delete(0,END)
        phy = ep.get()
        ep.delete(0, END)
        chem = ec.get()
        ec.delete(0, END)
        math = em.get()
        em.delete(0, END)
        english = ee.get()
        ee.delete(0, END)



        connection.execute("INSERT INTO " + TABLE_NAME5 + " ( " + STUDENT_SAPID + ", " + PHYSICS_MARKS  + ", " +
                           CHEM_MARKS + ", " + MATHS_MARKS + ", " +
                          ENGLISH_MARKS + " ) VALUES ( '" +ide + " ', '" + phy + " ', '"
                           + chem + "', '" + math + "', ' " + english + " '  ); ")
        connection.commit()


    b4 = Button(thirdWindow, text="Submit", command=submit2, fg="blue",bg="light blue")
    b4.grid(row=9, column=0)
    b8 = Button(thirdWindow, text="Display Marks", command=displaymarks,bg="light blue",
                fg="black")
    b8.grid(row=9, column=1)
    thirdWindow.mainloop()

def displaymarks():

    forthWindow = tk.Tk()
    forthWindow.title("Display marks")
    appLabel = tk.Label(forthWindow, text="Students Results", fg="purple", width=40)
    appLabel.config(font=("Algerian", 30))
    appLabel.pack()

    tree = ttk.Treeview(forthWindow)
    tree["columns"] = ("one", "two", "three", "four", "five")
    tree.column("one", width=200)
    tree.column("two", width=200)
    tree.column("three", width=200)
    tree.column("four", width=200)
    tree.column("five", width=200)

    tree.heading("one", text="Student ID")
    tree.heading("two", text="PHYSICS MARKS")
    tree.heading("three", text="CHEMISTRY MARKS")
    tree.heading("four", text="MATH MARKS")
    tree.heading("five", text="ENGLISH MARKS")

    cursor2 = connection.execute("SELECT * FROM " + TABLE_NAME5 + " ;")
    i = 0

    for row in cursor2:
        tree.insert('', i, text="Student Data",
                    values=(row[0], row[1],
                            row[2], row[3], row[4]))
        i = i + 1


    tree.pack()


def submit():
    secondWindow = tk.Tk()
    secondWindow.title("Student Login")
    label1 = Label(secondWindow, text="Student Login", fg="#0000A0", width="100")
    label1.grid(row=0, columnspan=2, padx=(30, 30), pady=(30, 30))
    loginLabel = Label(secondWindow, text="Enter Your Login ID", width="40", fg="#FF0000")
    loginLabel.grid(row=1, column=0, padx=(30, 30), pady=(30, 30))
    loginvar = Entry(secondWindow)
    loginvar.grid(row=1, column=1)

    def submit3():
        fifthWindow = tk.Tk()
        fifthWindow.title("Display marks")
        login=loginvar.get()
        loginvar.delete(0,END)
        cursor2=connection.execute("SELECT * FROM " + TABLE_NAME + " WHERE "  +STUDENT_SAPID+" = "+login+" ;")
        print(cursor2)
        b=0
        for row in cursor2:
            b=row[0]
        if b==int(login):

             appLabel = tk.Label(fifthWindow, text="Students Results", fg="purple", width=40)
             appLabel.config(font=("Algerian", 30))
             appLabel.pack()

             tree = ttk.Treeview(fifthWindow)
             tree["columns"] = ("one", "two", "three", "four", "five")
             tree.column("one", width=200)
             tree.column("two", width=200)
             tree.column("three", width=200)
             tree.column("four", width=200)
             tree.column("five", width=200)

             tree.heading("one", text="Student ID")
             tree.heading("two", text="PHYSICS MARKS")
             tree.heading("three", text="CHEMISTRY MARKS")
             tree.heading("four", text="MATH MARKS")
             tree.heading("five", text="ENGLISH MARKS")
             cursor2 = connection.execute("SELECT * FROM " + TABLE_NAME5 + " WHERE " + STUDENT_SAPID + " = " + login + " ;")

             i = 0
             for row in cursor2:
                    tree.insert('', i, text="Student Data",
                                values=(row[0], row[1],
                                        row[2], row[3], row[4]))
                    i = i + 1
             var = (int(row[1]) + int(row[2]) + int(row[3]) + int(row[4])) / 4
             if int(var) > 35:
                 label88 = tk.Label(fifthWindow,
                                    text="Congratulation " + str(row[0]) + " ! You have secured " + str(var) + "%age",
                                    width=100, fg="Green")
                 label88.config(font=("Sylfaen", 20))
                 label88.pack()
             else:
                 label99 = tk.Label(fifthWindow,
                                    text="Sorry  " + str(row[0]) + "! You have secured " + str(var) + "%age" + ". ",
                                    width=80,
                                    fg="#FF0000")
                 label99.config(font=("Sylfaen", 20))
                 label99.pack()
             tree.pack()

        else:
            tkinter.messagebox.showinfo('Error', "Sorry! SAP_ID is not registerd with us")
        fifthWindow.mainloop()
    b9 = Button(secondWindow, text="SUBMIT",
                command=submit3, bg="light blue", fg="black")
    b9.grid(row=4, column=20, padx=30, pady=40, sticky=W)
    secondWindow.mainloop()

b9 = Button(root, text="STUDENT", command=a1, height=10, width=30, bg="light pink", fg="black",font=("Sylfaen", 10))
b9.grid(row=4, column=20, padx=20, pady=40, sticky=W)
tbutton=Button(root,text='TEACHER',font=("Sylfaen", 10), command=teacher,fg="black" , height= 10,width=30,bg="light pink")
tbutton.grid(row=8,column=20 , padx=20,pady=40)

root.mainloop()
