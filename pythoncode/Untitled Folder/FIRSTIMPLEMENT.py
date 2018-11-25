from tkinter import *
import random
import time
import datetime
import numbers
from tkinter import messagebox

root = Tk()
root.geometry("1350x650+0+0")
root.title("Restaurant Billing System")

Tops = Frame(root, width=1350, height=50, bd=8, relief="raise")
Tops.pack(side=TOP)
Bottoms = Frame(root, width=1350, height=50, bd=8, relief="raise")
Bottoms.pack(side=BOTTOM)

f1 = Frame(root, width=900, height=650, bd=8, relief="raise")
f1.pack(side=LEFT)
f1a = Frame(f1, width=900, height=330, bd=8, relief="raise")
f1a.pack(side=TOP)
f2a = Frame(f1, width=900, height=320, bd=8, relief="raise")
f2a.pack(side=BOTTOM)

f1aa = Frame(f1a, width=400, height=430, bd=8, relief="raise")
f1aa.pack(side=LEFT)
f1ab = Frame(f1a, width=400, height=430, bd=8, relief="raise")
f1ab.pack(side=RIGHT)

f2aa = Frame(f2a, width=450, height=330, bd=8, relief="raise")
f2aa.pack(side=LEFT)
f2ab = Frame(f2a, width=450, height=330, bd=8, relief="raise")
f2ab.pack(side=LEFT)

f2 = Frame(root, width=440, height=650, bd=8, relief="raise")
f2.pack(side=RIGHT)

lblInfo = Label(Tops, font=('arial', 25, 'bold'), text="Restaurant Billing System", bd=10, anchor='w')
lblInfo.grid(row=0, column=0)
lblcopyright = Label(Bottoms, font=('arial', 10, 'italic'), text="Created by Raisul Islam", bd=0, anchor='w')
lblcopyright.grid(row=0, column=0)
#==============================Variables=====================
PaymentRef=StringVar()
chickenBurgers=StringVar()
beefBurgers=StringVar()
frenchFries=StringVar()
softDrinks=StringVar()
costchickenBurgers=StringVar()
costbeefBurgers=StringVar()
costfrenchFries=StringVar()
costsoftDrinks=StringVar()
dateRef=StringVar()
subTotal=StringVar()
vat=StringVar()
totalPrice=StringVar()
text_Input = StringVar()
dateRef.set(time.strftime("%d/%m/%y"))
operator = ""
vat.set(0)
chickenBurgers.set(0)
beefBurgers.set(0)
frenchFries.set(0)
softDrinks.set(0)
subTotal.set(0)
totalPrice.set(0)
costchickenBurgers.set(160)
costbeefBurgers.set(180)
costsoftDrinks.set(20)
costfrenchFries.set(80)

#=============================Functions==================
def tPrice():
    cBprice=int(costchickenBurgers.get())
    bBprice=int(costbeefBurgers.get())
    fFprice=int(costfrenchFries.get())
    sDprice=int(costsoftDrinks.get())

    cBno=int(chickenBurgers.get())
    bBno=int(beefBurgers.get())
    fFno=int(frenchFries.get())
    sDno=int(softDrinks.get())
    tempVat=int(vat.get())
    subPrice=(cBprice*cBno+bBprice*bBno+fFprice*fFno+sDprice*sDno)
    totalCost=str('%d'%subPrice),"Tk"
    totalCostwithVat=str('%d'%(subPrice +(subPrice*tempVat)/100)),"Tk"
    subTotal.set(totalCost)
    totalPrice.set(totalCostwithVat)


def iExit():
    qexit= messagebox.askyesno("Billing System", "Do you want to exit?")
    if qexit>0:
        root.destroy()
        return

def reset():
    PaymentRef.set("")
    chickenBurgers.set(0)
    beefBurgers.set(0)
    frenchFries.set(0)
    softDrinks.set(0)
    subTotal.set(0)
    totalPrice.set(0)

def refNo():
    x =  random.randint(10034, 699812)
    randomRef= str(x)
    PaymentRef.set("BILL"+randomRef)

def btnClick(numbers):
    global operator
    operator = operator + str(numbers)
    text_Input.set(operator)


def btnClearDisplay():
    global operator
    operator = ""
    text_Input.set("")


def btnEqualsInput():
    global operator
    sumup = str(eval(operator))
    text_Input.set(sumup)
    operator = ""
