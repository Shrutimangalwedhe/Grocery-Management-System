from tkinter import *
from PIL import Image, ImageTk
import sqlite3
from tkinter import messagebox as ms
import re
root = Tk()
root.title("Welcome to registration page")
root.geometry('800x800')   

image1 = Image.open("groceryregistrationimage.jpg")
image1 = image1.resize((810, 735), Image.ANTIALIAS)
background_image = ImageTk.PhotoImage(image1)
background_label = Label(root, image=background_image)
background_label.image = background_image
background_label.place(x=710, y=60)


Name=StringVar()
Username=StringVar()
Password=StringVar()

db = sqlite3.connect('grocery.db')
cursor = db.cursor()
create_table ='''CREATE TABLE IF NOT EXISTS groceryregistrationpage(
                            Name TEXT,
                            Username TEXT,
                            Password TEXT  
                          );'''
cursor.execute(create_table)
db.commit()


def password_check(passwd):
    SpecialSym = ['$', '@', '#', '%']
    val = True

    if len(passwd) < 6:
        print('length should be at least 6')
        val = False

    if len(passwd) > 20:
        print('length should not be greater than 20')
        val = False

    if not any(char.isdigit() for char in passwd):
        print('Password should have at least one numeral')
        val = False

    if not any(char.isupper() for char in passwd):
        print('Password should have at least one uppercase letter')
        val = False

    if not any(char.islower() for char in passwd):
        print('Password should have at least one lowercase letter')
        val = False

    if not any(char in SpecialSym for char in passwd):
        print('Password should have at least one of the symbols $@#')
        val = False

    if val:
        return val
    
def insert():
    name = Name.get()
    user_name = Username.get()
    passw = Password.get()
        
    db = sqlite3.connect('grocery.db')
    cursor = db.cursor()
    find_user = ('SELECT * FROM groceryregistrationpage WHERE Username=?')
    cursor.execute(find_user, [(Username.get())])
        
    if (name.isdigit() or (name == "")):
        ms.showinfo("Message", "please enter a valid name")
    elif (user_name == ""):
        ms.showinfo("Message", "Please enter a valid username")
    elif (cursor.fetchall()):
        ms.showerror('Error!', 'Username Taken. Try a Different One.')
    elif (passw == ""):
        ms.showinfo("Message", "Please enter a valid password")
    elif not password_check(passw):
        ms.showinfo("Message", "Password must contain at least 1 Uppercase letter, 1 symbol, 1 number")
    else:
        db = sqlite3.connect('grocery.db')
        cursor = db.cursor()
        insert_query = '''INSERT INTO groceryregistrationpage(Name,Username,Password) VALUES(?,?,?);'''
        user_data = (name, user_name, passw)
        cursor.execute(insert_query, user_data)
        db.commit()
        db.close()
        ms.showinfo('Success!', 'Account Created Successfully!')
        from subprocess import call
        call(["python", "groceryloginpage.py"])



main_label=Label(root,text="GROCERY MANAGEMENT SYSTEM",bg="#DC143C",width=43,height=1,fg="white",font=("times",20,"bold"))
main_label.place(x=370,y=0)

frame_alpr = LabelFrame(root,width=700, height=735, bd=5, font=("times", 14, "bold"), bg="#1874CD")
frame_alpr.grid(row=0, column=0, sticky="nw")
frame_alpr.place(x=10, y=60)

loginlabel=Label(root,text="REGISTRATION",bg="#1874CD",width=20,height=1,fg="black",font=("times",20,"bold"))
loginlabel.place(x=180,y=80) 

name = Label(root, text="Name", bg="#CD2990", width=15, height=1, fg="white", font=("times", 20, "bold"))
name.place(x=40, y=170)

nameentry = Entry(root, textvar=Name,width=18, font=("times", 22, "bold"))
nameentry.place(x=330, y=170)

username1 = Label(root, text="Username", bg="#CD2990", width=15, height=1, fg="white", font=("times", 20, "bold"))
username1.place(x=40, y=290)

username1entry = Entry(root,textvar=Username, width=18, font=("times", 22, "bold"))
username1entry.place(x=330, y=290)

password1 = Label(root, text="Password", bg="#CD2990", width=15, height=1, fg="white", font=("times", 20, "bold"))
password1.place(x=40, y=420)

password1entry = Entry(root,textvar=Password, width=18, font=("times", 22, "bold"))
password1entry.place(x=330, y=420)

button = Button(root, text="REGISTER", bg="#CD6889", width=15, height=1, fg="white", font=("times", 15, "bold"),command=insert)
button.place(x=200, y=580)

root.mainloop()