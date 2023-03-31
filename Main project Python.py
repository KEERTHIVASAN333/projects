from tkinter import*
from tkinter import messagebox
from functools import partial
import pymysql
from tkinter import ttk
import subprocess as good
root=Tk()
root.title("Library")
root.geometry("550x550")

db_connection=pymysql.connect(
        host="localhost",
        user="root",
        passwd="keerthi",
        database="5c"
        )
my_database=db_connection.cursor()
print("connected")
#======================================================page1============================================================================================
def p1(): 
    F1=Frame(root,height='550', width='550')
    F1.pack()
    F1.EFrame = LabelFrame(F1, width=550, height=550, font=('arial', 10, 'bold'), bg='lightblue', relief='ridge', bd=13)
    F1.EFrame.place(x=0,y=0)

    #label
    l0=Label(F1,text="Library",font=("harem",35))
    l0.place(x=170,y=10)
    l1=Label(F1,text="Log in:",font=("harem",20))
    l1.place(x=15,y=100)
    l2=Label(F1,text="Email :",font=("harem",15))
    l2.place(x=20,y=200)
    l3=Label(F1,text="password:",font=("harem",15))
    l3.place(x=20,y=250)  
#======================================================sql check for login=================================================================================
    def login():
        Email=entry1.get()
        password=entry2.get()
        sql="select*from 11c where Email=%s and password=%s"
        my_database.execute(sql,[(Email),(password)])
        pro=my_database.fetchall()
        print(pro)
#=======================================================authors page======================================================================================        
        if(pro):
            messagebox.showinfo("showinfo","login successful")
            F3=Frame(F1,bg="firebrick1",height='550', width='550')
            F3.pack()
            F3.EFrame = LabelFrame(F3, width=550, height=550, font=('arial', 10, 'bold'), bg='firebrick1', relief='ridge', bd=13)
            F3.EFrame.place(x=0,y=0)
            #label
            ud=Label(F3,text="Pick your favorite author and book",font=('arial',20,'bold'))
            ud.place(x=15,y=11)
            #Menubutton1
            mb=  Menubutton (F1, text="Rabindhranath tagore",font=('arial', 15, 'bold'),bg="salmon")
            mb.menu =  Menu ( mb, tearoff = 0)
            mb["menu"] =  mb.menu
            
            def rabi_little():
                programname="notepad.exe"
                filename='little boy.txt'
                good.Popen([programname,filename])

            def astro():
                programname="notepad.exe"
                filename='astronomer.txt'
                good.Popen([programname,filename])

            b1Var = IntVar()
            b2Var = IntVar()
        
            mb.menu.add_checkbutton(label="1 The Little Big Man",variable=b1Var,command=rabi_little)
            mb.menu.add_checkbutton(label="2 The Astronomer",variable=b2Var,command=astro)
            mb.place(x=140,y=100)
            #Menubutton_2
            def a2b1():
                programname="notepad.exe"
                filename='author2b1.txt'
                good.Popen([programname,filename])
            def a2b2():
                programname="notepad.exe"
                filename='author2b2.txt'
                good.Popen([programname,filename])

            mb=  Menubutton (F1, text="Amitav Ghosh",font=('arial', 15, 'bold'),bg="salmon" )
        
            mb.menu =  Menu ( mb, tearoff = 0 )
            mb["menu"] =  mb.menu

            b3Var = IntVar()
            b4Var = IntVar()
        
            mb.menu.add_checkbutton(label="1 The Circle of Reason",command=a2b1,variable=b3Var)
            mb.menu.add_checkbutton(label="2 The Shadow Lines ",command=a2b2,variable=b4Var)
            mb.place(x=140,y=170)
            #Menubutton_3
            def a3b1():
                programname="notepad.exe"
                filename='author3b1.txt'
                good.Popen([programname,filename])
            def a3b2():
                programname="notepad.exe"
                filename='author3b2.txt'
                good.Popen([programname,filename])
            mb=  Menubutton (F1, text="William Shakespeare",font=('arial', 15, 'bold'),bg="salmon" )
            mb.menu =  Menu ( mb, tearoff = 0 )
            mb["menu"] =  mb.menu

            b5Var = IntVar()
            b6Var = IntVar()
        
            mb.menu.add_checkbutton(label="1 The Merchant of Venice",command=a3b1,variable=b5Var)
            mb.menu.add_checkbutton(label="2 Romeo ve Juliet ",command=a3b2,variable=b6Var)
            mb.place(x=140,y=250)
            #Menubutton_4
            def a4b1():
                programname="notepad.exe"
                filename='author4b1.txt'
                good.Popen([programname,filename])
            def a4b2():
                programname="notepad.exe"
                filename='author4b2.txt'
                good.Popen([programname,filename])
            mb=  Menubutton (F1, text="chetan Bhagat",font=('arial', 15, 'bold'),bg="salmon" )
            mb.menu =  Menu ( mb, tearoff = 0 )
            mb["menu"] =  mb.menu

            b7Var = IntVar()
            b0Var = IntVar()
        
            mb.menu.add_checkbutton(label="1 One Indian girl",command=a4b1,variable=b7Var)
            mb.menu.add_checkbutton(label="2 Making India Awesome",command=a4b2,variable=b0Var)
            mb.place(x=140,y=330)
            #Menubutton_5
            def a5b1():
                programname="notepad.exe"
                filename='author5b1.txt'
                good.Popen([programname,filename])
            def a5b2():
                programname="notepad.exe"
                filename='author5b2.txt'
                good.Popen([programname,filename])
        
            mb=  Menubutton (F1, text="Swami Vivekananda",font=('arial', 15, 'bold'),bg="salmon" )
            mb.menu =  Menu ( mb, tearoff = 0 )
            mb["menu"] =  mb.menu

            b11Var = IntVar()
            b12Var = IntVar()
        
            mb.menu.add_checkbutton(label="1 Raja Yoga",command=a5b1,variable=b11Var)
            mb.menu.add_checkbutton(label="2 Jnana Yoga",command=a5b2,variable=b12Var)
            mb.place(x=140,y=410)

            Exitbutton2=Button(F1,text="Exit",width=10,command=root.destroy)
            Exitbutton2.place(x=390,y=460)
            
        if(pro):
            f3=Frame(F1,width="550",bg="firebrick1",height="550")
            f3.pack()
            ud=Label(F1,text="Pick your favorite author and book",font=('arial',20,'bold'))
            ud.place(x=15,y=11)
        else:
            messagebox.showinfo("Alert","no user found")

    #Entry box
    entry1=Entry(F1,width='30')
    entry1.place(x=130,y=204)
    eb1=StringVar()
    entry2=Entry(F1,width='30')
    entry2.place(x=130,y=253)
    eb2=StringVar()
