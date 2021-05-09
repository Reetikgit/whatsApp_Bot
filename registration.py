from tkinter import *
from tkinter import messagebox
def step1Registration():
    
    
    def submit():
        from firebase import firebase
        #connection establishment
        firebase = firebase.FirebaseApplication('https://internship-4292c-default-rtdb.firebaseio.com/')
        
        #create object and insert Data
        
        name=name_data.get()
        contact= contact_data.get()
        age=age_data.get()
        phone=phone_data.get()
        
        
        data={
              "Name":name,
              "Contact" :contact,
              "Age":age,
              'Phone':phone,
              "Email":Uemail,
              "Password ":Upassword

        }
        result=firebase.post('Personal_Details',data)
        messagebox.showinfo('Success', 'Registration Completed')
        import login
    
    def uploadImg():
        from tkinter.filedialog import askopenfilename
        
        storage= firebase.storage()
        path=askopenfilename(
                initialdir="",
                filetypes=(('csv file',"*.csv"),('all files','*.*')),
                title="Choose and image"
            )
        
        #insert the images
        
        storage.child(path).put(path)
        sub_btn['state']=NORMAL
        
    import pyrebase

    #connection establishment
    firebaseConfig = {
        'apiKey': "AIzaSyBF-5wv5cyFVe2KmHPhY3fMx0ZlPvj403Y",
        'authDomain': "internship-4292c.firebaseapp.com",
        'databaseURL':'https://internship-4292c-default-rtdb.firebaseio.com/',
        'projectId': "internship-4292c",
        'storageBucket': "internship-4292c.appspot.com",
        'messagingSenderId': "484348816343",
        'appId': "1:484348816343:web:ac5083a4b0f669451bf992",
        'measurementId': "G-0K3TYDT7PS"
    }
    #initilizing the server

    firebase=pyrebase.initialize_app(firebaseConfig)
    
    #create object & perform operation
    #signup
    '''auth=firebase.auth()
    email=input("Enter your emailid")
    password=input("Enter your password")
    try:
        auth.create_user_with_email_and_password(email, password)
    except:
        print("Somethig went wronge")'''
        
        
        
    #Login
    auth=firebase.auth()
    Uemail=email_Data.get()
    Upassword=password_Data.get()
    Cpass=Cpassword_Data.get()
    if(Uemail=="" and Upassword=="" and Uemail.find("@")==-1):
        messagebox.showerror('Error', 'Please enter the valid details')
    elif(Upassword!=Cpass):
        messagebox.showerror('Error', 'Password Missed Match')
    else:     
        try:
            
            
            auth.create_user_with_email_and_password(Uemail, Upassword)
            messagebox.showinfo('Success', 'Successfull')
            
            #open step-2 Window
            firstWin.destroy()
            secondWin=Tk()
            secondWin.geometry('1250x1250')
            heading=Label(secondWin,text="Fill out Details Step 2",font=('Times',20,"bold"))
            heading.place(x=550,y=20)
            name=Label(secondWin,text="Name")
            name.place(x=300,y=80)
            name_data=Entry(secondWin)
            name_data.place(x=700,y=80)
            
            contact=Label(secondWin,text="Contact")
            contact.place(x=300,y=100)
            contact_data=Entry(secondWin)
            contact_data.place(x=700,y=100)
            
            email=Label(secondWin,text="Age")
            email.place(x=300,y=130)
            age_data=Entry(secondWin)
            age_data.place(x=700,y=130)
            
            phone=Label(secondWin,text="Phone")
            phone.place(x=300,y=160)
            phone_data=Entry(secondWin)
            phone_data.place(x=700,y=160)
            upload_btn=Button(secondWin,text="Upload",command=uploadImg)
            upload_btn.place(x=700,y=200)
            sub_btn=Button(secondWin,text="Submit",command=submit)
            sub_btn.place(x=1000,y=230)
            sub_btn['state']=DISABLED
            secondWin.mainloop()
        except:
             messagebox.showerror('Error', 'Something Went Wrong')

firstWin=Tk()
firstWin.geometry('1250x1200')
firstWin.title('Sign Up')
firstWin.configure(background='white')

h=Label(firstWin,text="Create Your Account : Step 1",font=('times new roman',30),bg="white",fg='orange')
h.place(x=450,y=140)
#User ID
emailId=Label(firstWin,text="EmailId",font=('Helvetica',10),bg="white")
emailId.place(x=550,y=220)

email_Data=Entry(firstWin)
email_Data.place(x=620,y=220)
#Password
password=Label(firstWin,text="Password",font=('Helvetica',10),bg="white")
password.place(x=540,y=280)

password_Data=Entry(firstWin,show="*")
password_Data.place(x=620,y=280)

Cpassword=Label(firstWin,text="Confirm Password",font=('Helvetica',10),bg="white")
Cpassword.place(x=500,y=340)

Cpassword_Data=Entry(firstWin,show="*")
Cpassword_Data.place(x=620,y=340)

login_btn=Button(firstWin,text="Continue",height=2,width=10,bg="green",fg="white",relief=SUNKEN,command=step1Registration)
login_btn.place(x=610,y=400)

firstWin.mainloop()