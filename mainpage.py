# -*- coding: utf-8 -*-
"""
Created on Thu Apr 15 15:18:43 2021

@author: Navaratna
"""

from tkinter import *
def student():
    wb.destroy()
    import login

wb=Tk()
wb.geometry('1250x1250')
wb.title('main page')
wb.configure(background='white')
h=Label(wb,text="Whats-App Bot",font=('times new roman',50),bg="white",fg='black')
h.place(x=450,y=40)

#open the card
c=Frame(wb,bd=6,bg='white',relief=RAISED,width="150")
c.place(x=350,y=190,height=500,width=600)
heading=Label(c,text="Lets Get Started ",font=('times new roman',20),bg="white",fg='black')
heading.place(x=205,y=30)
student=Button(c,text="Get In",command=student,height=2,width=20,bg="orange",fg="black")
student.place(x=205,y=200)

# admin=Button(c,text="Admin",height=2,width=20,bg="brown",fg="white")
# admin.place(x=205,y=240)
wb.mainloop()