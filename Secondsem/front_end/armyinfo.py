from tkinter import*
from tkinter import ttk
from Secondsem.back_end.conarmyinfo import *
from Secondsem.model.info import *
from tkinter import messagebox

class armyinfo:
    def __init__(self,root):
        self.root=root
        self.root.title("Army Info Management")
        self.root.geometry("1600x800+70+30")
        self.root.iconbitmap("armym.ico.ico")

        # self.dbconnect = DbConnection()
        self.dbconnect = DbConnection()

        title=Label(self.root,text="Army management system",bd=10,relief=GROOVE,font=("times new roman",40,"bold"),bg="black",fg='white')
        title.pack(side=TOP,fill=X)


        global a
        a = PhotoImage(file="12.png")
        self.root.background = Label(self.root, image=a)
        self.root.background.place(x=0, y=80)

#====================================all varaiables===============================================
        self.Citizenship_No_var=StringVar()
        self.name_var=StringVar()
        self.Camp_ID_var=StringVar()
        self.gender_var=StringVar()
        self.contact_var=StringVar()
        self.height_var=StringVar()
        self.post_var=StringVar()
        self.search_by=StringVar()
        self.search_txt=StringVar()
#===================================================== first frme ho================================================================

        Manage_Frame=Frame(self.root,bd=5,relief=RIDGE,bg='dark green')
        Manage_Frame.place(x=70,y=150,width=470,height=580)

        m_title = Label(Manage_Frame, text='Manage Soldiers', bg='green', fg='white', font=("arail", 20, 'bold'))
        m_title.grid(row=0,columnspan=2,pady=20)
#================================================label ==========================================================================:
        lbl_first=Label(Manage_Frame, text='Citizenship No', bg='green', fg='white', font=("arail", 15, 'bold'))
        lbl_first.grid(row=1,column=0,pady=10,padx=10,sticky='w')

        txt_first=Entry(Manage_Frame,textvariable=self.Citizenship_No_var, font=("arail", 15, 'bold'),bd=5,relief=GROOVE)
        txt_first.grid(row=1,column=1,pady=10,padx=10,sticky='w')

        lbl_second = Label(Manage_Frame, text='Name', bg='green', fg='white', font=("arail", 15, 'bold'))
        lbl_second.grid(row=2, column=0, pady=10, padx=10, sticky='w')

        txt_second = Entry(Manage_Frame,textvariable=self.name_var, font=("arail", 15, 'bold'), bd=5, relief=GROOVE)
        txt_second.grid(row=2, column=1, pady=10, padx=10, sticky='w')

        lbl_third = Label(Manage_Frame, text='Camp ID', bg='green', fg='white', font=("arail", 15, 'bold'))
        lbl_third.grid(row=3, column=0, pady=10, padx=10, sticky='w')

        txt_third = Entry(Manage_Frame,textvariable=self.Camp_ID_var, font=("arail", 15, 'bold'), bd=5, relief=GROOVE)
        txt_third.grid(row=3, column=1, pady=10, padx=10, sticky='w')

        lbl_fourth = Label(Manage_Frame, text='Gender', bg='green', fg='white', font=("arail", 15, 'bold'))
        lbl_fourth.grid(row=4, column=0, pady=10, padx=10, sticky='w')

        combo_fourth=ttk.Combobox(Manage_Frame,textvariable=self.gender_var,font=('arial',14,'bold'),state='readonly')
        combo_fourth['values']=('Male','Female','Other')
        combo_fourth.grid(row=4,column=1,padx=7, pady=10)

        lbl_five = Label(Manage_Frame, text='Contact', bg='green', fg='white', font=("arail", 15, 'bold'))
        lbl_five.grid(row=5, column=0, pady=10, padx=10, sticky='w')

        txt_five = Entry(Manage_Frame,textvariable=self.contact_var, font=("arail", 15, 'bold'), bd=5, relief=GROOVE)
        txt_five.grid(row=5, column=1, pady=10, padx=10, sticky='w')

        lbl_six = Label(Manage_Frame, text='Height', bg='green', fg='white', font=("arail", 15, 'bold'))
        lbl_six.grid(row=6, column=0, pady=10, padx=10, sticky='w')

        txt_six = Entry(Manage_Frame,textvariable=self.height_var, font=("arail", 15, 'bold'), bd=5, relief=GROOVE)
        txt_six.grid(row=6, column=1, pady=10, padx=10, sticky='w')

        lbl_sev = Label(Manage_Frame, text='Post', bg='green', fg='white', font=("arail", 15, 'bold'))
        lbl_sev.grid(row=7, column=0, pady=10, padx=10, sticky='w')

        txt_sev = Entry(Manage_Frame,textvariable=self.post_var, font=("arail", 15, 'bold'), bd=5, relief=GROOVE)
        txt_sev.grid(row=7, column=1, pady=10, padx=10, sticky='w')

