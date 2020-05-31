from tkinter import *
from tkinter import ttk
import pymysql
from tkinter import messagebox
class Student:
    def __init__(self,root):
        self.root=root
        self.root.title("FIXED DEPOSIT")
        self.root.geometry("1350x700+0+0")
        title=Label(self.root,text="FIXED DEPOSIT",bd=10,relief=GROOVE,font=("times new roman",40,"bold"),bg="CRIMSON",fg="white")
        title.pack(side=TOP,fill=X)
        # All variables==================================================================
        self.BANK_NAME_var=StringVar()
        self.ISSUE_DATE_var = StringVar()
        self.NAME_var = StringVar()
        self.AMOUNT_var = StringVar()
        self.MATURITY_var = StringVar()
        self.DUE_DATE_var = StringVar()
        self.ACC_NO_var = StringVar()
        self.search_by = StringVar()
        self.search_txt = StringVar()
        #manage frames==================================================================
        Manage_Frame=Frame(self.root,bd=4,relief=RIDGE,bg="crimson")
        Manage_Frame.place(x=20,y=100,width=450,height=570)
        m_title=Label(Manage_Frame,text="FD Details :-",bg="crimson",fg="white",font=("times new roman",20,"bold"))
        m_title.grid(row=0,column=0,pady=20)

        BANK_NAME = Label(Manage_Frame, text="BANK NAME",bg="crimson",fg="white",font=("times new roman",15,"bold"))
        BANK_NAME.grid(row=1,column=0,pady=10,padx=20,sticky="w")
        ISSUE_DATE = Label(Manage_Frame, text="ISSUE DATE",bg="crimson",fg="white",font=("times new roman",15,"bold"))
        ISSUE_DATE.grid(row=2, column=0,pady=10,padx=20,sticky="w")
        NAME = Label(Manage_Frame, text="NAME",bg="crimson",fg="white",font=("times new roman",15,"bold"))
        NAME.grid(row=3, column=0,pady=10,padx=20,sticky="w")
        AMOUNT = Label(Manage_Frame, text="AMOUNT",bg="crimson",fg="white",font=("times new roman",15,"bold"))
        AMOUNT.grid(row=4, column=0,pady=10,padx=20,sticky="w")
        MATURITY = Label(Manage_Frame, text="MATURITY",bg="crimson",fg="white",font=("times new roman",15,"bold"))
        MATURITY.grid(row=5, column=0,pady=10,padx=20,sticky="w")
        DUE_DATE = Label(Manage_Frame, text="DUE DATE",bg="crimson",fg="white",font=("times new roman",15,"bold"))
        DUE_DATE.grid(row=6, column=0,pady=10,padx=20,sticky="w")
        ACC_NO = Label(Manage_Frame, text="ACC NO",bg="crimson",fg="white",font=("times new roman",15,"bold"))
        ACC_NO.grid(row=7, column=0,pady=10,padx=20,sticky="w")

        entry1 = ttk.Combobox(Manage_Frame,textvariable=self.BANK_NAME_var,font=("times new roman",15,"bold"),bd=5,state="readonly")
        entry1['values']=("BOI","SBI")
        entry1.grid(row=1, column=1,pady=10,padx=20,sticky="w")
        entry2 = Entry(Manage_Frame,textvariable=self.ISSUE_DATE_var,font=("times new roman",15,"bold"),bd=5,relief=GROOVE)
        entry2.grid(row=2, column=1,pady=10,padx=20,sticky="w")
        entry3 = Entry(Manage_Frame,textvariable=self.NAME_var,font=("times new roman",15,"bold"),bd=5,relief=GROOVE)
        entry3.grid(row=3, column=1,pady=10,padx=20,sticky="w")
        entry4 = Entry(Manage_Frame,textvariable=self.AMOUNT_var,font=("times new roman",15,"bold"),bd=5,relief=GROOVE)
        entry4.grid(row=4, column=1,pady=10,padx=20,sticky="w")
        entry5 = Entry(Manage_Frame,textvariable=self.MATURITY_var,font=("times new roman",15,"bold"),bd=5,relief=GROOVE)
        entry5.grid(row=5, column=1,pady=10,padx=20,sticky="w")
        entry6 = Entry(Manage_Frame,textvariable=self.DUE_DATE_var,font=("times new roman",15,"bold"),bd=5,relief=GROOVE)
        entry6.grid(row=6, column=1,pady=10,padx=20,sticky="w")
        entry7 = Entry(Manage_Frame,textvariable=self.ACC_NO_var,font=("times new roman",15,"bold"),bd=5,relief=GROOVE)
        entry7.grid(row=7, column=1,pady=10,padx=20,sticky="w")
        # button frames==================================================================
        btn_Frame = Frame(Manage_Frame, bd=0, relief=RIDGE, bg="crimson")
        btn_Frame.place(x=15, y=480, width=420)

        Addbtn=Button(btn_Frame,text="ADD",width=10,command=self.add_fd).grid(row=0, column=0,pady=10,padx=10)
        updatebtn = Button(btn_Frame, text="UPDATE", width=10,command=self.update_data).grid(row=0, column=1, pady=10, padx=10)
        deletebtn = Button(btn_Frame, text="DELETE", width=10,command=self.delete_data).grid(row=0, column=2, pady=10, padx=10)
        clearbtn = Button(btn_Frame, text="CLEAR", width=10,command=self.clear).grid(row=0, column=3, pady=10, padx=10)

        # detail frames==================================================================

        Detail_Frame = Frame(self.root, bd=4, relief=RIDGE, bg="crimson")
        Detail_Frame.place(x=500, y=100, width=800, height=570)

        lbl_search = Label(Detail_Frame, text="Search By", bg="crimson", fg="white", font=("times new roman", 20, "bold"))
        lbl_search.grid(row=0, column=0, pady=10, padx=20, sticky="w")

        search = ttk.Combobox(Detail_Frame,width=15,textvariable=self.search_by, font=("times new roman", 15, "bold"), state="readonly")
        search['values'] = ("BANK_NAME", "ISSUE_DATE","NAME","AMOUNT","MATURITY","DUE_DATE","ACC_NO")
        search.grid(row=0, column=1, pady=10, padx=20, sticky="w")

        txt_search = Entry(Detail_Frame,width=15,textvariable=self.search_txt, font=("times new roman", 15, "bold"), bd=5, relief=GROOVE)
        txt_search.grid(row=0, column=2, pady=10, padx=20, sticky="w")

        searchbtn = Button(Detail_Frame, text="SEARCH", width=10,command=self.search_data).grid(row=0, column=3, pady=10, padx=10)
        showallbtn = Button(Detail_Frame, text="SHOW ALL", width=10,command=self.fetch_data).grid(row=0, column=4, pady=10, padx=10)
        # table frames==================================================================
        Table_Frame = Frame(Detail_Frame, bd=4, relief=RIDGE, bg="crimson")
        Table_Frame.place(x=10, y=70, width=760, height=480)

        scroll_x = Scrollbar(Table_Frame, orient=HORIZONTAL)
        scroll_y = Scrollbar(Table_Frame, orient=VERTICAL)
        self.FD_table=ttk.Treeview(Table_Frame,columns=("BANK_NAME", "ISSUE_DATE","NAME","AMOUNT","MATURITY","DUE_DATE","ACC_NO"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_x.config(command=self.FD_table.xview)
        scroll_y.config(command=self.FD_table.yview)
        self.FD_table.heading("BANK_NAME",text="BANK_NAME")
        self.FD_table.heading("ISSUE_DATE", text="ISSUE_DATE")
        self.FD_table.heading("NAME", text="NAME")
        self.FD_table.heading("AMOUNT", text="AMOUNT")
        self.FD_table.heading("MATURITY", text="MATURITY")
        self.FD_table.heading("DUE_DATE", text="DUE_DATE")
        self.FD_table.heading("ACC_NO", text="ACC_NO")
        self.FD_table['show']='headings'
        self.FD_table.column("BANK_NAME", width=150)
        self.FD_table.column("ISSUE_DATE", width=100)
        self.FD_table.column("NAME", width=150)
        self.FD_table.column("AMOUNT", width=100)
        self.FD_table.column("MATURITY", width=100)
        self.FD_table.column("DUE_DATE",width=100)
        self.FD_table.column("ACC_NO", width=200)
        self.FD_table.bind("<ButtonRelease-1>",self.get_cursor)
        self.FD_table.pack(fill=BOTH,expand=1)
        self.fetch_data()
    def add_fd(self):
        if (self.BANK_NAME_var.get()=="" or
                self.ISSUE_DATE_var.get()==""
                or self.NAME_var.get()=="" or
                self.AMOUNT_var.get()=="" or
                self.MATURITY_var.get()=="" or
                self.DUE_DATE_var.get()=="" or
                self.ACC_NO_var.get()=="" ):
            messagebox.showerror("Error","All fields are required!")
        else:
            con=pymysql.connect(host="localhost",user="root",password="desai",database="fdd")
            cur=con.cursor()
            cur.execute(" insert into fdd values(%s,%s,%s,%s,%s,%s,%s)",( self.BANK_NAME_var.get(),
            self.ISSUE_DATE_var.get(),
            self.NAME_var.get(),
            self.AMOUNT_var.get(),
            self.MATURITY_var.get(),
            self.DUE_DATE_var.get(),
            self.ACC_NO_var.get(),

            ))
            con.commit()
            self.fetch_data()
            self.clear()
            con.close()
            7

    def fetch_data(self):
        con = pymysql.connect(host="localhost", user="root", password="desai", database="fdd")
        cur = con.cursor()
        cur.execute("select * from fdd")
        rows=cur.fetchall()
        if len(rows)!=0:
            self.FD_table.delete(*self.FD_table.get_children())
            for row in rows:
                self.FD_table.insert('',END,values=row)
            con.commit()
        con.close()
    def clear(self):
        self.BANK_NAME_var.set("")
        self.ISSUE_DATE_var.set("")
        self.NAME_var.set("")
        self.AMOUNT_var.set("")
        self.MATURITY_var.set("")
        self.DUE_DATE_var.set("")
        self.ACC_NO_var.set("")
    def get_cursor(self,ev):
        cursor_row=self.FD_table.focus()
        content=self.FD_table.item(cursor_row)
        row=content["values"]
        self.BANK_NAME_var.set(row[0])
        self.ISSUE_DATE_var.set(row[1])
        self.NAME_var.set(row[2])
        self.AMOUNT_var.set(row[3])
        self.MATURITY_var.set(row[4])
        self.DUE_DATE_var.set(row[5])
        self.ACC_NO_var.set(row[6])
    def update_data(self):
        con=pymysql.connect(host="localhost",user="root",password="desai",database="fdd")
        cur=con.cursor()
        cur.execute(" update fdd set bank_name=%s,issue_date=%s,name=%s,amount=%s,maturity=%s,due_date=%s where acc_no=%s",( self.BANK_NAME_var.get(),
        self.ISSUE_DATE_var.get(),
        self.NAME_var.get(),
        self.AMOUNT_var.get(),
        self.MATURITY_var.get(),
        self.DUE_DATE_var.get(),
        self.ACC_NO_var.get(),

        ))
        con.commit()
        self.fetch_data()
        self.clear()
        con.close()
        messagebox.showinfo("Success"," Record has been Updated")
    def delete_data(self):
        con = pymysql.connect(host="localhost", user="root", password="desai", database="fdd")
        cur = con.cursor()
        cur.execute("delete from fdd where acc_no=%s",self.ACC_NO_var.get())
        con.commit()
        con.close()
        self.fetch_data()
        self.clear()
        messagebox.showinfo("Success", "Record has been deleted")
    def search_data(self):
        if self.search_txt.get()=="":
            messagebox.showinfo("Error", "field is empty")

        else:
            con = pymysql.connect(host="localhost", user="root", password="desai", database="fdd")
            cur = con.cursor()
            cur.execute("select * from fdd where "+str(self.search_by.get())+" LIKE '%"+str(self.search_txt.get())+"%'")
            rows=cur.fetchall()
            print(rows)
            if rows==():
                a=str(self.search_by.get())
                b=str(self.search_txt.get())
                c= a +" :- " + b +" dosen't exist"
                messagebox.showinfo("Error",c)

            if len(rows)!=0:
                self.FD_table.delete(*self.FD_table.get_children())
                for row in rows:
                    self.FD_table.insert('',END,values=row)
                con.commit()
            con.close()

root=Tk()
ob=Student(root)
root.mainloop()