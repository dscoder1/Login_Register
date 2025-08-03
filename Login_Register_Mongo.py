from tkinter import *
from tkinter.messagebox import *
from PIL import Image,ImageTk
from tkinter import ttk
import pymongo
import datetime
import time
# Database Setup
Login=Tk()
Login.geometry("1500x750+10+10")
Login.title("Registration Page")
Login.resizable(width=False,height=False)
Login.iconbitmap("registerIcon.ico")
Login.config(bg="sky blue")

fname=StringVar()
lname=StringVar()
username=StringVar()
email=StringVar()
passwd=StringVar()

Loginusername=StringVar()
Loginpasswd=StringVar()

Forgotusername=StringVar()

empty=""

def MainWindow():
    pass
def submit():
    firstname=fname.get().strip()
    lastname=lname.get().strip()
    Username=username.get().strip()
    emailadd=email.get().strip()
    password=passwd.get().strip()
    
    if(firstname!="" and lastname!="" and Username!="" and emailadd!="" and password!=""):
        data={'firstname':firstname,'lastname':lastname,'username':Username,'email':emailadd,'password':password,'date':datetime.datetime.now()}
        coll.insert_one(data)
        fname.set(empty)
        lname.set(empty)
        username.set(empty)
        email.set(empty)
        passwd.set(empty)
        showinfo("Info","User Registered Successfully\n\nPlease Login !!")
        time.sleep(1)
        loginpage()
    else:
        showwarning("Warning","All Field Required")

def chck():
    Username=Loginusername.get().strip()
    password=Loginpasswd.get().strip()
    if(Username!="" and password!=""):
        data=coll.find_one({'username':Username,'password':password})
        if(data!=None):
            print(data)
            showinfo("Info","User Login Successfully")
            MainWindow()
            Loginusername.set(empty)
            Loginpasswd.set(empty)
        else:
            showwarning("Warning","Username or Password Not Matched")
            loginpage()
            Loginusername.set(empty)
            Loginpasswd.set(empty)
    else:
        showwarning("Warning","All Field Required")
        loginpage()

def chckPassword():
    username=Forgotusername.get().strip()
    print(username)
    if(username!=""):
        data=coll.find_one({'username':username})
        if(data!=None):
            print(data['password'])
            showinfo("Info","User Found !! \nPassword--"+data['password']+"\nPlease Login !!")
            Forgotusername.set(empty)
            time.sleep(1)
            loginpage()
        else:
            Forgotusername.set(empty)
            showerror("Error","User Not Found \nTry Again !!")
            loginpage()
    else:
        showwarning("Warning","All Field Required")
        chckpass()

def chckpass():
    ForgotPage=Toplevel()
    ForgotPage.geometry("1200x300+200+300")
    ForgotPage.title("Forgot Password Page")
    ForgotPage.resizable(width=False,height=False)
    ForgotPage.iconbitmap("registerIcon.ico")
    ForgotPage.config(bg="sky blue")
    ForgotBgImage = Image.open("Forgot.png") 
    ForgotBg_resize_image = ForgotBgImage.resize((1200,300))
    ForgotBgImage = ImageTk.PhotoImage(ForgotBg_resize_image) 
    ForgotImgLabel = Label(ForgotPage,image =ForgotBgImage) 
    ForgotImgLabel.place(x=0,y=0)
    ForgotLblFrame=LabelFrame(ForgotPage,bg="sky blue")
    ForgotLblFrame.place(x=250,y=70,height=170,width=700)
    ForgotForm=Label(ForgotLblFrame,text="Forgot Password Form",font=("Calibri",15,"bold"),bg="sky blue",bd=2,relief="ridge")
    ForgotForm.place(x=10,y=10,height=40,width=300)
    ForgotuserName=Label(ForgotLblFrame,text="Username",font=("Calibri",20,"bold"),bg="sky blue")
    ForgotuserName.place(x=30,y=85,height=40,width=120)
    ForgotUsernameEntry=Entry(ForgotLblFrame,font=("Calibri",15),textvariable=Forgotusername)
    ForgotUsernameEntry.place(x=160,y=92,height=30,width=350)
    ForgotCheck=Button(ForgotLblFrame,text="Check",font=("Calibri",20,"bold"),command=chckPassword,bg="blue",fg="white")
    ForgotCheck.place(x=550,y=90,height=33,width=130)
    ForgotPage.mainloop()

