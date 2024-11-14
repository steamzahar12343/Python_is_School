from tkinter import *
from tkinter import ttk

root = Tk()
root.title("Calculator")
root.geometry("200x100")
root.resizable(False, False)

def commandPlus():
    pass

entryNumb1 = ttk.Entry()
entryNumb2 = ttk.Entry()
btnPlus = ttk.Button(text = "+", command=commandPlus)
btnMinus = ttk.Button(text = "-")
btnDevide = ttk.Button(text = "/")
btnMultiply = ttk.Button(text = "*")
#btnResult = ttk.Button(text = "=", width=20)
LblInfo = ttk.Label(text = "test//")

entryNumb1.grid(row=0,column=0)
entryNumb2.grid(row=1,column=0)
btnPlus.grid(row=0,column=1)
btnMinus.grid(row=1,column=1)
btnDevide.grid(row=2,column=1)
btnMultiply.grid(row=3,column=1)
#btnResult.grid(row=2,column=0)
LblInfo.grid(row=3,column=0)

#entryNumb1.pack(anchor="nw")
#entryNumb2.pack(anchor="nw")

#btnPlus.pack()
#btnMinus.pack()
#btnDevide.pack()
#btnMultiply.pack() 
#btnResult.pack()
#LblInfo.pack()
root.mainloop()