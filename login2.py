# -*- coding: utf-8 -*-
"""
Created on Thu Apr 15 15:37:03 2021

@author: Navaratna
"""

from tkinter import *
from tkinter import messagebox
from tkinter import ttk

def login():
    def editprofile():
        wind=Tk()
        wind.geometry('1250x1250')
        cd=Frame(wind,bd=5,bg='gray',relief=RAISED)
        cd.place(x=400,y=60,height=500,width=400)
        Rpassword=Label(cd,text="Re-enter password")
        Rpassword.place(x=40,y=10)
        Rpassword_data=Entry(cd)
        Rpassword_data.place(x=200,y=10)
        
        choose=Label(cd,text="choose the filed")
        choose.place(x=40,y=120)
        
        h=ttk.Combobox(cd)
        h['values']=('fname','lname')
        h.current(1)
        h.place(x=150,y=120)
        
        update=Label(cd,text="enter the  new vale")
        update.place(x=40,y=180)
        update_data=Entry(cd)
        update_data.place(x=200,y=180)
        
        up_btn=Button(cd,text="update")
        up_btn.place(x=130,y=220)
        wind.mainloop()
    import pyrebase

    #connection established
    
    firebaseConfig = {
        'apiKey': "AIzaSyB-5omastgFFE2B7fHHbHp2Jmvok3_SYlc",
        'authDomain': "internship-98081.firebaseapp.com",
        'databaseURL':'https://internship-98081-default-rtdb.firebaseio.com/',
        'projectId': "internship-98081",
        'storageBucket': "internship-98081.appspot.com",
        'messagingSenderId': "185151675490",
        'appId': "1:185151675490:web:959d79cdb08968daeb053b",
        'measurementId': "G-B0XR8693FW"
      }
    
    #initialsiing the server
    firebase=pyrebase.initialize_app(firebaseConfig)
    
    #create the object perform the operation
   
        
        
    #login
    auth=firebase.auth()
    email=email_data.get()
    password=password_data.get()
    try:
        auth.sign_in_with_email_and_password(email, password)
        print("success")
        messagebox.showinfo('information','login successful')
        dashboard=Tk()
        dashboard.geometry('1250x1250')
        dashboard.configure(background='blue')
        #fetch the name of user
        import pyrebase

        #connection established
        
        firebaseConfig = {
            'apiKey': "AIzaSyB-5omastgFFE2B7fHHbHp2Jmvok3_SYlc",
            'authDomain': "internship-98081.firebaseapp.com",
            'databaseURL':'https://internship-98081-default-rtdb.firebaseio.com/',
            'projectId': "internship-98081",
            'storageBucket': "internship-98081.appspot.com",
            'messagingSenderId': "185151675490",
            'appId': "1:185151675490:web:959d79cdb08968daeb053b",
            'measurementId': "G-B0XR8693FW"
          }
        
        #initialsiing the server
        firebase=pyrebase.initialize_app(firebaseConfig)
        
        db=firebase.database()
        
        #fetch the data
        data=db.child('personal_details').get()
        for each_data in data.each():
            email1=each_data.val()['email']
            if(email1==email):
                name=each_data.val()['fname']
                name2=each_data.val()['lname']
           
           

        #heading
        heading=Label(dashboard,text=("Welcome"+" "+name+" "+name2),font=('times new roman',30),bg='blue',fg='white')
        heading.place(x=500,y=40)
        
        from datetime import datetime,timedelta

        #present date and time
        present=datetime.now()
        #print(present)
        
        
        
        presenttime=present.strftime("%H::%M::%S")
        print(presenttime)
        login_time=Label(dashboard,text=("login time"+presenttime))
        login_time.place(x=900,y=100)
        
        show_btn=Button(dashboard,text="show details")
        show_btn.place(x=700,y=200)
        
        c=Frame(dashboard,bd=5,bg='gray',relief=RAISED)
        c.place(x=10,y=120,height=800,width=400)
        Namee=Label(c,text=name)
        Lname=Label(c,text=name2)
        Email=Label(c,text=email1)
        Namee.place(x=20,y=30)
        Lname.place(x=20,y=60)
        Email.place(x=20,y=90)
        
        
        edit=Button(c,text="Edit profile",command=editprofile)
        edit.place(x=30,y=200)
        
    except:
        print("something wrong")
        messagebox.showinfo('error','incorrect credential')
    dashboard.mainloop()
    
    
   
    

w=Tk()
w.geometry('1250x1250')
email=Label(w,text="email")
email.place(x=40,y=60)
email_data=Entry(w)
email_data.place(x=80,y=60)

password=Label(w,text="password")
password.place(x=20,y=135)
password_data=Entry(w)
password_data.place(x=80,y=140)

btn=Button(w,text="login",command=login)
btn.place(x=100,y=180)

w.mainloop()