#=================================button haru==
        btn_Frame=Frame(Manage_Frame,bd=4,relief=RIDGE,bg="green")
        btn_Frame.place(x=15,y=490,width=440)

        Addbtn=Button(btn_Frame,text="Add",command=self.add,width=10).grid(row=0,column=0,padx=3,pady=10)
        updatebtn=Button(btn_Frame, text="Update",command=self.update, width=10).grid(row=0, column=1, padx=3, pady=10)
        deletebtn=Button(btn_Frame, text="Delete",command=self.delete ,width=10).grid(row=0, column=2, padx=3, pady=10)
        clearbtn=Button(btn_Frame, text="Clear",command=self.clear, width=10).grid(row=0, column=3, padx=3, pady=10)
        exitbtn = Button(btn_Frame, text="Exit", command=self.exit, width=10).grid(row=0, column=4, padx=3, pady=10)

#=============================================detail frame=================================================================
        Detail_Frame = Frame(self.root, bd=5, relief=RIDGE, bg='dark green')
        Detail_Frame.place(x=650, y=110, width=900, height=630)

        lbl_search=Label(Detail_Frame, text='Search By:>', bg='green', fg='white', font=("arail", 15, 'bold'))
        lbl_search.grid(row=0, column=0, pady=10, padx=10, sticky='w')

        combo_search = ttk.Combobox(Detail_Frame,text=self.search_by,width=10, font=('arial', 14, 'bold'), state='readonly')
        combo_search['values'] = ('Citizenship_No')
        combo_search.grid(row=0, column=1, padx=20, pady=10)

        txt_Search=Entry(Detail_Frame,text=self.search_txt, font=("arail", 13, 'bold'), bd=5, relief=GROOVE)
        txt_Search.grid(row=0, column=2, pady=10, padx=10, sticky='w')

        searchbtn=Button(Detail_Frame, text="Search",command=self.search_data, width=10,pady=5).grid(row=0, column=3, padx=20, pady=10)
        showallbtn=Button(Detail_Frame, text="Show All",command=self.fetch,width=10,pady=5).grid(row=0,column=4,padx=20,pady=10)

#=========================sorting============================================

        lbl_sort = Label(Detail_Frame, text="Sort By:",bg='green',fg='white', font=("arial", 13, "bold"), )
        lbl_sort.place(x=10, y=50)

        self.combo_sort = ttk.Combobox(Detail_Frame, width=12, font=("arial", 12, "bold"), state="readonly")
        self.combo_sort['values'] = ("Ascending", "Descending")
        self.combo_sort.place(x=160, y=50)
        sortbtn = Button(Detail_Frame, text="Sort", width=8, pady=1,
                         command=self.sort).place(x=320, y=50)

#===================================table frame================================================
        Table_Frame=Frame(Detail_Frame,bd=4,relief=RIDGE,bg='blue')
        Table_Frame.place(x=20,y=80,width=850,height=540)

