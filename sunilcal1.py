#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import tkinter
from tkinter import*
from tkinter import messagebox
val=""
A=0
operator=""

def btn_1_isclicked():
    global val
    val=val+"1"
    data.set(val)
    
def btn_2_isclicked():
    global val
    val=val+"2"
    data.set(val)

def btn_3_isclicked():
    global val
    val=val+"3"
    data.set(val)
    
def btn_4_isclicked():
    global val
    val=val+"4"
    data.set(val)

def btn_5_isclicked():
    global val
    val=val+"5"
    data.set(val)
    
def btn_6_isclicked():
    global val
    val=val+"6"
    data.set(val)    

def btn_7_isclicked():
    global val
    val=val+"7"
    data.set(val)
    
def btn_8_isclicked():
    global val
    val=val+"8"
    data.set(val)
    
def btn_9_isclicked():
    global val
    val=val+"9"
    data.set(val)    
    
def btn_0_isclicked():
    global val
    val=val+"0"
    data.set(val)    
    
def btn_plus_clicked():
    global A
    global operator
    global val
    A=int(val)
    operator="+"
    val=val+"+"
    data.set(val)
    
def btn_min_clicked():
    global A
    global operator
    global val
    A=int(val)
    operator="-"
    val=val+"-"
    data.set(val)
def btn_mul_clicked():
    global A
    global operator
    global val
    A=int(val)
    operator="*"
    val=val+"*"
    data.set(val)
def btn_div_clicked():
    global A
    global operator
    global val
    A=int(val)
    operator="/"
    val=val+"/"
    data.set(val)
    
def ac_pressed():
    global A
    global operator
    global val
    val=""
    A=0
    operator=""
    data.set(val) 
def result():  
    global A
    global operator
    global val
    val2=val
    if operator=="+":
        y=int((val2.split("+")[1]))
        c=A+y
        data.set(c)
        val=str(c)
    elif operator=="-":
        y=int((val2.split("-")[1]))
        c=A-y
        data.set(c)
        val=str(c)
    
    elif operator=="*":
        y=int((val2.split("*")[1]))
        c=A*y
        data.set(c)
        val=str(c)
        
    elif operator=="/":
        y=int((val2.split("/")[1]))
        if y==0:
            messagebox.showerror("error","invalid input")
            A=""
            val=""
            data.set(val)
        else:
            
            c=A/y
            data.set(c)
            val=str(c)
    
root=Tk()
sk=Label(root,text="calculator")
sk.pack()

data=StringVar()

lbl=Label(
    root,
    text="Label",
    anchor=SE,
    font=("verdana",20),
    textvariable=data,
)
lbl.pack(expand=1,fill="both")

btnrow1=Frame(root)
btnrow1.pack(expand=1,fill="both",)

btnrow2=Frame(root)
btnrow2.pack(expand=1,fill="both",)

btnrow3=Frame(root)
btnrow3.pack(expand=1,fill="both",)

btnrow4=Frame(root)
btnrow4.pack(expand=1,fill="both",)


btn1=Button(
    btnrow1,
    text="1",
    font=("verdana",22),
    relief=GROOVE,
    border=0,
    command=btn_1_isclicked,
)
btn1.pack(side=LEFT,expand=1,fill="both",)

btn2=Button(
    btnrow1,
    text="2",
    font=("verdana",22),
    relief=GROOVE,
    border=0,
    command=btn_2_isclicked,
)
btn2.pack(side=LEFT,expand=1,fill="both",)

btn3=Button(
    btnrow1,
    text="3",
    font=("verdana",22),  
 relief=GROOVE,
    border=0,
    command=btn_3_isclicked,
)
btn3.pack(side=LEFT,expand=1,fill="both",)


btn4=Button(
    btnrow1,
    text="+",
    font=("verdana",22),
    relief=GROOVE,
    border=0,
    command=btn_plus_clicked,
)
btn4.pack(side=LEFT,expand=1,fill="both",)

btn5=Button(
    btnrow2,
    text="4",
    font=("verdana",22),
    relief=GROOVE,
    border=0,
    command=btn_4_isclicked,
)
btn5.pack(side=LEFT,expand=1,fill="both",)

btn6=Button(
    btnrow2,
    text="5",
    font=("verdana",22),
    relief=GROOVE,
    border=0,
    command=btn_5_isclicked,
)
btn6.pack(side=LEFT,expand=1,fill="both",)

btn3=Button(
    btnrow2,
    text="6",
    font=("verdana",22),
relief=GROOVE,
    border=0,
    command=btn_6_isclicked,
)
btn3.pack(side=LEFT,expand=1,fill="both",)


btn4=Button(
    btnrow2,
    text="-",
    font=("verdana",22),
relief=GROOVE,
    border=0,
    command=btn_min_clicked,
)
btn4.pack(side=LEFT,expand=1,fill="both",)
btn1=Button(
    btnrow3,
    text="7",
    font=("verdana",22),
relief=GROOVE,
    border=0,
    command=btn_7_isclicked,
)
btn1.pack(side=LEFT,expand=1,fill="both",)

btn2=Button(
    btnrow3,
    text="8",
    font=("verdana",22),
relief=GROOVE,
    border=0,
    command=btn_8_isclicked,
)
btn2.pack(side=LEFT,expand=1,fill="both",)

btn3=Button(
    btnrow3,
    text="9",
    font=("verdana",22),
relief=GROOVE,
    border=0,
    command=btn_9_isclicked,
)
btn3.pack(side=LEFT,expand=1,fill="both",)


btn4=Button(
    btnrow3,
    text="*",
    font=("verdana",22),
relief=GROOVE,
    border=0,
    command=btn_mul_clicked,
)
btn4.pack(side=LEFT,expand=1,fill="both",)

btn1=Button(
    btnrow4,
    text="ac",
    font=("verdana",22),
relief=GROOVE,
    border=0,
    command=ac_pressed,
)
btn1.pack(side=LEFT,expand=1,fill="both",)

btn2=Button(
    btnrow4,
    text="0",
    font=("verdana",22),
relief=GROOVE,
    border=0,
    command=btn_0_isclicked,
)
btn2.pack(side=LEFT,expand=1,fill="both",)

btn3=Button(
    btnrow4,
    text="=",
    font=("verdana",22),
relief=GROOVE,
    border=0,
    command=result,
)
btn3.pack(side=LEFT,expand=1,fill="both",)


btn4=Button(
    btnrow4,
    text="/",
    font=("verdana",22),
relief=GROOVE,
    border=0,
    command=btn_div_clicked,
)
btn4.pack(side=LEFT,expand=1,fill="both",)

root.mainloop()


# In[ ]:





# In[ ]:





# In[ ]:




