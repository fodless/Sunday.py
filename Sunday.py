from tkinter import *
import time




def NycSal():
    FinalAmount = 0
    i=0
    Gross = 0
    tax = 0.66
    Nys = Tk()
    Nys.geometry('500x800')
    Lgross = Label(Nys, text='Gross Income')
    Lgross.place(x=10,y=10)
    Egross = Entry(Nys)
    Egross.place(x=10,y=30)
        
    Lrent = Label(Nys, text='How much do you spend on rent / Mortgage monthly?')
    Lrent.place(x=10,y=80)
    Erent = Entry(Nys)
    Erent.place(x=10,y=100)

    LFL = Label(Nys, text='If you finance or lease your car, how much do you spend monthly?')
    LFL.place(x=10,y=150)
    EFL = Entry(Nys)
    EFL.place(x=10,y=170)

    Lsave = Label(Nys, text='How much do you save monthly?')
    Lsave.place(x=10,y=220)
    Esave = Entry(Nys)
    Esave.place(x=10,y=240)

    LGross = Label(Nys, text=Gross)
    LGross.place(x=10,y=300)

    def Calculate():
        Gross = Egross.get
        Rent = Erent.get
        FL = EFL.get
        Save = Esave.get
        Grossposttax = Gross * tax
        otherexpences = Rent + FL + Save
        print(otherexpences)
        FinalAmount == Grossposttax - otherexpences
        
        
        print('Through on calc')

    LGross = Button(Nys, text='Calculate', command=Calculate)
    LGross.place(x=10,y=270)
    print('h')
    Nys.mainloop()
    

def Gpa00():

    GpaCalc = Tk()
    GpaCalc.geometry('300x400')
    GpaCalc.title('Gpa Calculator')
    GpaCalc.config(bg='#101820')

    Header11 = Label(GpaCalc, text='GPA Calculator', font=('arial', 30), bg='#101820')
    Header11.place(x=35,y=20)

    global Fresh00
    Fresh00 = Entry(GpaCalc, text='Freshmn', width='10')
    Fresh00.place(y=80)
    Fresh01 = Label(GpaCalc, text='Grade Freshman Year', bg='#101820')
    Fresh01.place(x=105,y=82)

    global Soph00
    Soph00 = Entry(GpaCalc, text='Fresman', width='10')
    Soph00.place(y=110)
    Soph01 = Label(GpaCalc, text='Grade Sophmore Year', bg='#101820')
    Soph01.place(x=105,y=112)

    global Jun00
    Jun00 = Entry(GpaCalc, text='Feshman', width='10')
    Jun00.place(y=140)
    Jun01 = Label(GpaCalc, text='Grade Junior Year', bg='#101820')
    Jun01.place(x=105,y=142)

    global Seni00
    Seni00 = Entry(GpaCalc, text='Freshman', width='10')
    Seni00.place(y=170)
    Seni01 = Label(GpaCalc, text='Grade Senior Year', bg='#101820')
    Seni01.place(x=105,y=172)

    Finalstuf = Label(GpaCalc, text=' ', bg='#101820')
    Finalstuf.place(y=230)
    Finalstuf2 = Label(GpaCalc, text=' ', bg='#101820')
    Finalstuf2.place(y=250)

    def Gpamath():
        Freshval = Fresh00.get
        Fresher = int(Freshval())
        Sophval = Soph00.get
        Sophy = int(Sophval())
        Junval = Jun00.get
        Juny = int(Junval())
        Senval = Seni00.get
        Seny = int(Senval())
        FS00 = Fresher + Sophy
        JS00 = Juny + Seny
        Gpaadded = FS00 + JS00
        GpaFinal = Gpaadded / 4

        if GpaFinal < 65:
            Gpa = 0
        elif GpaFinal > 64 and GpaFinal < 67:
            Gpa = 1.0
        elif GpaFinal > 66 and GpaFinal < 70:
            Gpa = 1.3
        elif GpaFinal > 69 and GpaFinal < 73:
            Gpa = 1.7       
        elif GpaFinal > 72 and GpaFinal < 77:
            Gpa = 2.0
        elif GpaFinal > 76 and GpaFinal < 80:
            Gpa = 2.3
        elif GpaFinal > 79 and GpaFinal < 83:
            Gpa = 2.7
        elif GpaFinal > 82 and GpaFinal < 87:
            Gpa = 3.0
        elif GpaFinal > 86 and GpaFinal < 90:
            Gpa = 3.3
        elif GpaFinal > 89 and GpaFinal < 93:
            Gpa = 3.7
        elif GpaFinal > 92:
            Gpa = 4.0
        Finalstuf.config(text=f'Percent Average = {GpaFinal}')
        Finalstuf2.config(text=f'Gpa = {Gpa}')


    GpaSum = Button(GpaCalc, text='Calculate', command=Gpamath, highlightbackground='#101820')
    GpaSum.place(y=200)
    GpaCalc.mainloop()

def Kaliui():
    print('Kali In')

    Decide = Tk()
    Decide.geometry('500x500')
    Decide.config(bg='#000010')

    def Enter_Button():
        print('testing')
        input = Entry01.get()
        if input == 'a':
            print('lack of api here is killing me')

    Entry01 = Entry(Decide, highlightbackground="#208E90", bg='#208E90')
    Entry01.place(x='10', y='40')

    Button01 = Button(Decide, command=Enter_Button, highlightbackground='#000010')
    Button01.place(x='8')

    Decide.mainloop()

def Home():
    print('Home In')


    Homescreen = Tk()
    Homescreen.title('Sunday by Yours Truely')
    Homescreen.geometry('800x500')
    Homescreen.config(bg='#363945')

    TopHeader = Label(Homescreen, text='Select An Option', font=('arial', 20),  bg='#363945')
    TopHeader.place(x=320,y=10)

    Op1 = Button(Homescreen, text='GPA CALCULATOR', command=Gpa00, highlightbackground='#363945')
    Op1.place(y=50)
    Op1.pack

    Homescreen.mainloop()

def LoginPage():

    

    Login = Tk()
    Login.title('Login')
    Login.config(bg='black')

    Username00 = Entry(Login)
    Username00.place(x=4,y=10)
    Username00.pack

    Password00 = Entry(Login, width=10)
    Password00.place(x=49, y=40)
    Password00.pack



    def LoginCheck():
        User = Username00.get()
        Password = Password00.get()

        class Users:
            def __init__(self, Username, Password):
                self.Username = Username
                self.Password = Password
                pass

        George = Users('A', '03')
        Kali = Users('Kali', 'Kali')

        if User == (George.Username) and Password == (George.Password):
            Home()
            print('Login Out and Over')
        elif User == (Kali.Username) and Password == (Kali.Password):
            Kaliui()


            
        else:
            print('-Incorect Login-')

            print('User tried for ', User)
            print('Corosponding Password Attempt: ', Password)

    LoginChecker = Button(Login,highlightbackground='black', command=LoginCheck)
    LoginChecker.place(x=79,y=70)
    Login.mainloop()






LoginPage()
#NycSal()
