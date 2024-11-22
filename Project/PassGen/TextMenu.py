import tkinter as tk
from tkinter import ttk

class EntryEx(ttk.Entry):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.menu = tk.Menu(self, tearoff=False)
        self.menu.add_command(label="Copy", command=self.popup_copy)
        self.menu.add_command(label="Paste", command=self.popup_paste)
        self.bind("<Button-3>", self.display_popup)

    def display_popup(self, event):
        self.menu.post(event.x_root, event.y_root)
    def popup_copy(self):
        self.event_generate("<<Copy>>")
    def popup_paste(self):
        self.event_generate("<<Paste>>")