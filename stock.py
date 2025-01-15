from tkinter import*
from PIL import Image,ImageTk #pip install pillow
from tkinter import ttk,messagebox
import sqlite3
import time
class stockClass:
    def __init__(self, root):
        self.root=root
        self.root.geometry("1100x500+220+130")
        self.root.title("Inventory Management System")
        self.root.config(bg="white")
        self.root.focus_force()

        self.var_searchby=StringVar()
        self.var_searchtxt=StringVar()

        self.var_pid=StringVar()
        self.var_cat=StringVar()
        self.var_sup=StringVar()
        self.cat_list=[]
        self.sup_list=[]
        self.var_name=StringVar()
        self.var_price=StringVar()
        self.var_qty=StringVar()
        self.var_status=StringVar()

        #===title===#
        self.icon_title=PhotoImage(file="")
        title=Label(self.root,text="Inventory Management System",image=self.icon_title,compound=LEFT,font=("times new roman",40,"bold"),bg="#900c3f",fg="white",anchor="w",padx=20).place(x=0,y=0,relwidth=1,height=70)

        #===btn_logout===#
        btn_logout=Button(self.root,text="Logout",font=("times new roman",15,"bold"),bg="yellow",cursor="hand2").place(x=1150,y=10,height=50,width=100)
        
        #===clock===#
        self.lbl_clock=Label(self.root,text="Welcome to Inventory Management System \t\t Date: DD-MM-YYYY\t\t Time: HH:MM:SS",font=("times new roman",15),bg="#c70039",fg="white")
        self.lbl_clock.place(x=0,y=70,relwidth=1,height=30)

        product_Frame=Frame(self.root,bd=3,relief=RIDGE,bg="white")
        product_Frame.place(x=10,y=105,width=1080,height=390)

        scrolly=Scrollbar(product_Frame,orient=VERTICAL)
        scrollx=Scrollbar(product_Frame,orient=HORIZONTAL)

        self.product_Table=ttk.Treeview(product_Frame,columns=("pid","name","price","qty","status"),yscrollcommand=scrolly.set,xscrollcommand=scrollx.set)
        scrollx.pack(side=BOTTOM,fill=X)
        scrolly.pack(side=RIGHT,fill=Y)
        scrollx.config(command=self.product_Table.xview)
        scrolly.config(command=self.product_Table.yview)

        self.product_Table.heading("pid",text="P ID")
        self.product_Table.heading("name",text="Name")
        self.product_Table.heading("price",text="Price")
        self.product_Table.heading("qty",text="Qty")
        self.product_Table.heading("status",text="Status")
        self.product_Table["show"]="headings"

        self.product_Table.column("pid",width=40)
        self.product_Table.column("name",width=100)
        self.product_Table.column("price",width=100)
        self.product_Table.column("qty",width=40)
        self.product_Table.column("status",width=90)
        self.product_Table.pack(fill=BOTH,expand=1)
        # self.product_Table.bind("<ButtonRelease-1>",self.get_data)

        self.show()
        self.update_date_time()

    # def get_data(self,ev):
    #     f=self.product_Table.focus()
    #     content=(self.product_Table.item(f))
    #     row=content['values']
    #     self.var_pid.set(row[0])
    #     self.var_pname.set(row[1])
    #     self.var_price.set(row[2])
    #     self.lbl_inStock.config(text=f"In Stock [{str(row[3])}]")
    #     self.var_stock.set(row[3])
    #     self.var_qty.set('1')

    def show(self):
        con=sqlite3.connect(database=r'inventory_system.db')
        cur=con.cursor()
        try:
            cur.execute("select pid,name,price,qty,status from product where status='Active'")
            rows=cur.fetchall()
            self.product_Table.delete(*self.product_Table.get_children())
            for row in rows:
                self.product_Table.insert('',END,values=row)
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to : {str(ex)}",parent=self.root)

    def update_date_time(self):
        time_=time.strftime("%I:%M:%S")
        date_=time.strftime("%d-%m-%Y")
        self.lbl_clock.config(text=f"Welcome to Inventory Management System \t\t Date: {str(date_)}\t\t Time: {str(time_)}")
        self.lbl_clock.after(200,self.update_date_time)



if __name__=="__main__":
    root=Tk()
    obj=stockClass(root)
    root.mainloop()