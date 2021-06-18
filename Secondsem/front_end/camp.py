from tkinter import*
from tkinter import ttk
from tkinter import messagebox
from Secondsem.back_end.conarmyinfo import *
from Secondsem.model.campp import *

class camp:
    def __init__(self,root):
        self.root=root
        self.root.title("Camp Management")
        self.root.geometry("1450x850+200+50")
        self.root.iconbitmap("camm.ico.ico")

        title=Label(self.root,text="Camp management system",bd=10,relief=GROOVE,font=("times new roman",40,"bold"),bg="green",fg='white')
        title.pack(side=TOP,fill=X)

        self.dbconnect = DbConnection()
#===================bg====================
        global a
        a = PhotoImage(file="8.png")
        self.root.background = Label(self.root, image=a)
        self.root.background.place(x=0, y=80)

#============================all varaiables==
        self.Camp_ID_var=StringVar()
        self.Camp_Name_var=StringVar()
        self.Camp_No_var=StringVar()
        self.Title_var=StringVar()
        self.contact_var=StringVar()
        self.Tent_No_var=StringVar()
        self.address_var=StringVar()

        self.search_by=StringVar()
        self.search_txt=StringVar()
#==================================first frame==========================================

        Manage_Frame=Frame(self.root,bd=5,relief=RIDGE,bg='dark grey')
        Manage_Frame.place(x=20,y=140,width=470,height=580)

        m_title = Label(Manage_Frame, text='Manage Camp', bg='grey', fg='white', font=("arail", 20, 'bold'))
        m_title.grid(row=0,columnspan=2,pady=20)
#==========================labels of first frame ==========================:
        lbl_first=Label(Manage_Frame, text='Camp_ID.', bg='grey', fg='white', font=("arail", 15, 'bold'))
        lbl_first.grid(row=1,column=0,pady=10,padx=10,sticky='w')

        txt_first=Entry(Manage_Frame,textvariable=self.Camp_ID_var, font=("arail", 15, 'bold'),bd=5,relief=GROOVE)
        txt_first.grid(row=1,column=1,pady=10,padx=10,sticky='w')

        lbl_second = Label(Manage_Frame, text='Camp Name', bg='grey', fg='white', font=("arail", 15, 'bold'))
        lbl_second.grid(row=2, column=0, pady=10, padx=10, sticky='w')

        txt_second = Entry(Manage_Frame,textvariable=self.Camp_Name_var, font=("arail", 15, 'bold'), bd=5, relief=GROOVE)
        txt_second.grid(row=2, column=1, pady=10, padx=10, sticky='w')

        lbl_third = Label(Manage_Frame, text='Camp NO', bg='grey', fg='white', font=("arail", 15, 'bold'))
        lbl_third.grid(row=3, column=0, pady=10, padx=10, sticky='w')

        txt_third = Entry(Manage_Frame,textvariable=self.Camp_No_var, font=("arail", 15, 'bold'), bd=5, relief=GROOVE)
        txt_third.grid(row=3, column=1, pady=10, padx=10, sticky='w')

        lbl_fourth = Label(Manage_Frame, text='Title', bg='grey', fg='white', font=("arail", 15, 'bold'))
        lbl_fourth.grid(row=4, column=0, pady=10, padx=10, sticky='w')

        combo_fourth=ttk.Combobox(Manage_Frame,textvariable=self.Title_var,font=('arial',14,'bold'),state='readonly')
        combo_fourth['values']=('Defense','Sniper','Peace')
        combo_fourth.grid(row=4,column=1,padx=7, pady=10)


        lbl_five = Label(Manage_Frame, text='Contact', bg='grey', fg='white', font=("arail", 15, 'bold'))
        lbl_five.grid(row=5, column=0, pady=10, padx=10, sticky='w')

        txt_five = Entry(Manage_Frame,textvariable=self.contact_var, font=("arail", 15, 'bold'), bd=5, relief=GROOVE)
        txt_five.grid(row=5, column=1, pady=10, padx=10, sticky='w')

        lbl_six = Label(Manage_Frame, text='Tent No', bg='grey', fg='white', font=("arail", 15, 'bold'))
        lbl_six.grid(row=6, column=0, pady=10, padx=10, sticky='w')

        txt_six = Entry(Manage_Frame,textvariable=self.Tent_No_var, font=("arail", 15, 'bold'), bd=5, relief=GROOVE)
        txt_six.grid(row=6, column=1, pady=10, padx=10, sticky='w')

        lbl_sev = Label(Manage_Frame, text='Address', bg='grey', fg='white', font=("arail", 15, 'bold'))
        lbl_sev.grid(row=7, column=0, pady=10, padx=10, sticky='w')

        txt_sev = Entry(Manage_Frame,textvariable=self.address_var, font=("arail", 15, 'bold'), bd=5, relief=GROOVE)
        txt_sev.grid(row=7, column=1, pady=10, padx=10, sticky='w')