def loginpage():
    LoginPage=Toplevel()
    LoginPage.geometry("700x650+500+70")
    LoginPage.title("Login Page")
    LoginPage.resizable(width=False,height=False)
    LoginPage.iconbitmap("registerIcon.ico")
    LoginPage.config(bg="sky blue")
    LoginBgImage = Image.open("Login.png") 
    LoginBg_resize_image = LoginBgImage.resize((700,650))
    LoginBgImage = ImageTk.PhotoImage(LoginBg_resize_image) 
    LoginImgLabel = Label(LoginPage,image =LoginBgImage) 
    LoginImgLabel.place(x=0,y=0)
    LoginLblFrame=LabelFrame(LoginPage,bg="sky blue")
    LoginLblFrame.place(x=150,y=100,height=400,width=400)
    LoginForm=Label(LoginLblFrame,text="Login Form",font=("Calibri",20,"bold"),bg="sky blue",bd=5,relief="ridge")
    LoginForm.place(x=10,y=10,height=50,width=150)
    LoginuserName=Label(LoginLblFrame,text="Username",font=("Calibri",20,"bold"),bg="sky blue")
    LoginuserName.place(x=10,y=90,height=50,width=120)
    LoginUsernameEntry=Entry(LoginLblFrame,font=("Calibri",15),textvariable=Loginusername)
    LoginUsernameEntry.place(x=150,y=90,height=40,width=230)
    LoginPasswd=Label(LoginLblFrame,text="Password",font=("Calibri",20,"bold"),bg="sky blue")
    LoginPasswd.place(x=10,y=180,height=50,width=120)
    LoginPasswdEntry=Entry(LoginLblFrame,font=("Calibri",15),textvariable=Loginpasswd)
    LoginPasswdEntry.place(x=150,y=180,height=40,width=230)
    LoginSubmit=Button(LoginLblFrame,text="Login",font=("Calibri",20,"bold"),command=chck,bg="blue",fg="white")
    LoginSubmit.place(x=150,y=250,height=50,width=100)
    frgtpass=Button(LoginLblFrame,text="Forgot Password ?",font=("Calibri",17,"bold"),bg="sky blue",fg="blue",bd=0,command=chckpass)
    frgtpass.place(x=110,y=310,height=30,width=180)
    LoginPage.mainloop()

BgImage = Image.open("Register.png") 
Bg_resize_image = BgImage.resize((1500,750))
BgImage = ImageTk.PhotoImage(Bg_resize_image) 
ImgLabel = Label(Login,image =BgImage) 
ImgLabel.place(x=0,y=0)
LblFrame=LabelFrame(Login,bg="sky blue")
LblFrame.place(x=500,y=50,height=650,width=500)
RegisterForm=Label(LblFrame,text="Registration Form",font=("Calibri",20,"bold"),bg="sky blue",bd=5,relief="ridge")
RegisterForm.place(x=10,y=10,height=50,width=250)
Fname=Label(LblFrame,text="First Name",font=("Calibri",20,"bold"),bg="sky blue")
Fname.place(x=30,y=100,height=50,width=200)
FnameEntry=Entry(LblFrame,font=("Calibri",20),textvariable=fname)
FnameEntry.place(x=230,y=105,height=40,width=230)
Lname=Label(LblFrame,text="Last Name",font=("Calibri",20,"bold"),bg="sky blue")
Lname.place(x=30,y=170,height=50,width=200)
LnameEntry=Entry(LblFrame,font=("Calibri",20),textvariable=lname)
LnameEntry.place(x=230,y=175,height=40,width=230)
userName=Label(LblFrame,text="Username",font=("Calibri",20,"bold"),bg="sky blue")
userName.place(x=30,y=240,height=50,width=200)
UsernameEntry=Entry(LblFrame,font=("Calibri",20),textvariable=username)
UsernameEntry.place(x=230,y=245,height=40,width=230)
Email=Label(LblFrame,text="Email Add.",font=("Calibri",20,"bold"),bg="sky blue")
Email.place(x=30,y=310,height=50,width=200)
EmailEntry=Entry(LblFrame,font=("Calibri",20),textvariable=email)
EmailEntry.place(x=230,y=315,height=40,width=230)
Passwd=Label(LblFrame,text="Password",font=("Calibri",20,"bold"),bg="sky blue")
Passwd.place(x=30,y=380,height=50,width=200)
PasswdEntry=Entry(LblFrame,font=("Calibri",20),textvariable=passwd)
PasswdEntry.place(x=230,y=385,height=40,width=230)
Submit=Button(LblFrame,text="Submit",font=("Calibri",20,"bold"),command=submit,bg="blue",fg="white")
Submit.place(x=200,y=480,height=50,width=130)
login=Button(LblFrame,text="Login ?",font=("Calibri",17,"bold"),bg="sky blue",fg="blue",bd=0,command=loginpage)
login.place(x=230,y=550,height=30,width=70)

Login.mainloop()
