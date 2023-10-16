from tkinter import ttk, messagebox
import tkinter as tk
from cell import Cell
from detail_window import DetailWindow

class MainWindow():

    def onButtonClicked(self, cell):

        
        detail_window = DetailWindow(self.root, cell.title, cell.imageTk, cell.description)  #Cuando haces click sale un mensaje


    def _init_(self, root):
        
        
        root.title("5 libros de Brandon Sanderson") #Título de la ventana
        self.root = root

        
        self.cells = [       #Celdas con el título y su ruta definidos

            Cell("AC Brotherhood", "C:\\Users\\Megaport\\Downloads\\Python\\catalog\\data\\unedited\\acbrotherhood.jpg", "En el Renacimiento italiano, como miembro de la hermandad de asesinos, luchas por la libertad y la justicia en un contexto de conspiraciones y conflictos."),
            Cell("Dishonored","C:\\Users\\Megaport\\Downloads\\Python\\catalog\\data\\unedited\\dishonored.jpg", "En una ciudad steampunk, encarnas a un vengador silencioso con habilidades sobrenaturales. Te deslizas entre las sombras en misiones de sigilo y retribución."),
            Cell("Skyrim","C:\\Users\\Megaport\\Downloads\\Python\\catalog\\data\\unedited\\skyrim.jpg", "Un épico videojuego de rol que te sumerge en una fantasía nórdica, donde enfrentas dragones y forjas tu destino en un vasto mundo abierto."),
            Cell("Diablo IV", "C:\\Users\\Megaport\\Downloads\\Python\\catalog\\data\\unedited\\diabloIV.jpg", "Adéntrate en un mundo desolado y devastado por demonios. En este juego de rol de acción, libras batallas épicas y desatas poderes arcanos en un conflicto eterno entre el bien y el mal."),
            Cell("Rainbow Six Siege", "C:\\Users\\Megaport\\Downloads\\Python\\catalog\\data\\unedited\\rainbowsix.jpg", "Experimenta la emoción de operaciones tácticas en equipos. Enfréntate en asedios explosivos como un operativo especial, en un ambiente de competencia intensa.")

        ]
        
        for i, cell in enumerate(self.cells): #Bucle para leer la lista

            label = ttk.Label(root, image = cell.imageTk, text = cell.title, compound = tk.BOTTOM)
            label.grid(row = 0,column = i)
            label.bind("<Button-1>",lambda event, cell = cell: self.onButtonClicked(cell))