#========================================================Record============================================================================================
    def positive():
        F2=Frame(F1,height='550', width='550')
        F2.pack()
        F2.EFrame = LabelFrame(F2, width=550, height=550, font=('arial', 10, 'bold'), bg='medium spring green', relief='ridge', bd=13)
        F2.EFrame.place(x=0,y=0)
        #label
        l1=Label(F2,text="Record:",font=("harem",30)).place(x=15,y=15)
        l2=Label(F2,text="Email",font=("times new roman",15)).place(x=20,y=110)
        l3=Label(F2,text="password",font=("times new roman",15)).place(x=20,y=160)
        l4=Label(F2,text="confirm password",font=("times new roman",15)).place(x=20,y=210)
        
        def franck(eb1,eb2,eb3):
            Email=e1.get()
            password=e2.get()
            confirmpassword=e3.get()
            sql="INSERT INTO 11c(Email,password,confirmpassword)VALUES(%s,%s,%s)"
            value=(Email,password,confirmpassword)
            my_database.execute(sql,value)
            db_connection.commit()
            print("success")
            if(e1.get()and e2.get() and e3.get() and e2.get()==e3.get()):
                messagebox.showinfo("showinfo","Registered successfully")
            elif(e2.get()!=e3.get()):
                messagebox.showinfo("showerror","not matching")
         
            else:
                messagebox.showinfo("showinfo","fields cant be empty")      
        #Entry box
        e1=Entry(F2,width=30)
        e1.place(x=170,y=117)
        eb1=StringVar
        e2=Entry(F2,width=30)
        e2.place(x=170,y=167)
        eb2=IntVar
        e3=Entry(F2,width=30)
        e3.place(x=170,y=217)
        eb3=IntVar
        franck=partial(franck,eb1,eb2,eb3)
        #button_1
        signup_button2=Button(F2,text="Register",width=30,command= franck,bg="slateBlue1")
        signup_button2.place(x=150,y=310)
        back_to_log=Button(F2,text="Back to login",width=30,command=F2.destroy ,bg="slateBlue1")
        back_to_log.place(x=150,y=370)
       

    #button_2
    logbutton1=Button(F1,text="Log in",width=30,command=login,bg="blue violet")
    logbutton1.place(x=130,y=355)
    regbutton2=Button(F1,text="Register",width=30,command= positive,bg="orange")
    regbutton2.place(x=130,y=390)
    Exitbutton1=Button(F1,text="Exit",width=30,command=root.destroy,bg="red")
    Exitbutton1.place(x=130,y=425)



p1()



        
            
          
