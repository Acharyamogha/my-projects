from tkinter import *
root=Tk()
eq=" "
equation=StringVar()
calculation=Label(root, textvariable=equation)

equation.set("Enter your equation: ")
calculation.grid(columnspan=5)

def btnpress(num):
    global eq
    eq=eq+str(num)
    equation.set(eq)

def Equalpress():
    global eq
    sum=str(eval(eq))
    equation.set(sum)
    eq=" "

def clear():
    global eq
    eq=" "
    equation.set(" ")

b7=Button(root, text="7",command=lambda:btnpress(7))
b7.grid(row=1,column=0)

b8=Button(root, text="8",command=lambda:btnpress(8))
b8.grid(row=1,column=1)

b9=Button(root, text="9",command=lambda:btnpress(9))
b9.grid(row=1,column=2)

b4=Button(root, text="4",command=lambda:btnpress(4))
b4.grid(row=2,column=0)

b5=Button(root, text="5",command=lambda:btnpress(5))
b5.grid(row=2,column=1)

b6=Button(root, text="6",command=lambda:btnpress(6))
b6.grid(row=2,column=2)

b1=Button(root, text="1",command=lambda:btnpress(1))
b1.grid(row=3,column=0)

b2=Button(root, text="2",command=lambda:btnpress(2))
b2.grid(row=3,column=1)

b3=Button(root, text="3",command=lambda:btnpress(3))
b3.grid(row=3,column=2)

b0=Button(root, text="0",command=lambda:btnpress(0))
b0.grid(row=4,column=1)

plus=Button(root, text="+",command=lambda:btnpress("+"))
plus.grid(row=4,column=3)

minus=Button(root, text="-",command=lambda:btnpress("-"))
minus.grid(row=3,column=3)

multi=Button(root, text="x",command=lambda:btnpress("*"))
multi.grid(row=2,column=3)

divide=Button(root, text="/",command=lambda:btnpress("/"))
divide.grid(row=1,column=3)

equal=Button(root, text= "=", command=Equalpress)
equal.grid(row=4,column=2)

clear=Button(root, text="C",command=clear)
clear.grid(row=4,column=0)


root.mainloop()
