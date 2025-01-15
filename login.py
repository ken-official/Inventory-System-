from tkinter import*
from PIL import ImageTk,Image,ImageDraw,ImageFont
from tkinter import messagebox
import sqlite3
import os
class Login_System:
    def __init__(self,root):
        self.root=root
        self.root.title("Login System")
        self.root.geometry("1350x700+0+0")
        self.employee_id=StringVar()
        self.password=StringVar()

        self.bg=ImageTk.PhotoImage(file="Images/trial.png")

        canvas=Canvas(self.root)
        canvas.create_image(0,0,image=self.bg,anchor=NW)
        canvas.create_text(670,425,text="Username",font=("poppins",15,"bold"),fil="black")
        self.txt_username=Entry(self.root,textvariable=self.employee_id,font=("poppins",13),bg="lightblue")
        self.txt_username.place(x=620,y=440,width=200,height=30)
        canvas.create_text(670,505,text="Password",font=("poppins",15,"bold"),fil="white")
        txt_password=Entry(self.root,textvariable=self.password,show="*",font=("poppins",13),bg="lightblue")
        txt_password.place(x=620,y=520,width=200,height=30)
        canvas.pack(fill="both",expand=True)

        #===Button Log in===#
        btn_login=Button(self.root,text="Log in",command=self.login,font=("poppins",15),cursor="hand2")
        btn_login.place(x=620,y=570,width=200,height=30)

        btn_forgot_button=Button(self.root,text="Forgot Password",font=("poppins",8),cursor="hand2")
        btn_forgot_button.place(x=655,y=620,width=120,height=20)

        btn_sign_up=Button(self.root,text="Sign up",font=("poppins",8),cursor="hand2")
        btn_sign_up.place(x=655,y=650,width=120,height=20)

    #===Log in Condition===#
    def login(self):
        con=sqlite3.connect(database=r'inventory_system.db')
        cur=con.cursor()
        try:
            if self.employee_id.get()=="" or self.password.get()=="":
                messagebox.showerror("Error","All Fields are Required to be Filled",parent=self.root)
            else:
                cur.execute("select utype from employee where eid=? AND pass=?",(self.employee_id.get(),self.password.get()))
                user=cur.fetchone()
                if user==None:
                    messagebox.showerror("Error",f"Error due to : INVALID USERNAME OR PASSWORD",parent=self.root)
                else:
                    if user[0]=="Admin":
                        self.root.destroy()
                        os.system("python dashboard.py")
                    else:
                        self.root.destroy()
                        os.system("python user.py")
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to : {str(ex)}",parent=self.root)


root=Tk()
obj=Login_System(root)  
root.mainloop() 