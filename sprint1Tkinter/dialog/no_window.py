import tkinter as tk

def open_window():
    ventana = tk.Tk()
    etiqueta_no = tk.Label(ventana, text="Mala suerte")
    etiqueta_no.pack()
    ventana.mainloop()
