import tkinter as tk

def open_window():
    ventana = tk.Tk()
    etiqueta_yes = tk.Label(ventana, text="Me alegro")
    etiqueta_yes.pack()
    ventana.mainloop()