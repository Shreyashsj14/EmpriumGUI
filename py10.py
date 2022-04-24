
from tkinter import *
from tkinter import messagebox as mbox
import mysql.connector as mysql


mydb = mysql.connect(host="localhost",user="root",passwd="",database="my_db")
mycur = mydb.cursor()

class MyEntry:
    def __init__(self,root):
        self.frame = Frame(root)
        self.frame.pack()
        self.f1 = Frame(self.frame,bg="#dabf00")
        
        self.search = Button(self.f1, text="Search", command=lambda :[ self.f1.destroy(),self.search_page()])
        self.search.pack(side=RIGHT)

        self.insert = Button(self.f1, text="Insert Details", command=lambda :[self.insert_page(), self.f1.destroy()])
        self.insert.pack(side=RIGHT)

        self.f1.pack(expand=True)

    def insert_page(self):
        self.frame = Frame(root)
        self.frame.pack()
        self.f = Frame(self.frame, height=300, width=270, bg='#dabf00')  # Defining a Frame for the gui
        self.l1 = Label(self.f, text="Enter your name:")  # Adding label for name
        self.l1.grid(row=0, column=0, pady=4)  # Getting the label placed
        fnt = ("Times New Roman", 14)
        self.e1 = Entry(self.f, width=15, fg="black", bg="gray", font=fnt)  # Entry box for name
        self.e1.grid(row=0, column=1, pady=4, padx=3)
        self.l2 = Label(self.f, text="Enter your age")  # Adding Label for marks
        self.l2.grid(row=1, column=0, pady=4)
        self.e2 = Entry(self.f, width=15, fg="black", bg="gray", font=fnt)  # Entry box for marks
        self.e2.grid(row=1, column=1, pady=4, padx=3)

        # self.val1 = StringVar()  # Taking the variable
        self.l3 = Label(self.f, text="Enter your Height:")  # Adding label for city
        self.l3.grid(row=2, column=0, pady=4)
        self.e3 = Entry(self.f, width=15, fg="black", bg="gray", font=fnt)  # Entry box for marks
        self.e3.grid(row=2, column=1, pady=4, padx=3)

        self.l4 = Label(self.f, text="Enter your weight:")  # Adding label for city
        self.l4.grid(row=3, column=0, pady=4)
        self.e4 = Entry(self.f, width=15, fg="black", bg="gray", font=fnt)  # Entry box for marks
        self.e4.grid(row=3, column=1, pady=4, padx=3)

        self.l5 = Label(self.f, text="Enter your Qualification :")  # Adding label for city
        self.l5.grid(row=4, column=0, pady=4)
        self.e5 = Entry(self.f, width=15, fg="black", bg="gray", font=fnt)  # Entry box for marks
        self.e5.grid(row=4, column=1, pady=4, padx=3)

        self.l6 = Label(self.f, text="Enter your Hobby:")  # Adding label for city
        self.l6.grid(row=5, column=0, pady=4)
               self.e6 = Entry(self.f, width=15, fg="black", bg="gray", font=fnt)  # Entry box for marks
        self.e6.grid(row=5, column=1, pady=4, padx=3)
        self.b = Button(self.f, text="ADD Details", command=self.insert_data)  # Adding button for displaying details
        self.b.grid(row=7, column=1, columnspan=2, pady=8)
        self.f.pack(side=TOP)

    def insert_data(self):

        name = self.e1.get()  # printing name
        age = int(self.e2.get())  # printing marks
        height = int(self.e3.get())
        weight = int(self.e4.get())
        Quali = self.e5.get()
        hobby = self.e6.get()
        data = (name, age, height, weight, Quali, hobby)
        query = 'insert into information(Name,age,height,weight,Qualification,hobby) values(%s,%s,%s,%s,%s,%s)'
        mycur.execute(query, data)
        mydb.commit()
        mbox.showinfo("Message", "Data inserted")

    # Function to display the output
    def search_page(self):
        frame = Frame(root)
        frame.place(x=12,y=20)
        val1 = StringVar()
        l1 = Label(frame,text="Search By")
        s1 = Spinbox(frame, values=("Name","Info_id"), textvariable=val1, width=15,
                          fg="black", font="Arial 12")
        e = Entry(frame,width=10)
        l1.pack(side=LEFT)
        s1.pack(side=LEFT)
        e.pack(side=LEFT)
        but = Button(frame,text="Search",command=lambda :[self.search_data(e.get(),val1.get())])
        but.pack()

    def search_data(self,name,command):
        try:

            if command == "Name":
                data = (name,)
                quer = 'select * from information where Name=%s'
            elif command == 'Info_id':
                name=int(name)
                data = (name,)
                quer = 'select * from information where Info_id=%s'

            mycur.execute(quer, data)
            res = mycur.fetchall()
            l7 = Label(text="Name :" + res[0][0], font=("Times New Roman", 18)).place(x=50, y=150)
            l8 = Label(text="age :" + str(res[0][1]), font=("Times New Roman", 18)).place(x=50, y=190)
            l9 = Label(text="Height : " + str(res[0][2]), font=("Times New Roman", 18)).place(x=50, y=230)
            l6 = Label(text="Weight :" + str(res[0][3]), font=("Times New Roman", 18)).place(x=50, y=270)
            l10 = Label(text="Qualification :" + res[0][4], font=("Times New Roman", 18)).place(x=50, y=310)
            l11 = Label(text="Hobby :" + res[0][5], font=("Times New Roman", 18)).place(x=50, y=350)
        except:
            l = Label(text='NOT FOUND', font=("Times New Roman", 22)).place(x=50, y=300)



root = Tk()  # Creating root
root.title("This is a GUI Application")  # Giving a title
root.geometry('600x470')
mb = MyEntry(root)  # Calling the function
root.mainloop()