import tkinter as tk

class MainWindow:
    def __init__(self, root, json_data):
        self.root = root
        self.json_data = json_data
        self.root.title("Videojuegos")
        self.root.geometry("800x600")
        self.root.resizable(True, True)

        self.catalog_frame = tk.Frame(self.root)
        self.catalog_frame.pack(fill=tk.BOTH, expand=True)

        self.game_list = tk.Listbox(self.catalog_frame, selectmode=tk.SINGLE)
        self.game_list.pack(fill=tk.BOTH, expand=True)

        self.load_games()

        self.game_list.bind("<<ListboxSelect>>", self.show_details)

    def load_games(self):
        for game in self.json_data:
            self.game_list.insert(tk.END, game["name"])

    def show_details(self, event):
        selection = self.game_list.curselection()
        if selection:
            index = selection[0]
            selected_game = self.json_data[int(index)]
            detail_window = tk.Toplevel(self.root)
            detail_window.title(selected_game["name"])
            detail_label = tk.Label(detail_window, text=f"Descripción: {selected_game['description']}")
            detail_label.pack()
            # Agrega más etiquetas y widgets para mostrar otros detalles

def launch_main_window(json_data):
    root = tk.Tk()
    app = MainWindow(root, json_data)
    root.mainloop()
