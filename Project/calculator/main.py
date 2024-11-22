import tkinter as ttk
import math
            #Настройка
root = ttk.Tk()
root.title("Calculator")
root.geometry("500x200")
root.resizable(False, False)
root.configure(bg="#b0b8b5")
            #Логика кнопок
def commandPlus():
    try: 
        LblInfo["text"] = str(float(entryNumb1.get()) + float(entryNumb2.get()))
        LblInfo.delete(0, 100)
        LblInfo.insert(0, str(float(entryNumb1.get()) + float(entryNumb2.get())))
    except:
        LblInfo["text"] = "e"
        
def commandMinus():
    try: 
        LblInfo["text"] = str(float(entryNumb1.get()) - float(entryNumb2.get()))
        LblInfo.delete(0, 100)
        LblInfo.insert(0, str(float(entryNumb1.get())- float(entryNumb2.get())))
    except:
        LblInfo["text"] = "e"

def commandMultiply():
    try: 
        LblInfo["text"] = str(float(entryNumb1.get()) * float(entryNumb2.get()))
        LblInfo.delete(0, 100)
        LblInfo.insert(0, str(float(entryNumb1.get()) * float(entryNumb2.get())))
    except:
        LblInfo["text"] = "e"
    
def commandDevide():
    try: 
        LblInfo["text"] = str(float(entryNumb1.get()) / float(entryNumb2.get()))
        LblInfo.delete(0, 100)
        LblInfo.insert(0, str(float(entryNumb1.get()) / float(entryNumb2.get())))
    except:
        LblInfo["text"] = "e"
        
def commandCE():
    LblInfo.delete(0, 100)
    entryNumb1.delete(0, 100)
    entryNumb2.delete(0, 100)

def commandSqrt():
    try:
        LblInfo.delete(0, 100)
        LblInfo.insert(0, str(math.pow(float(entryNumb1.get()),1/float(entryNumb2.get()))))
    except:
        LblInfo["text"] = "e"
        
def commandDegr():
    try:
        LblInfo.delete(0, 100)
        LblInfo.insert(0, str(math.pow(float(entryNumb1.get()), float(entryNumb2.get()))))
    except:
        LblInfo["text"] = "e"
            #Инициализация входных данных      
entryNumb1 = ttk.Entry(relief="ridge", highlightbackground="red", highlightcolor="red", font=("Arial", 24))
entryNumb2 = ttk.Entry(relief="ridge", highlightbackground="red", highlightcolor="red", font=("Arial", 24))
            #Инициализация кнопок
btnPlus = ttk.Button(text = "+", command = commandPlus)
btnMinus = ttk.Button(text = "-", command = commandMinus)
btnMultiply = ttk.Button(text = "*", command = commandMultiply)
btnDevide = ttk.Button(text = "/", command = commandDevide)
btnCE = ttk.Button(text = "CE", command = commandCE)
ALL = [btnPlus, btnMinus, btnMultiply, btnDevide, btnCE]
btnPlus = ttk.Button(text = "+", command=commandPlus, borderwidth=2)
btnMinus = ttk.Button(text = "-", command=commandMinus, borderwidth=2)
btnMultiply = ttk.Button(text = "*", command=commandMultiply, borderwidth=2)
btnDevide = ttk.Button(text = "/", command=commandDevide, borderwidth=2)
btnCE = ttk.Button(text = "CE", command=commandCE)
btnSqrt = ttk.Button(text = "√", command=commandSqrt)
btnDegr = ttk.Button(text =  "a^x", command=commandDegr)
ALL = [btnPlus, btnMinus, btnMultiply, btnDevide, btnCE, btnSqrt, btnDegr]
            #Инициализация ввода
LblInfo = ttk.Entry(text = "0", font=("Arial", 25), justify = "center", background="#b0b8b5")
#Вывод на экран:
for i in ALL:
    i.config(width = 10, height = 2, borderwidth = 2)

for c in range(3): root.columnconfigure(index = c , weight = 1)
for r in range(3): root.rowconfigure(index = r, weight = 1)

entryNumb1.grid(row = 1, column = 1)
entryNumb2.grid(row = 2, column = 1)

btnPlus.grid(row = 1, column = 0)
btnMinus.grid(row = 2, column = 0)
btnMultiply.grid(row = 1, column = 2)
btnDevide.grid(row = 2, column = 2)
btnSqrt.grid(row = 3, column = 0)
btnDegr.grid(row = 3, column = 1)
btnCE.grid(row = 0, column = 2)

LblInfo.grid(row = 0, column = 1)


root.mainloop()