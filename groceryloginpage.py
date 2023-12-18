from tkinter import *
from PIL import Image, ImageTk
import sqlite3
from tkinter import messagebox as ms
import re



root = Tk()
root.title("Welcome to login page")
root.geometry('800x800')
image1 = Image.open("groceryloginimage.jpg")
image1 = image1.resize((800, 700), Image.ANTIALIAS)
background_image = ImageTk.PhotoImage(image1)
background_label = Label(root, image=background_image)
background_label.image = background_image
background_label.place(x=730, y=75)

Username=StringVar()
Password=StringVar()




def insert():
    
    user_name = Username.get()
    passw = Password.get()
    
    db = sqlite3.connect('grocery.db')
    cursor = db.cursor()
    find_user = ('SELECT * FROM groceryregistrationpage WHERE Username = ? AND Password=?')
    
    cursor.execute(find_user,[(Username.get()),(Password.get())])
    result=cursor.fetchall()
    
    
    
      
    
    if result:
        msg=""
        print(msg)
        ms.showinfo("message","login successfully") 
        
        from subprocess import call
        call(['python','addgrocery.py'])
        
    elif (user_name == ""):
        ms.showinfo("Message", "Please enter a valid username")
    elif (passw == ""):
            ms.showinfo("Message", "Please enter a valid password")
            
    else:
        ms.showinfo("oops!","username or password are not found match")
        
        
        

        



main_label=Label(root,text="GROCERY MANAGEMENT SYSTEM",bg="#DC143C",width=43,height=1,fg="white",font=("times",20,"bold"))
main_label.place(x=370,y=0)

frame_alpr = LabelFrame(root, width=700, height=700, bd=5, font=("times", 14, "bold"), bg="#43CD80")
frame_alpr.grid(row=0, column=0, sticky="nw")
frame_alpr.place(x=15, y=80)



loginlabel=Label(root,text="LOGIN",bg="#43CD80",width=30,height=2,fg="black",font=("times",25,"bold"))
loginlabel.place(x=20,y=110) 

Username1 = Label(root, text="User Name", bg="#7A67EE", width=13, height=1, fg="white", font=("times", 20, "bold"))
Username1.place(x=80, y=300)

uentry1 = Entry(root, textvar=Username,width=17, font=("times", 20, "bold"))
uentry1.place(x=340, y=300)

Password1 = Label(root, text="Password", bg="#7A67EE", width=13, height=1, fg="white", font=("times", 20, "bold"))
Password1.place(x=80, y=400)

pentry1 = Entry(root,textvar=Password, width=17, font=("times", 20, "bold"))
pentry1.place(x=340, y=400)

    
button = Button(root, text="login", bg="#9FB6CD", width=15, height=1, fg="white", font=("times", 20, "bold"),command=insert)
button.place(x=200, y=550)



root.mainloop()