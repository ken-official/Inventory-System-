from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk #pip install pillow
from stock import stockClass
import sqlite3
from tkinter import messagebox
import os
import time
import subprocess
class userClass:
    def __init__(self, root):
        self.root=root
        self.root.geometry("1350x700+0+0")
        self.root.title("Inventory Management System")
        self.root.config(bg="white")

        #===title===#
        self.icon_title=PhotoImage(file="")
        title=Label(self.root,text="Inventory Management System",image=self.icon_title,compound=LEFT,font=("times new roman",40,"bold"),bg="#900c3f",fg="white",anchor="w",padx=20).place(x=0,y=0,relwidth=1,height=70)

        #===btn_logout===#
        btn_logout=Button(self.root,text="Logout",command=self.logout,font=("times new roman",15,"bold"),bg="yellow",cursor="hand2").place(x=1150,y=10,height=50,width=100)
        
        #===clock===#
        self.lbl_clock=Label(self.root,text="Welcome to Inventory Management System \t\t Date: DD-MM-YYYY\t\t Time: HH:MM:SS",font=("times new roman",15),bg="#c70039",fg="white")
        self.lbl_clock.place(x=0,y=70,relwidth=1,height=30)

        #===Left_Menu
        self.MenuLogo=Image.open("Images/csu.png")
        self.MenuLogo=self.MenuLogo.resize((200,200),Image.ANTIALIAS)
        self.MenuLogo=ImageTk.PhotoImage(self.MenuLogo)
        
        LeftMenu=Frame(self.root,bd=2,relief=RIDGE,bg="white")
        LeftMenu.place(x=0,y=102,width=200,height=565)

        lbl_MenuLogo=Label(LeftMenu,image=self.MenuLogo)
        lbl_MenuLogo.pack(side=TOP,fill=X)

        self.icon_side=PhotoImage(file="")
        lbl_menu=Label(LeftMenu,text="Menu",font=("times new roman",20),bg="#FF5733").pack(side=TOP,fill=X)
        btn_product=Button(LeftMenu,text="Product Stocks",command=self.stock,image=self.icon_side,compound=LEFT,padx=5,anchor="w",font=("times new roman",15,"bold"),bg="white",bd=3,cursor="hand2").pack(side=TOP,fill=X)

    def stock(self):
        self.new_win=Toplevel(self.root)
        self.new_obj=stockClass(self.new_win)

    def logout(self):
        self.root.destroy()
        subprocess.Popen(["python","login.py"])

if __name__=="__main__":
    root=Tk()
    obj=userClass(root)
    root.mainloop()