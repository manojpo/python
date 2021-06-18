from tkinter import *
import Secondsem.front_end.militaryregisteration
import tkinter.messagebox
import os
import pickle
import Secondsem.front_end.Welcometo

class Login:
    def __init__(self, window):
        self.wn = window
        self.wn.geometry('480x600+500+100')
        self.wn.title('Admin Login')
        self.wn.iconbitmap("adminn.ico.ico")
        self.wn.resizable(False,False)

        # ======all image=========================
        global a
        a = PhotoImage(file='hj.png')
        self.wn.background= Label(self.wn, image=a)
        self.wn.background.place(x=0,y=0)

        global b
        b= PhotoImage(file='70.png')
        self.wn.background=Label(self.wn, image=b)
        self.wn.background.place(x=190,y=150)

        # ==lbl heading================================
        self.lb_heading = Label(self.wn, text='Admin Page', bg='black', fg='white', font=('arial', 20, 'bold'))
        self.lb_heading.place(x=0, y=0, relwidth=1)
        self.lb_heading = Label(self.wn, text='Hello! Creating new admin account? signup here:', bg='green', fg='white', font=('arial', 13, 'bold'))
        self.lb_heading.place(x=0, y=550)
        # ===frame=================================================
        self.frame1 = Frame(self.wn,bg='green')
        self.frame1.place(x=50, y=250)

        # ====label and entry

        self.lb_Username = Label(self.frame1, text='Username:', bg='light green', font=('arial', 15, 'italic'), fg='blue')
        self.lb_Username.grid(row=0, column=0, padx=10, pady=10)

        self.ent_Username = Entry(self.frame1, font=('arial', 15,'italic'))
        self.ent_Username.grid(row=0, column=1, padx=10, pady=10)

        self.lb_pass = Label(self.frame1, text='Password:',  bg='light green', font=('arial', 15, 'italic'), fg='blue')
        self.lb_pass.grid(row=1, column=0, padx=10, pady=10)

        self.ent_pass = Entry(self.frame1, font=('arial', 15,'italic'), show='*')
        self.ent_pass.grid(row=1, column=1, padx=10, pady=10)

        # ======buttons

        self.btn_login = Button(self.wn, text='Login', fg='blue', font=('arial', 10, 'bold'),
                                command=self.btn_login_click)
        self.btn_login.place(x=300, y=360)

        self.btn_reset = Button(self.wn, text='Reset', fg='black', font=('arial', 10, 'bold'),
                                command=self.btn_reset_click)
        self.btn_reset.place(x=350, y=360)

        self.btn_signup = Button(self.wn, text='Sign Up', fg='blue',bg='light green', font=('arial', 10, 'bold'),
                                 command=self.btn_signup_click)
        self.btn_signup.place(x=400, y=550)

        #====click buttons

    def btn_signup_click(self):
        user_window = Toplevel()
        Secondsem.front_end.militaryregisteration.Military_Form(user_window)
        # user_window.destroy()
    #
    def btn_login_click(self):
        self.load()

    def load(self):
        le = os.path.getsize('C:\\Users\\Admin\\PycharmProjects\\Secondsem\\front_end\\login.txt')

        if le > 0:
            f=open('login.txt', 'rb')
            ld = pickle.load(f)
            print(ld)
            f.close()
            for i, j in ld.items():
                if i == self.ent_Username.get():
                    for p in j:
                        if self.ent_pass.get()==p:
                            tkinter.messagebox.showinfo('Login success','Congarulations login successful!')
                            self.wn.withdraw()
                            wn=Toplevel()
                            Secondsem.front_end.Welcometo.welcome(wn)
                            return
            else:
                tkinter.messagebox.showerror('Error', 'Sorry! User password  wrong')

        else:
            print('Empty file')

    def btn_reset_click(self):
        self.ent_Username.delete(0, END)
        self.ent_pass.delete(0, END)


wn = Tk()
Login(wn)
wn.mainloop()
