from tkinter import *
from PIL import ImageTk, Image
import pickle
import os
import tkinter.messagebox

d = {}
class Military_Form:
    def __init__(self, window):
        self.wn = window
        self.wn.title('Admin registeration')
        self.wn.geometry('430x450+900+120')
        self.wn.iconbitmap("regi.ico.ico")
        self.wn.resizable(False,False)

        global b
        b = ImageTk.PhotoImage(file="101.png")
        self.wn.background = Label(self.wn, image=b)
        self.wn.background.place(x=0,y=0)

        self.user_value = StringVar()
        self.pass_value = StringVar()
        self.add_value = StringVar()
        self.email_value = StringVar()
        self.contact_value = StringVar()
        self.age_value = StringVar()
        self.address_value = StringVar()


        self.lb_heading = Label(self.wn, text='Admin Register form:', bg='red', fg='white', font=('arial', 20, 'bold'))
        self.lb_heading.place(x=0, y=0, relwidth=1)
        self.lb_heading.grid(columnspan=4)

        # ====label and entry

        self.lb_username = Label(self.wn, text='User Name:', font=('arial', 15, 'bold'), fg='blue')
        self.lb_username.grid(row=1, column=0, padx=10, pady=10)

        self.ent_username = Entry(self.wn, font=('arial', 15, 'italic'), textvariable=self.user_value)
        self.ent_username.grid(row=1, column=1, padx=10, pady=10)

        self.lb_pass = Label(self.wn, text='Password:', font=('arial', 15, 'bold'), fg='blue')
        self.lb_pass.grid(row=2, column=0, padx=10, pady=10)

        self.ent_pass = Entry(self.wn, font=('arial', 15, 'bold'), show='*', textvariable=self.pass_value)
        self.ent_pass.grid(row=2, column=1, padx=10, pady=10)

        self.lb_email = Label(self.wn, text='E-mail:', font=('arial', 15, 'bold'), fg='blue')
        self.lb_email.grid(row=3, column=0, padx=10, pady=10)

        self.ent_email = Entry(self.wn, font=('arial', 15, 'bold'), textvariable=self.email_value)
        self.ent_email.grid(row=3, column=1, padx=10, pady=10)

        self.lb_contact = Label(self.wn, text='Contact Number:', font=('arial', 15, 'bold'), fg='blue')
        self.lb_contact.grid(row=4, column=0, padx=10, pady=10)

        self.ent_contact = Entry(self.wn, font=('arial', 15, 'bold'), textvariable=self.contact_value)
        self.ent_contact.grid(row=4, column=1, padx=10, pady=10)

        self.lb_age = Label(self.wn, text='Age:', font=('arial', 15, 'bold'), fg='blue')
        self.lb_age.grid(row=5, column=0, padx=10, pady=10)

        self.ent_age = Entry(self.wn, font=('arial', 15, 'bold'), textvariable=self.age_value)
        self.ent_age.grid(row=5, column=1, padx=10, pady=10)

        self.lb_Nation = Label(self.wn, text='Nation:', font=('arial', 15, 'bold'), fg='blue')
        self.lb_Nation.grid(row=6, column=0, padx=10, pady=10)

        self.ent_Nation = Entry(self.wn, font=('arial', 15, 'bold'), textvariable=self.address_value)
        self.ent_Nation.grid(row=6, column=1, padx=10, pady=10)

        self.btn_submit = Button(self.wn, text='submit', fg='green', bg='skyblue', font=('arial', 10, 'bold'),
                                 command=self.btn_submit_click)
        self.btn_submit.grid(row=7, column=0, padx=10, pady=10)

        self.ent_reset = Button(self.wn, text='Reset', fg='red', bg='skyblue', font=('arial', 10, 'bold'),
                                command=self.btn_reset_click)
        self.ent_reset.grid(row=7, column=1, padx=10, pady=10)

    def btn_submit_click(self):
        self.insert()

    def btn_reset_click(self):
        self.btn_reset()

    def insert(self):
        global d
        le = os.path.getsize('C:\\Users\\Admin\\PycharmProjects\\Secondsem\\front_end\\login.txt')
        username = self.ent_username.get()
        password = self.ent_pass.get()
        email = self.ent_email.get()
        contact = self.ent_contact.get()
        age = self.ent_age.get()
        address = self.ent_Nation.get()
        di = {username: [password, email, contact, age, address]}
        print(di)

        if le > 0:
            f = open('login.txt', 'rb+')
            d = pickle.load(f)
            d.update(di)
            f.seek(0)
            pickle.dump(d, f)
            tkinter.messagebox.showinfo('success', 'data saved successfully')
            f.close()
            self.wn.destroy()
        else:
            f = open('login.txt', 'wb')
            d.update(di)
            pickle.dump(d, f)
            f.close()
            self.wn.destroy()

    def btn_reset(self):
        self.ent_username.delete(0, END)
        self.ent_pass.delete(0, END)
        self.ent_email.delete(0, END)
        self.ent_contact.delete(0, END)
        self.ent_age.delete(0, END)
        self.ent_Nation.delete(0, END)

# wn=Tk()
# Military_Form(wn)
# wn.mainloop()
#
