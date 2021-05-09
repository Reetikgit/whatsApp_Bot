# -*- coding: utf-8 -*-
"""
Created on Thu Apr 15 15:37:03 2021

@author: Navaratna
"""

from tkinter import *
from tkinter import messagebox, ttk
import random
import pyrebase

def openSignUpPage():
    import registration
def login():
    def verifyOtp():
        codeData=code_data.get()
        print((genOTP))
        print(int(codeData))
        if((genOTP) == int(codeData)):
            messagebox.showinfo('Otp Verified', 'OTP VERIFIED ')
            import pyttsx3

            voice = pyttsx3.init()

            speech = "Welcome "+email
            voice.say(speech)
            voice.runAndWait()
            Otpwin.destroy()
            import WhatsappBot
        else:
            messagebox.showinfo('Error', 'Invalid OTP')

    def editProfile():
        wind = Tk()
        wind.geometry('1250x1250')
        cd = Frame(wind, bd=5, bg='gray', relief=RAISED)
        cd.place(x=400, y=60, height=500, width=400)
        Rpassword = Label(cd, text="Re-enter password")
        Rpassword.place(x=40, y=10)
        Rpassword_data = Entry(cd)
        Rpassword_data.place(x=200, y=10)

        choose = Label(cd, text="choose the filed")
        choose.place(x=40, y=120)

        h = ttk.Combobox(cd)
        h['values'] = ('fname', 'lname')
        h.current(1)
        h.place(x=150, y=120)

        update = Label(cd, text="enter the  new vale")
        update.place(x=40, y=180)
        update_data = Entry(cd)
        update_data.place(x=200, y=180)

        up_btn = Button(cd, text="update")
        up_btn.place(x=130, y=220)
        wind.mainloop()
    import pyrebase

    # connection establishment
    firebaseConfig = {
        'apiKey': "AIzaSyBF-5wv5cyFVe2KmHPhY3fMx0ZlPvj403Y",
        'authDomain': "internship-4292c.firebaseapp.com",
        'databaseURL': 'https://internship-4292c-default-rtdb.firebaseio.com/',
        'projectId': "internship-4292c",
        'storageBucket': "internship-4292c.appspot.com",
        'messagingSenderId': "484348816343",
        'appId': "1:484348816343:web:ac5083a4b0f669451bf992",
        'measurementId': "G-0K3TYDT7PS"
    }
    # initilizing the server

    firebase = pyrebase.initialize_app(firebaseConfig)

    # create object & perform operation
    # signup
    auth = firebase.auth()
    email = email_data.get()
    password=password_data.get()



    try:
        auth.sign_in_with_email_and_password(email, password)
        import smtplib

        sender_email = "abcdtech.2021@gmail.com"
        sender_password = "mygmail9450021817"
        reciever_email = email
        genOTP = random.randint(1000, 9999)
        TEXT = "Your OTP for Login is " + str(genOTP)
        SUBJECT = "Verify Your OTP"
        message = 'Subject: {}\n\n{}'.format(SUBJECT, TEXT)

        # open gmail server

        s = smtplib.SMTP('smtp.gmail.com', 587)

        # start the server
        s.starttls()
        # login to server

        s.login(sender_email, sender_password)

        # send the mail
        s.sendmail(sender_email, reciever_email, message)

        s.quit()
        messagebox.showinfo('Success', 'Login Successfull')


        #Fetch name if user
        import pyrebase

        # connection establishment
        firebaseConfig = {
            'apiKey': "AIzaSyBF-5wv5cyFVe2KmHPhY3fMx0ZlPvj403Y",
            'authDomain': "internship-4292c.firebaseapp.com",
            'databaseURL': 'https://internship-4292c-default-rtdb.firebaseio.com/',
            'projectId': "internship-4292c",
            'storageBucket': "internship-4292c.appspot.com",
            'messagingSenderId': "484348816343",
            'appId': "1:484348816343:web:ac5083a4b0f669451bf992",
            'measurementId': "G-0K3TYDT7PS"
        }
        # initilizing the server

        firebase = pyrebase.initialize_app(firebaseConfig)

        db = firebase.database()
        # Fetch the data
        global name
        data = db.child('Personal_Details').get()
        for each_data in data.each():

            dbemail = each_data.val()['Email']

            if(email==dbemail):
                phone = each_data.val()['Phone']
                name = each_data.val()['Name']
                age = each_data.val()['Age']
                contact = each_data.val()['Contact']
                break;
        w.destroy()
        Otpwin = Tk()
        Otpwin.geometry('1250x1250')
        Otpwin.title('main page')
        Otpwin.configure(background='white')
        h = Label(Otpwin, text="Verify Your Identity", font=('times new roman', 50), bg="white", fg='black')
        h.place(x=10, y=40)
        card = Frame(Otpwin, bd=6, bg='white', relief=RAISED, width="150")
        card.place(x=350, y=190, height=500, width=600)
        heading = Label(card, text="Enter Code sent on your mail", font=('times new roman', 20), bg="white", fg='black')
        heading.place(x=200, y=30)
        code = Label(card, text="Enter Code", bg="white", font=('times new roman', 20))
        code.place(x=140, y=140)
        code_data = Entry(card)
        code_data.place(x=280, y=140)

        btnVerify = Button(card, text="Verify", command=verifyOtp, bg="orange", height=2, width=20)
        btnVerify.place(x=200, y=270)

    except:
        print("Somethig went wronge")
w=Tk()
w.geometry('1250x1250')
w.title('main page')
w.configure(background='white')
h=Label(w,text="Whats-App Bot Login",font=('times new roman',50),bg="white",fg='black')
h.place(x=10,y=40)
card=Frame(w,bd=6,bg='white',relief=RAISED,width="150")
card.place(x=350,y=190,height=500,width=600)
heading=Label(card,text="Welcome Back !",font=('times new roman',20),bg="white",fg='black')
heading.place(x=210,y=30)
email=Label(card,text="Email",bg="white",font=('times new roman',20))
email.place(x=140,y=140)
email_data=Entry(card)
email_data.place(x=280,y=140)

password=Label(card,text="Password",bg="white",font=('times new roman',20))
password.place(x=140,y=200)
password_data=Entry(card)
password_data.place(x=280,y=200)

btn=Button(card,text="login",command=login,bg="orange",height=2,width=20)
btn.place(x=200,y=270)

subheading=Label(card,text="Already have an account ?",font=('times new roman',12),bg="white",fg='black')
subheading.place(x=130,y=380)
btnSign=Button(card,text="Click here",command=openSignUpPage,bg="white",bd=0,borderwidth=0,  highlightthickness=0,
                      highlightcolor="white",
                      highlightbackground="white", )
btnSign.place(x=350,y=380)
# btnSign.pack()
w.mainloop()