#=========================================for scrollbutton==============================================================
        scroll_x=Scrollbar(Table_Frame,orient=HORIZONTAL)
        scroll_y=Scrollbar(Table_Frame,orient=VERTICAL)
        self.armyinfo_table=ttk.Treeview(Table_Frame,columns=("citizenship no","name","Camp ID","gender","contact","height","post"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=self.armyinfo_table.xview)
        scroll_y.config(command=self.armyinfo_table.yview)

#=========================================== heading============================================================
        self.armyinfo_table.heading("citizenship no",text="Citizenship No")
        self.armyinfo_table.heading("name", text="Name")
        self.armyinfo_table.heading("Camp ID", text="Camp ID")
        self.armyinfo_table.heading("gender", text="Gender")
        self.armyinfo_table.heading("contact", text="Contact")
        self.armyinfo_table.heading("height", text="Height")
        self.armyinfo_table.heading("post", text="Post")
        self.armyinfo_table['show']='headings'
        self.armyinfo_table.column("citizenship no",width=110)
        self.armyinfo_table.column("name", width=110)
        self.armyinfo_table.column("Camp ID", width=110)
        self.armyinfo_table.column("gender", width=110)
        self.armyinfo_table.column("contact", width=110)
        self.armyinfo_table.column("height", width=110)
        self.armyinfo_table.column("post", width=110)
        self.armyinfo_table.pack(fill=BOTH,expand=1)
        self.armyinfo_table.bind("<ButtonRelease-1>",self.get_cursor)
        self.fetch()

    def get_cursor(self, ev):
            curosor_row = self.armyinfo_table.focus()
            contents = self.armyinfo_table.item(curosor_row)
            row = contents['values']

            self.Citizenship_No_var.set(row[0])
            self.name_var.set(row[1])
            self.Camp_ID_var.set(row[2])
            self.gender_var.set(row[3])
            self.contact_var.set(row[4])
            self.height_var.set(row[5])
            self.post_var.set(row[6])

    def add(self):
        if self.Citizenship_No_var.get()=="" or self.name_var.get()=="" or self.Camp_ID_var.get=="" or self.gender_var.get()=="" or\
                self.contact_var.get()=="" or self.height_var.get()=="" or self.post_var.get()=="":
            messagebox.showerror("Error","Sabai value hala")

        else:
            info_obj=info(self.Citizenship_No_var.get(),self.name_var.get(),self.Camp_ID_var.get(),self.gender_var.get()
                           ,self.contact_var.get(),self.height_var.get(),self.post_var.get())
            query='insert into info values(%s,%s,%s,%s,%s,%s,%s);'
            values=(int(info_obj.get_Citizenship_No()),info_obj.get_name(),info_obj.get_Camp_ID(),info_obj.get_gender()
                    ,info_obj.get_contact(),info_obj.get_height(),info_obj.get_post())
            self.dbconnect.insert(query,values)
            messagebox.showinfo('sucess','Army information inserted sucessfully')
            self.fetch()
            self.Citizenship_No_var.set("")
            self.name_var.set("")
            self.Camp_ID_var.set("")
            self.gender_var.set("")
            self.contact_var.set("")
            self.height_var.set("")
            self.post_var.set("")

    def fetch(self):
        query="select * from info"
        rows=self.dbconnect.select1(query)
        if rows!=0:
            self.armyinfo_table.delete(*self.armyinfo_table.get_children())
            for row in rows:
                self.armyinfo_table.insert('',END,values=row)
            self.dbconnect.fetch(query)

    def search_data(self):
        query = " select * from info where Citizenship_No = %s; "
        records = self.dbconnect.select2(query,(self.search_txt.get(),))
        data_list = []
        for row in records:
            data_list.append(row[0])
        ans = self.linear_search(data_list, str(self.search_txt.get()))
        print(f"this is linear data{ans}")

        if ans:
            messagebox.showinfo('Success', 'congrats Citizenship No exists in this list')
            query1 = "select * from info where Citizenship_No=%s;"
            values1 = (ans,)
            records1 = self.dbconnect.select2(query1, values1)
            if len(records1) != 0:
                self.armyinfo_table.delete(*self.armyinfo_table.get_children())
                for row in records1:
                    self.armyinfo_table.insert('', END, values=row)


    @classmethod
    def linear_search(cls,data, item):
        for i in range(len(data)):
            if data[i] == item:
                return data[i]
        return False



    @classmethod
    def mergesort(cls, order, ascending=True):
        list = []
        if len(order) == 1:
            return order

        mit = len(order) // 2

        first_section = cls.mergesort(order[:mit])
        second_section = cls.mergesort(order[mit:])

        x = 0
        y = 0
        while x < len(first_section) and y < len(second_section):
            if first_section[x] > second_section[y]:
                list.append(second_section[y])
                y = y + 1

            else:
                list.append(first_section[x])
                x = x + 1

        conclusion = list + first_section[x:]
        conclusion = conclusion + second_section[y:]

        if ascending == True:
            return conclusion

        else:
            conclusion.reverse()
            return conclusion

    def sort(self):
        sortby = self.combo_sort.get()
        query = 'select * from info'
        value_fetch = self.dbconnect.select1(query)
        if sortby == 'Ascending':
            row = self.mergesort(value_fetch, True)
            messagebox.showinfo("Sorted","your data has been shorted in ascending order")

        elif sortby == 'Descending':
            row = self.mergesort(value_fetch, False)
            messagebox.showinfo("Sorted", "your data has been shorted in descending order")

        else:
            row = []

        if len(row) != 0:
            self.armyinfo_table.delete(
                *self.armyinfo_table.get_children())
            for rows in row:
                self.armyinfo_table.insert('', END, values=rows)

    def update(self):
        info_obj=info(self.Citizenship_No_var.get(),self.name_var.get(),self.Camp_ID_var.get(),self.gender_var.get()
                       ,self.contact_var.get(),self.height_var.get(),self.post_var.get())
        query='update info set  name=%s, Camp_ID=%s, gender=%s, contact=%s, height=%s,post=%s where Citizenship_No=%s;'
        Citizenship_No=self.Citizenship_No_var.get()
        name=self.name_var.get()
        Camp_ID=self.Camp_ID_var.get()
        gender=self.gender_var.get()
        contact=self.contact_var.get()
        height=self.height_var.get()
        post=self.post_var.get()
        values=(name,Camp_ID,gender,contact,height,post,Citizenship_No)
        self.dbconnect.update(query,values)
        messagebox.showinfo('sucess', 'data updated sucessfully')
        self.fetch()
        self.Citizenship_No_var.set("")
        self.name_var.set("")
        self.Camp_ID_var.set("")
        self.gender_var.set("")
        self.contact_var.set("")
        self.height_var.set("")
        self.post_var.set("")

    def clear(self):
        self.Citizenship_No_var.set("")
        self.name_var.set("")
        self.Camp_ID_var.set("")
        self.gender_var.set("")
        self.contact_var.set("")
        self.height_var.set("")
        self.post_var.set("")
        messagebox.showinfo("success","values cleared")


    def delete(self):
        query = "delete from info where Citizenship_No=%s;"
        id = self.Citizenship_No_var.get()
        value = (id,)
        self.dbconnect.delete(query, value)
        messagebox.showinfo("Success", "Data deleted successfully")
        self.fetch()
        self.Citizenship_No_var.set("")
        self.name_var.set("")
        self.Camp_ID_var.set("")
        self.gender_var.set("")
        self.contact_var.set("")
        self.height_var.set("")
        self.post_var.set("")


    def exit(self):
        self.root.destroy()

#
# root=Tk()
# ob=armyinfo(root)
# root.mainloop()
