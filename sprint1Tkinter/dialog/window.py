import tkinter as tk
from tkinter import ttk, Button, Label
import yes_window
import no_window

class MainWindow:
    def on_button1_click(self):
        yes_window.open_window()

    def on_button2_click(self):
        no_window.open_window()

    def __init__(self, root):
        self.root = root
        self.label = Label(root, text="¿Has tenido un buen día?")
        self.label.pack()
        self.button1 = ttk.Button(root, text="Si", command=self.on_button1_click)
        self.button2 = ttk.Button(root, text="No", command=self.on_button2_click)
        self.button1.pack(side="left")
        self.button2.pack(side="right")

root = tk.Tk()
app = MainWindow(root)
root.mainloop()
