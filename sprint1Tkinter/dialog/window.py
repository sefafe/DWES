from tkinter import ttk, Button, Label

class MainWindow:
    def on_button_click(self):
        pass
    def __init__(self,root):
        self.root=root
        self.label=Label(root, text="Prueba")
        self.label.pack()
        self.button=ttk.Button(self.root, text="Realizar acción", command=self.on_button_click)
        self.button.pack()
        