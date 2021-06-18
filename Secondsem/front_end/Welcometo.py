from tkinter import *
import Secondsem.front_end.armyinfo
import Secondsem.front_end.camp
import Secondsem.front_end.wep

class welcome:
    def __init__(self, window):
        self.wn = window
        self.wn.title('Welcome to military management system')
        self.wn.geometry('1050x900+30+20')
        self.wn.iconbitmap("welcomee.ico.ico")

        #===image======================================================================
        global b
        b = PhotoImage(file="55.png")
        self.wn.background = Label(self.wn, image=b)
        self.wn.background.place(x=-10, y=0)

        global a
        a = PhotoImage(file="wat.png")
        self.wn.background = Label(self.wn, image=a)
        self.wn.background.place(x=150, y=100)

        global c
        c = PhotoImage(file="pistol.png")
        self.wn.background = Label(self.wn, image=c)
        self.wn.background.place(x=100, y=400)

        global  d
        d = PhotoImage(file="fire.png")
        self.wn.background = Label(self.wn, image=d)
        self.wn.background.place(x=100, y=550)
        #
        global e
        e = PhotoImage(file="sold.png")
        self.wn.background = Label(self.wn, image=e)
        self.wn.background.place(x=100, y=700)


        # ========== Label Heading ===========================================================================================================================

        self.lb_heading = Label(self.wn, text='Welcome', bg='black',fg="white",
                                font=('arial', 20, 'bold'))
        self.lb_heading.place(x=0, y=0, relwidth=1)
        self.lb_heading = Label(self.wn, text='Hello admin please select the given option to manage which field you want from below ',
                                bg='yellow', fg='black',
                                font=('arial', 18, 'bold'))
        self.lb_heading.place(x=10, y=50)

        # ========== Button =====================================================================================
        self.btn_wep = Button(self.wn, text='Weapons', fg='white', bg='black', font=('ariel', 14, 'bold'), bd='6',
                              command=self.btn_wep_click)
        self.btn_wep.place(x=200, y=405, relwidth=0.4)

        self.btn_arm = Button(self.wn, text='Army info', fg='white',bg='black', font=('ariel', 14, 'bold'), bd='6',
                              command=self.btn_arm_click)
        self.btn_arm.place(x=210, y=710, relwidth=0.4)

        self.btn_cam = Button(self.wn, text='Camp', fg='white',bg='black', font=('ariel', 14, 'bold'), bd='6',
                              command=self.btn_cam_click)
        self.btn_cam.place(x=195, y=565, relwidth=0.4)

        self.btn_exit = Button(self.wn, text='exit', fg='white', bg='purple', font=('ariel', 14, 'bold'), bd='6',
                              command=self.btn_exit_click)
        self.btn_exit.place(x=200, y=790,relwidth=0.4)

    #
    def btn_arm_click(self):
        user_window=Toplevel()
        Secondsem.front_end.armyinfo.armyinfo(user_window)


    def btn_cam_click(self):
        user_window=Toplevel()
        Secondsem.front_end.camp.camp(user_window)

    def btn_wep_click(self):
        user_window = Toplevel()
        Secondsem.front_end.wep.wep(user_window)


    def btn_exit_click(self):
        self.wn.destroy()


# wn = Tk()
# welcome(wn)
# wn.mainloop()

