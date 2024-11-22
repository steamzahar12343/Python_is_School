import tkinter as tk
import random
#from tkinter import ttk
import math
from TextMenu import EntryEx

root = tk.Tk()
root.title("PassGenerator")
root.geometry("330x60")
root.resizable(False, False)
root.configure(bg="#b0b8b5")
root.iconphoto(False, tk.PhotoImage(file="Project/PassGen/icon.png"))

def commandGenerate():
    lenPass = comb.get()
    strPass = ""
    keys = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z',
            'A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z',
            '1','2','3','4','5','6','7','8','9','0']
    spec = ['!','@','#','$','%','^','&']
    specUse = False
    KeyOrSpec = 0   
    for i in range(int(lenPass)):
        KeyOrSpec = random.randint(1,2)
        if(KeyOrSpec == 2 and specUse == False):
            strPass += random.choice(spec)
            specUse = True
        else:
            strPass += random.choice(keys)
    EntryPass.set(strPass)
    
lenPassList = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
EntryPass = tk.StringVar()

comb = tk.ttk.Combobox(values = lenPassList, state="readonly", font=("Arial", 14))
GenerateBtn = tk.Button(text="Generate", command=commandGenerate)
password = EntryEx(font=("Arial", 14), state="readonly", textvariable=EntryPass)

comb.config(width = 20, height = 10)
password.config(width = 22)
GenerateBtn.config(width = 10, height = 3, borderwidth = 2)

comb.grid(row=0, column=0)
GenerateBtn.grid(row=0, column=1, rowspan=2)
password.grid(row=1, column=0)

root.mainloop()