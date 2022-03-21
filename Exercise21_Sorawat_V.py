from tkinter import *
import math

def leftClick(E):
    x = float(textboxWeight.get())
    y = math.pow(float(textboxHeight.get()) / 100, 2)
    z = x/y
    labelCalBMI2.configure(text=z)
    if z >= 30:
        labelCalBMI4.configure(text="อ้วนมาก")
    elif z>=25 and z<=29.9:
        labelCalBMI4.configure(text="อ้วน")
    elif z>=23 and z<=24.9:
        labelCalBMI4.configure(text="น้ำหนักเกิน")
    elif z>=18.6 and z<=22.9:
        labelCalBMI4.configure(text="น้ำหนักปกติ")
    else:
        labelCalBMI4.configure(text="ผอมเกินไป")

windows = Tk()
windows.title("BMI Testing")
windows.geometry("250x150")
labelWeight = Label(windows,text="น้ำหนัก (Kg.)")
labelWeight.grid(row=0,column=0)
textboxWeight = Entry(windows)
textboxWeight.grid(row=0,column=1)
labelHeight = Label(windows,text="ส่วนสูง (cm.)")
labelHeight.grid(row=1,column=0)
textboxHeight = Entry(windows)
textboxHeight.grid(row=1,column=1)
calButton = Button(windows,text="คำนวณค่า BMI")
calButton.grid(row=3,column=1)
labelspace = Label(windows, text="")
labelspace.grid(row=4)
labelCalBMI = Label(windows,text="ค่า BMI : ")
labelCalBMI.grid(row=5,column=0)
labelCalBMI2 = Label(windows,text=" - ")
labelCalBMI2.grid(row=5,column=1)
labelcalBMI3 = Label(windows,text= "ผลลัพธ์ : ")
labelcalBMI3.grid(row=6,column=0)
labelCalBMI4 = Label(windows,text=" - ")
labelCalBMI4.grid(row=6,column=1)
calButton.bind('<Button-1>', leftClick)

windows.mainloop()
