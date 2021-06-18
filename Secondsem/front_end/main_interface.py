from tkinter import *
from tkinter import messagebox
from Secondsem.model.student import *
from Secondsem.back_end.connection import *

class Main_Interface:
    def __init__(self,root):
        self.wn=root
        self.wn.title('My Test Application')
        self.wn.geometry('400x500')

        self.name_var=StringVar()
        self.id_var=StringVar()

        #=====connection object===
        self.dbconnect=DbConnection()


        #====heading====
        heading=Label(self.wn,text='My Test Application',bg='yellow',font=('arial',20,'bold'))
        heading.pack(side=TOP, fill=X)


        #============Frame in window==========
        main_frame=Frame(self.wn,bg='magenta')
        main_frame.place(x=30,y=50,width=330,height=300)

        btn_frame=Frame(self.wn,bg='cyan',bd=5)
        btn_frame.place(x=30,y=350,width=330,height=60)

        #======widgets in frame==
        lbl_id=Label(main_frame,text='ID',font=('arial',15,'bold'),width=10)
        lbl_id.grid(row=0,column=1,padx=10,pady=10)

        self.ent_id=Entry(main_frame)
        self.ent_id.grid(row=0,column=2,padx=10,pady=10)

        lbl_name = Label(main_frame, text='Name', font=('arial', 15, 'bold'), width=10)
        lbl_name.grid(row=1, column=1, padx=10, pady=10)

        self.ent_name = Entry(main_frame)
        self.ent_name.grid(row=1, column=2, padx=10, pady=10)

        btn_add=Button(btn_frame,text='Add',font=('arial',10,'bold'),command=self.add)
        btn_add.pack(side=LEFT,padx=10,pady=10)

        btn_clear = Button(btn_frame, text='clear', font=('arial', 10, 'bold'))
        btn_clear.pack(side=LEFT, padx=10, pady=10)

        btn_update = Button(btn_frame, text='update', font=('arial', 10, 'bold'))
        btn_update.pack(side=LEFT, padx=10, pady=10)

    def add(self):
        stu_obj=Student(self.ent_id.get(),self.ent_name.get())
        query='insert into exp values(%s,%s);'
        values=(int(stu_obj.get_id()),stu_obj.get_name())
        self.dbconnect.insert(query,values)
        messagebox.showinfo('sucess','data inserted sucessfully')

    def update(self):
        stu_obj = Student(self.ent_id.get(), self.ent_name.get())
        query='update exp set name=%s where id=%s;'




window=Tk()
Main_Interface(window)
window.mainloop()