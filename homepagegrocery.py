from tkinter import *
from PIL import Image,ImageTk
root= Tk()
root.title("Welcome to Grocery Management System")
root.geometry('450x400')
image1=Image.open("homepageimage.jpg")
image1=image1.resize((1800,700),Image.ANTIALIAS)
background_image=ImageTk.PhotoImage(image1)
background_label=Label(root,image=background_image)
background_label.image=background_image
background_label.place(x=0,y=130)

main_label=Label(root,text="GROCERY MANAGEMENT SYSTEM",bg="#DC143C",width=100,height=1,fg="white",font=("times",20,"bold"))
main_label.place(x=5,y=0)

sub_label=Label(root,bg="#8A3324",width=100,height=2,fg="white",font=("times",20,"bold"))
sub_label.place(x=0,y=50)

    
def register_b():
    from subprocess import call
    call(["python","groceryregistrationpage.py"])

admin_button=Button(root,text="Admin Register",command=register_b,bg="#8B3A3A",width=15,height=1,fg="white",font=("times",15,"bold"))
admin_button.place(x=650,y=65)


root.mainloop()