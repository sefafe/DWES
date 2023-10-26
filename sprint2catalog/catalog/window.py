import tkinter as tk
from tkinter import ttk
from cell import Cell


class MainWindow:
    cells=[]
    def __init__(self,root,json_data):
        self.root=root
        root.title("Videojuegos")
        for videojuego in json_data:
            name=videojuego.get("name")
            description=videojuego.get("description")
            image_url=videojuego.get("image_url")
            cell=Cell(name,image_url,description)
            self.cells.append(cell)
            self.show_cells() #Método para mostrar las celdas


    def show_cells(self):
        for i,cell in enumerate(self.cells):
            label=ttk.Label(self.root, image=cell.image_tk,text=cell.title,compund=tk.BOTTOM) #Imagen y titulo del label
            label.grid(row=i,column=0)
