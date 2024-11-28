import tkinter as tk
import random
import math

root = tk.Tk()
root.title("Программа для заметок")
root.geometry("500x500")
root.resizable(False, False)
root.configure(bg="#b0b8b5")

editor = tk.Text()
editor.pack(fill="both", expand=1)

def Exx():
    root.destroy()

root.option_add("*tearOff", False)
 
main_menu = tk.Menu()
 
file_menu = tk.Menu()
file_menu.add_command(label="New")
file_menu.add_command(label="Save")
file_menu.add_command(label="Save as")
file_menu.add_command(label="Open")
file_menu.add_separator()
file_menu.add_command(label="Exit", command=Exx)
 
main_menu.add_cascade(label="File", menu=file_menu)
 

 
Value = editor.get("1.0", "end")
 
 
root.config(menu=main_menu)














root.mainloop()