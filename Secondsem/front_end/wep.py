from tkinter import*
from tkinter import ttk
from Secondsem.back_end.conarmyinfo import *
from Secondsem.model.weap import *
from tkinter import messagebox


class wep:
    def __init__(self,root):
        self.root=root
        self.root.title("Weapons Management")
        self.root.geometry("1500x900+100+30")
        self.root.iconbitmap("rr.ico.ico")

        title=Label(self.root,text="Weapons management",bd=10,relief=GROOVE,font=("times new roman",40,"bold"),bg="blue",fg='white')
        title.pack(side=TOP,fill=X)
#connection============================================================================================================================================
        self.dbconnect = DbConnection()
#variable===============================================================================================================================================
        self.Weapon_type_var = StringVar()
        self.Weapon_Name_var = StringVar()
        self.Weapon_No_var = StringVar()
        self.Bullet_qty_var = StringVar()
        self.search_by = StringVar()
        self.search_txt = StringVar()
        self.sort_by=StringVar()
        self.sort_txt=StringVar()

#image for background=================================================================================================================================
        global c
        c = PhotoImage(file="5.png")
        self.root.background = Label(self.root, image=c)
        self.root.background.place(x=0, y=80)
#firstframe=========================================================================================================================================
        Manage_Frame = Frame(self.root, bd=5, relief=RIDGE, bg='dark red')
        Manage_Frame.place(x=50, y=170, width=470, height=400)
        m_title = Label(Manage_Frame, text='Manage Weapons', bg='grey', fg='white', font=("arail", 20, 'bold'))
        m_title.grid(row=0, columnspan=2, pady=20)
#=============================================labels ==========================:
        lbl_zero = Label(Manage_Frame, text='Weapon Type', bg='grey', fg='white', font=("arail", 15, 'bold'))
        lbl_zero.grid(row=1, column=0, pady=10, padx=10, sticky='w')

        combo_zero = ttk.Combobox(Manage_Frame, textvariable=self.Weapon_type_var, font=('arial', 14, 'bold'),
                                    state='readonly')
        combo_zero['values'] = ('AR', 'Sniper', 'SMG','LMG','Grenade','Air','Land')
        combo_zero.grid(row=1, column=1, padx=7, pady=10)

        lbl_first = Label(Manage_Frame, text='Weapon Name', bg='grey', fg='white', font=("arail", 15, 'bold'))
        lbl_first.grid(row=2, column=0, pady=10, padx=10, sticky='w')

        txt_first = Entry(Manage_Frame, textvariable=self.Weapon_Name_var, font=("arail", 15, 'bold'), bd=5, relief=GROOVE)
        txt_first.grid(row=2, column=1, pady=10, padx=10, sticky='w')

        lbl_second = Label(Manage_Frame, text='Weapon No', bg='grey', fg='white', font=("arail", 15, 'bold'))
        lbl_second.grid(row=3, column=0, pady=10, padx=10, sticky='w')

        txt_second = Entry(Manage_Frame, textvariable=self.Weapon_No_var, font=("arail", 15, 'bold'), bd=5,
                           relief=GROOVE)
        txt_second.grid(row=3, column=1, pady=10, padx=10, sticky='w')

        lbl_third = Label(Manage_Frame, text='Bullet Qty', bg='grey', fg='white', font=("arail", 15, 'bold'))
        lbl_third.grid(row=4, column=0, pady=10, padx=10, sticky='w')

        txt_third = Entry(Manage_Frame, textvariable=self.Bullet_qty_var, font=("arail", 15, 'bold'), bd=5, relief=GROOVE)
        txt_third.grid(row=4, column=1, pady=10, padx=10, sticky='w')

#================================= ===button inside first frame============================================================
        btn_Frame = Frame(Manage_Frame, bd=4, relief=RAISED, bg="green")
        btn_Frame.place(x=10, y=300, width=440)

        Addbtn = Button(btn_Frame, text="Add",command=self.add ,width=10).grid(row=0, column=0,padx=3, pady=10)
        updatebtn = Button(btn_Frame, text="Update",command=self.update ,width=10).grid(row=0, column=1,padx=3, pady=10)
        deletebtn = Button(btn_Frame, text="Delete",command=self.delete, width=10).grid(row=0, column=2,padx=3,pady=10)
        clearbtn = Button(btn_Frame, text="Clear",command=self.clear, width=10).grid(row=0, column=3,padx=3, pady=10)
        exitbtn=Button(btn_Frame,text="Exit",command=self.exit,width=10).grid(row=0,column=4,padx=3,pady=10)

