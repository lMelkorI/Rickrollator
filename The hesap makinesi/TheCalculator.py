from tkinter import*
import pygame

root=Tk()
root.title("Simple Calculator")
e=Entry(root,width=50,borderwidth=5)
e.grid(row=0,column=0,columnspan=3,padx=10,pady=10)
def click(number):
   current=e.get()
   e.delete(0,END)
   e.insert(0,str(current)+str(number))
def clear():
    e.delete(0,END)
def add():
    a=e.get()
    global num
    global durum
    durum="+"
    num=float(a)
    e.delete(0,END)
def subs():
    a=e.get()
    global num
    global durum
    durum="-"
    num=float(a)
    e.delete(0,END)
def multiply():
    a=e.get()
    global num
    global durum
    durum="*"
    num=float(a)
    e.delete(0,END)
def divide():
    a=e.get()
    global num
    global durum
    durum="/"
    num=float(a)
    e.delete(0,END)
def dot():
    a=e.get()
    e.delete(0,END)
    e.insert(0,str(a)+".")
    

def equal():
    b=int(e.get())
    e.delete(0,END)
    if durum=="+":
        e.insert(0,31)
    elif durum=="-":
        e.insert(0,31)
    elif durum=="*":
        e.insert(0,31)
    else: 
        e.insert(0,31)
    pygame.init()
    pygame.mixer.music.load("Never gonna give you up.mp3")
    pygame.mixer.music.play(loops=0,start=41.7)
    



# Make the buttons
button_1=Button(root,text="1",padx=40,pady=20,command=lambda: click(1))
button_2=Button(root,text="2",padx=40,pady=20,command=lambda: click(2))
button_3=Button(root,text="3",padx=40,pady=20,command=lambda: click(3))
button_4=Button(root,text="4",padx=40,pady=20,command=lambda: click(4))
button_5=Button(root,text="5",padx=40,pady=20,command=lambda: click(5))
button_6=Button(root,text="6",padx=40,pady=20,command=lambda: click(6))
button_7=Button(root,text="7",padx=40,pady=20,command=lambda: click(7))
button_8=Button(root,text="8",padx=40,pady=20,command=lambda: click(8))
button_9=Button(root,text="9",padx=40,pady=20,command=lambda: click(9))
button_0=Button(root,text="0",padx=40,pady=20,command=lambda: click(0))
button_ad=Button(root,text="+",padx=38,pady=20,command=add)
button_sub=Button(root,text="-",padx=40,pady=20,command=subs)
button_mult=Button(root,text="x",padx=41,pady=20,command=multiply)
button_divd=Button(root,text="/",padx=41,pady=20,command=divide)
button_clear=Button(root,text="clear",padx=87,pady=20,command=clear)
button_equal=Button(root,text="=",padx=95,pady=20,command=equal)
button_dot=Button(root,text=".",padx=41,pady=20,command=dot)

#Button on screen
button_1.grid(row=3,column=0)
button_2.grid(row=3,column=1)
button_3.grid(row=3,column=2)

button_4.grid(row=2,column=0)
button_5.grid(row=2,column=1)
button_6.grid(row=2,column=2)

button_7.grid(row=1,column=0)
button_8.grid(row=1,column=1)
button_9.grid(row=1,column=2)

button_0.grid(row=4,column=0)

button_ad.grid(row=5,column=0)
button_sub.grid(row=6,column=0)
button_mult.grid(row=6,column=1)
button_divd.grid(row=6,column=2)

button_clear.grid(row=4,column=1,columnspan=2)
button_equal.grid(row=5,column=1,columnspan=2)
button_dot.grid(row=7,column=0)





root.mainloop()