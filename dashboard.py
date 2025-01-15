from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk #pip install pillow
from employee import employeeClass
from supplier import supplierClass
from category import categoryClass
from product import productClass
from billing import BillClass
from sales import salesClass
import sqlite3
from tkinter import messagebox
import os
import time
import subprocess
class IMS:
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

        btn_employee=Button(LeftMenu,text="Staff",command=self.employee,image=self.icon_side,compound=LEFT,padx=5,anchor="w",font=("times new roman",15,"bold"),bg="white",bd=3,cursor="hand2").pack(side=TOP,fill=X)
        btn_supplier=Button(LeftMenu,text="Supplier",command=self.supplier,image=self.icon_side,compound=LEFT,padx=5,anchor="w",font=("times new roman",15,"bold"),bg="white",bd=3,cursor="hand2").pack(side=TOP,fill=X)
        btn_category=Button(LeftMenu,text="Category",command=self.category,image=self.icon_side,compound=LEFT,padx=5,anchor="w",font=("times new roman",15,"bold"),bg="white",bd=3,cursor="hand2").pack(side=TOP,fill=X)
        btn_product=Button(LeftMenu,text="Product",command=self.product,image=self.icon_side,compound=LEFT,padx=5,anchor="w",font=("times new roman",15,"bold"),bg="white",bd=3,cursor="hand2").pack(side=TOP,fill=X)
        btn_billing=Button(LeftMenu,text="Billing",command=self.billing,image=self.icon_side,compound=LEFT,padx=5,anchor="w",font=("times new roman",15,"bold"),bg="white",bd=3,cursor="hand2").pack(side=TOP,fill=X)
        btn_sales=Button(LeftMenu,text="Sales",command=self.sales,image=self.icon_side,compound=LEFT,padx=5,anchor="w",font=("times new roman",15,"bold"),bg="white",bd=3,cursor="hand2").pack(side=TOP,fill=X)
        btn_exit=Button(LeftMenu,text="Exit",image=self.icon_side,compound=LEFT,padx=5,anchor="w",font=("times new roman",15,"bold"),bg="white",bd=3,cursor="hand2").pack(side=TOP,fill=X)

        #===content===#
        self.lbl_employee=Label(self.root,text="Total Staff\n[0]",font=("goudy old style",15,"bold"),bd=5,relief=RIDGE,bg="#33bbf9",fg="white")
        self.lbl_employee.place(x=300,y=180,height=130,width=280)

        self.lbl_supplier=Label(self.root,text="Total Supplier\n[0]",font=("goudy old style",15,"bold"),bd=5,relief=RIDGE,bg="#ff5722",fg="white")
        self.lbl_supplier.place(x=600,y=180,height=130,width=280)

        self.lbl_category=Label(self.root,text="Total Category\n[0]",font=("goudy old style",15,"bold"),bd=5,relief=RIDGE,bg="#009688",fg="white")
        self.lbl_category.place(x=900,y=180,height=130,width=280)

        self.lbl_product=Label(self.root,text="Total Product\n[0]",font=("goudy old style",15,"bold"),bd=5,relief=RIDGE,bg="#607d8b",fg="white")
        self.lbl_product.place(x=445,y=360,height=130,width=280)

        self.lbl_sales=Label(self.root,text="Total Sales\n[0]",font=("goudy old style",15,"bold"),bd=5,relief=RIDGE,bg="#ffc107",fg="white")
        self.lbl_sales.place(x=745,y=360,height=130,width=280)

        #===footer===#
        lbl_footer=Label(self.root,text="IMS - Inventory Management System | Developed by CpE\nFor any Technical Issue Contact: 09359522372",font=("times new roman",10),bg="#4d636d",fg="white").pack(side=BOTTOM,fill=X)
        self.update_content()
        self.update_date_time()
    def employee(self):
        self.new_win=Toplevel(self.root)
        self.new_obj=employeeClass(self.new_win)

    def supplier(self):
        self.new_win=Toplevel(self.root)
        self.new_obj=supplierClass(self.new_win)

    def category(self):
        self.new_win=Toplevel(self.root)
        self.new_obj=categoryClass(self.new_win)

    def product(self):
        self.new_win=Toplevel(self.root)
        self.new_obj=productClass(self.new_win)

    def sales(self):
        self.new_win=Toplevel(self.root)
        self.new_obj=salesClass(self.new_win)

    def billing(self):
        self.new_win=Toplevel(self.root)
        self.new_obj=BillClass(self.new_win)

    def update_content(self):
        con=sqlite3.connect(database=r'inventory_system.db')
        cur=con.cursor()
        try:
            cur.execute("select * from product")
            product=cur.fetchall()
            self.lbl_product.config(text=f"Total Product\n{str(len(product))}")

            cur.execute("select * from supplier")
            supplier=cur.fetchall()
            self.lbl_supplier.config(text=f"Total Supplier\n{str(len(supplier))}")

            cur.execute("select * from category")
            category=cur.fetchall()
            self.lbl_category.config(text=f"Total Category\n{str(len(category))}")

            cur.execute("select * from employee")
            employee=cur.fetchall()
            self.lbl_employee.config(text=f"Total Staff\n{str(len(employee))}")

            bill=len(os.listdir('bill'))
            self.lbl_sales.config(text=f"Total Sales [{bill}]")
        
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to : {str(ex)}",parent=self.root)

    def update_date_time(self):
        time_=time.strftime("%I:%M:%S")
        date_=time.strftime("%d-%m-%Y")
        self.lbl_clock.config(text=f"Welcome to Inventory Management System \t\t Date: {str(date_)}\t\t Time: {str(time_)}")
        self.lbl_clock.after(200,self.update_date_time)

    # def logout(self):
    #     self.root.destroy()
    #     os.system("python login.py")

    def logout(self):
        self.root.destroy()
        subprocess.Popen(["python","login.py"])
        
if __name__=="__main__":
    root=Tk()
    obj=IMS(root)
    root.mainloop()