# ===================detail frame or second frame============================================================
        Detail_Frame = Frame(self.root, bd=5, relief=RIDGE, bg='brown')
        Detail_Frame.place(x=570, y=110, width=760, height=610)

        lbl_search = Label(Detail_Frame, text='Search By:>', bg='brown', fg='white', font=("arail", 15, 'bold'))
        lbl_search.grid(row=0, column=0, pady=5, padx=5, sticky='w')

        combo_search = ttk.Combobox(Detail_Frame, text=self.search_by, width=10, font=('arial', 14, 'bold'),
                                    state='readonly')
        combo_search['values'] = ( 'Weapon_No')
        combo_search.grid(row=0, column=1, padx=10, pady=5)

        txt_Search = Entry(Detail_Frame, text=self.search_txt, font=("arail", 13, 'bold'), bd=5, relief=GROOVE)
        txt_Search.grid(row=0, column=2, pady=5, padx=5, sticky='w')

        searchbtn = Button(Detail_Frame, text="Search",command=self.search_data, width=10, pady=5).grid(row=0, column=3, padx=5, pady=5)
        showallbtn = Button(Detail_Frame, text="Show All",command=self.fetch, width=10, pady=5).grid(row=0, column=4, padx=5, pady=5)


#===============================sorting==============================================================================
        lbl_sort = Label(Detail_Frame, text="Sort By:", bg='brown', fg='white', font=("arial", 13, "bold"), )
        lbl_sort.place(x=10, y=50)

        self.combo_sort = ttk.Combobox(Detail_Frame, width=12, font=("arial", 12, "bold"), state="readonly")
        self.combo_sort['values'] = ("Ascending", "Descending")
        self.combo_sort.place(x=160, y=50)
        sortbtn = Button(Detail_Frame, text="Sort", width=8, pady=1,
                         command=self.sort).place(x=320, y=50)

        # ========================view table frame for show of data added to database=================================================================
        Table_Frame = Frame(Detail_Frame, bd=4, relief=RIDGE, bg='blue')
        Table_Frame.place(x=15, y=90, width=720, height=490)