#=====================================button in frame===================================
        btn_Frame=Frame(Manage_Frame,bd=4,relief=RIDGE,bg="green")
        btn_Frame.place(x=15,y=490,width=440)

        Addbtn=Button(btn_Frame,text="Add",command=self.add,width=10).grid(row=0,column=0,padx=3,pady=10)
        updatebtn=Button(btn_Frame, text="Update",command=self.update, width=10).grid(row=0, column=1, padx=3, pady=10)
        deletebtn=Button(btn_Frame, text="Delete",command=self.delete, width=10).grid(row=0, column=2, padx=3, pady=10)
        clearbtn=Button(btn_Frame, text="Clear",command=self.clear, width=10).grid(row=0, column=3, padx=3, pady=10)
        exitbtn = Button(btn_Frame, text="Exit", command=self.exit, width=10).grid(row=0, column=4, padx=3, pady=10)

#=============================detail frame for second side ko==================================================================================
        Detail_Frame = Frame(self.root, bd=5, relief=RIDGE, bg='brown')
        Detail_Frame.place(x=530, y=100, width=890, height=700)

        lbl_search=Label(Detail_Frame, text='Search By:>', bg='brown', fg='white', font=("arail", 15, 'bold'))
        lbl_search.grid(row=0, column=0, pady=10, padx=10, sticky='w')

        combo_search = ttk.Combobox(Detail_Frame,text=self.search_by,width=10, font=('arial', 14, 'bold'), state='readonly')
        combo_search['values'] = ('Camp_ID')
        combo_search.grid(row=0, column=1, padx=20, pady=10)

        txt_Search=Entry(Detail_Frame,text=self.search_txt, font=("arail", 13, 'bold'), bd=5, relief=GROOVE)
        txt_Search.grid(row=0, column=2, pady=10, padx=10, sticky='w')

#========================btn========================================================================================================

        searchbtn=Button(Detail_Frame, text="Search",command=self.search_data, width=10,pady=5).grid(row=0, column=3, padx=10, pady=10)
        showallbtn=Button(Detail_Frame, text="Show All",command=self.fetch,width=10,pady=5).grid(row=0,column=4,padx=10,pady=10)

        lbl_sort = Label(Detail_Frame, text="Sort By:", font=("arial", 13, "bold"), )
        lbl_sort.place(x=10, y=45)
#===============================shorting=============================================================================================

        self.combo_sort = ttk.Combobox(Detail_Frame, width=12, font=("arial", 12, "bold"), state="readonly")
        self.combo_sort['values'] = ("Ascending", "Descending")
        self.combo_sort.place(x=160, y=45)

        sortbtn = Button(Detail_Frame, text="Sort", width=8, pady=1,
                         command=self.sort).place(x=320, y=45)

#===============================================table frame===================================================
        Table_Frame=Frame(Detail_Frame,bd=4,relief=RIDGE,bg='blue')
        Table_Frame.place(x=20,y=80,width=850,height=600)

