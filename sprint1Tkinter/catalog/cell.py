import tkinter as tk
from PIL import Image, ImageTk

class Cell:

    def _init_(self, title, path):

        self.title = title
        self.path = path
        
        resizedImage = (Image.open(self.path)).resize((100, 100), Image.Resampling.LANCZOS)
        self.imageTk = ImageTk.PhotoImage(resizedImage)