#=========================== scrollbutton inside viewtable====================================================================================
        scroll_x = Scrollbar(Table_Frame, orient=HORIZONTAL)
        scroll_y = Scrollbar(Table_Frame, orient=VERTICAL)
        self.wep_table = ttk.Treeview(Table_Frame, columns=(
        "Weapon Type", "Weapon Name", "Weapon No", "Bullet Qty"), xscrollcommand=scroll_x.set,
                                       yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_x.config(command=self.wep_table.xview)
        scroll_y.config(command=self.wep_table.yview)

 #=======================inside frame heading=========================================================================
        self.wep_table.heading("Weapon Type", text="Weapon Type")
        self.wep_table.heading("Weapon Name", text="Weapon Name")
        self.wep_table.heading("Weapon No", text="Weapon No")
        self.wep_table.heading("Bullet Qty", text="Bullet Qty")
        self.wep_table['show'] = 'headings'
        self.wep_table.column("Weapon Type", width=110)
        self.wep_table.column("Weapon Name", width=110)
        self.wep_table.column("Weapon No", width=110)
        self.wep_table.column("Bullet Qty", width=110)

        self.wep_table.pack(fill=BOTH, expand=1)
        self.wep_table.bind("<ButtonRelease-1>", self.get_cursor)
        self.fetch()
#========================functions========================================================================================

    def get_cursor(self, ev):
        curosor_row = self.wep_table.focus()
        contents = self.wep_table.item(curosor_row)
        row = contents['values']

        self.Weapon_type_var.set(row[0])
        self.Weapon_Name_var.set(row[1])
        self.Weapon_No_var.set(row[2])
        self.Bullet_qty_var.set(row[3])

    def add(self):
        if self.Weapon_type_var.get()=="" or self.Weapon_Name_var.get()=="" or self.Weapon_No_var.get()=="" or self.Bullet_qty_var.get()=="":
            messagebox.showerror("Cannot add null values"," Please fill all the data")
        else:
            wep_obj = weap(self.Weapon_type_var.get(), self.Weapon_Name_var.get(),
                            self.Weapon_No_var.get(), self.Bullet_qty_var.get())

            query = 'insert into wep values(%s,%s,%s,%s);'
            values = (wep_obj.get_Weapon_type(), wep_obj.get_Weapon_Name(), int(wep_obj.get_Weapon_No()), wep_obj.get_Bullet_qty())

            self.dbconnect.insert(query, values)
            messagebox.showinfo('Success', 'Congratulations wep details has been added ')
            self.fetch()
            self.Weapon_Name_var.set("")
            self.Weapon_type_var.set("")
            self.Weapon_No_var.set("")
            self.Bullet_qty_var.set("")

    def fetch(self):
        query = "select * from wep"
        rows = self.dbconnect.select1(query)
        if rows != 0:
            self.wep_table.delete(*self.wep_table.get_children())
            for row in rows:
                self.wep_table.insert('', END, values=row)
            self.dbconnect.fetch(query)


    def search_data(self):
        query = " select * from wep where Weapon_No = %s; "
        records = self.dbconnect.select2(query, (self.search_txt.get(),))
        data_list = []
        for row in records:
            data_list.append(row[2])
        ans = self.linear_search(data_list, int(self.search_txt.get()))
        print(f"this is linear data{ans}")

        if ans:
            messagebox.showinfo('Success', 'congrats this weapon no exists in this list')
            query1 = "select * from wep where Weapon_No=%s;"
            values1 = (ans,)
            records1 = self.dbconnect.select2(query1, values1)
            if len(records1) != 0:
                self.wep_table.delete(*self.wep_table.get_children())
                for row in records1:
                    self.wep_table.insert('', END, values=row)

    @classmethod
    def linear_search(cls, data, item):
        for i in range(len(data)):
            if data[i] == item:
                return data[i]
        return False

    @classmethod
    def mergesort(self, order, ascending=True):
        list = []
        if len(order) == 1:
            return order
        mit = len(order) // 2
        first_section = self.mergesort(order[:mit])
        second_section = self.mergesort(order[mit:])
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
        query = 'select * from wep'
        value_fetch = self.dbconnect.select1(query)
        if sortby == 'Ascending':
            row = self.mergesort(value_fetch, True)
            messagebox.showinfo("Sucess","Data has been shorted in ascending order")
        elif sortby == 'Descending':
            row = self.mergesort(value_fetch, False)
            messagebox.showinfo("Sucess","Data has been shorted in descending")
        else:
            row = []

        if len(row) != 0:
            self.wep_table.delete(
                *self.wep_table.get_children())
            for rows in row:
                self.wep_table.insert('', END, values=rows)



    def update(self):
        wep_obj =weap(self.Weapon_type_var.get(), self.Weapon_Name_var.get(),
                        self.Weapon_No_var.get(), self.Bullet_qty_var.get())
        query = 'update wep set  Weapon_type=%s,  Weapon_Name=%s,Bullet_qty=%s where Weapon_No=%s;'
        Weapon_Name = self.Weapon_Name_var.get()
        Weapon_type = self.Weapon_type_var.get()
        Weapon_No = self.Weapon_No_var.get()
        Bullet_qty = self.Bullet_qty_var.get()

        values = (Weapon_type, Weapon_Name, Bullet_qty, Weapon_No)
        self.dbconnect.update(query, values)
        messagebox.showinfo('success', 'your data has been updated successfully')
        self.fetch()

    def clear(self):
        self.Weapon_type_var.set("")
        self.Weapon_Name_var.set("")
        self.Weapon_No_var.set("")
        self.Bullet_qty_var.set("")
        messagebox.showinfo("Clear","Data clear")

    def delete(self):
        query = "delete from wep where Weapon_No=%s;"
        id = self.Weapon_No_var.get()
        value = (id,)
        self.dbconnect.delete(query, value)
        messagebox.showinfo("Success", "Data deleted successfully")
        self.fetch()

    def exit(self):
        self.root.destroy()

# root=Tk()
# ob=wep(root)
# root.mainloop()

