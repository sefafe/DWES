import tkinter as tk
import tkinter.messagebox as messagebox


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

        menubar = tk.Menu(root)
        help_menu = tk.Menu(menubar, tearoff=0)
        help_menu.add_command(label="Acerca de", command=self.show_about_dialog)
        menubar.add_cascade(label="Ayuda", menu=help_menu)
        root.config(menu=menubar)

        window_width = 800
        window_height = 600
        screen_width = root.winfo_screenwidth()
        screen_height = root.winfo_screenheight()
        x = (screen_width // 2) - (window_width // 2)
        y = (screen_height // 2) - (window_height // 2)
        self.root.geometry(f"{window_width}x{window_height}+{x}+{y}")

    def show_about_dialog(self):
        about_text = "Acerca del desarrollador:\n\nMe gusta la mantequilla, y también los cacahuetes, pero no me gusta la mantequilla de cacahuete, que raro."
        messagebox.showinfo("Acerca de", about_text)

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