#======================================scrollbutton ===============================================
        scroll_x=Scrollbar(Table_Frame,orient=HORIZONTAL)
        scroll_y=Scrollbar(Table_Frame,orient=VERTICAL)
        self.camp_table=ttk.Treeview(Table_Frame,columns=("Camp ID","Camp name","Camp No","Title","contact","Tent No","Address"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=self.camp_table.xview)
        scroll_y.config(command=self.camp_table.yview)

#==================================================frame  heading=============================
        self.camp_table.heading("Camp ID",text="Camp ID")
        self.camp_table.heading("Camp name", text="Camp Name")
        self.camp_table.heading("Camp No", text="Camp NO")
        self.camp_table.heading("Title", text="Title")
        self.camp_table.heading("contact", text="Contact")
        self.camp_table.heading("Tent No", text="TentNo")
        self.camp_table.heading("Address", text="Address")
        self.camp_table['show']='headings'
        self.camp_table.column("Camp ID",width=110)
        self.camp_table.column("Camp name", width=110)
        self.camp_table.column("Camp No", width=110)
        self.camp_table.column("Title", width=110)
        self.camp_table.column("contact", width=110)
        self.camp_table.column("Tent No", width=110)
        self.camp_table.column("Address", width=110)
        self.camp_table.pack(fill=BOTH,expand=1)
        self.camp_table.bind("<ButtonRelease-1>",self.get_cursor)
        self.fetch()

#============================function===================================
    def get_cursor(self, ev):
            curosor_row = self.camp_table.focus()
            contents = self.camp_table.item(curosor_row)
            row = contents['values']

            self.Camp_ID_var.set(row[0])
            self.Camp_Name_var.set(row[1])
            self.Camp_No_var.set(row[2])
            self.Title_var.set(row[3])
            self.contact_var.set(row[4])
            self.Tent_No_var.set(row[5])
            self.address_var.set(row[6])

    def add(self):
        if self.Camp_ID_var.get()=="" or self.Camp_Name_var.get()==""\
                or self.Camp_No_var.get()=="" or self.Title_var.get()=="" or self.Tent_No_var.get()=="" or self.contact_var.get()=="" or self.Tent_No_var.get()=="" or self.address_var.get()=="":
            messagebox.showerror("Error","All field are required")
        else:
            camp_obj=campp(self.Camp_ID_var.get(),self.Camp_Name_var.get(),self.Camp_No_var.get(),self.Title_var.get()
                           ,self.contact_var.get(),self.Tent_No_var.get(),self.address_var.get())
            query='insert into camp values(%s,%s,%s,%s,%s,%s,%s);'
            values=(int(camp_obj.get_Camp_ID()),camp_obj.get_Camp_Name(),camp_obj.get_Camp_No(),camp_obj.get_Title(),camp_obj.get_contact(),camp_obj.get_Tent_No(),camp_obj.get_address())
            self.dbconnect.insert(query,values)
            messagebox.showinfo('sucess','data inserted sucessfully')
            self.fetch()
            self.Camp_ID_var.set("")
            self.Camp_Name_var.set("")
            self.Camp_No_var.set("")
            self.Title_var.set("")
            self.contact_var.set("")
            self.Tent_No_var.set("")
            self.address_var.set("")

    def fetch(self):
        query="select * from camp"
        rows=self.dbconnect.select1(query)
        if rows!=0:
            self.camp_table.delete(*self.camp_table.get_children())
            for row in rows:
                self.camp_table.insert('',END,values=row)
            self.dbconnect.fetch(query)

    def search_data(self):
        query = " select * from camp where Camp_ID = %s; "
        records = self.dbconnect.select2(query, (self.search_txt.get(),))
        data_list = []
        for row in records:
            data_list.append(row[0])
        ans = self.linear_search(data_list, str(self.search_txt.get()))
        print(f"this is linear data{ans}")

        if ans:
            messagebox.showinfo('Success', 'oow this Camp ID  exists in this list')
            query1 = "select * from camp where Camp_ID=%s;"
            values1 = (ans,)
            records1 = self.dbconnect.select2(query1, values1)
            if len(records1) != 0:
                self.camp_table.delete(*self.camp_table.get_children())
                for row in records1:
                    self.camp_table.insert('', END, values=row)

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
        query = 'select * from camp'
        value_fetch = self.dbconnect.select1(query)
        if sortby == 'Ascending':
            row = self.mergesort(value_fetch, True)
            messagebox.showinfo("Sorted","Data sorted in ascending")


        elif sortby == 'Descending':
            row = self.mergesort(value_fetch, False)
            messagebox.showinfo('Sorted','Data sorted in descending ')

        else:
            row = []

        if len(row) != 0:
            self.camp_table.delete(
                *self.camp_table.get_children())
            for rows in row:
                self.camp_table.insert('', END, values=rows)






    def update(self):
        camp_obj=campp(self.Camp_ID_var.get(),self.Camp_Name_var.get(),self.Camp_No_var.get(),self.Title_var.get()
                       ,self.contact_var.get(),self.Tent_No_var.get(),self.address_var.get())
        query='update camp set  Camp_Name=%s, Camp_No=%s, Title=%s, contact=%s, Tent_No=%s,address=%s where Camp_ID=%s;'
        Camp_ID=self.Camp_ID_var.get()
        Camp_Name=self.Camp_Name_var.get()
        Camp_No=self.Camp_No_var.get()
        Title=self.Title_var.get()
        contact=self.contact_var.get()
        Tent_No=self.Tent_No_var.get()
        address=self.address_var.get()
        values=(Camp_Name,Camp_No,Title,contact,Tent_No,address,Camp_ID)
        self.dbconnect.update(query,values)
        messagebox.showinfo('sucess', 'data updated sucessfully')
        self.fetch()
        self.Camp_ID_var.set("")
        self.Camp_Name_var.set("")
        self.Camp_No_var.set("")
        self.Title_var.set("")
        self.contact_var.set("")
        self.Tent_No_var.set("")
        self.address_var.set("")

    def clear(self):
        self.Camp_ID_var.set("")
        self.Camp_Name_var.set("")
        self.Camp_No_var.set("")
        self.Title_var.set("")
        self.contact_var.set("")
        self.Tent_No_var.set("")
        self.address_var.set("")
        messagebox.showinfo('Success','Cleared sucessfully')



    def delete(self):
        query = "delete from camp where Camp_ID=%s;"
        id =self.Camp_ID_var.get()
        value = (id,)
        self.dbconnect.delete(query, value)
        messagebox.showinfo("Success", "Data deleted successfully")
        self.fetch()
        self.Camp_ID_var.set("")
        self.Camp_Name_var.set("")
        self.Camp_No_var.set("")
        self.Title_var.set("")
        self.contact_var.set("")
        self.Tent_No_var.set("")
        self.address_var.set("")

    def exit(self):
        self.root.destroy()
#
# #
# root=Tk()
# ob=camp(root)
# root.mainloop()