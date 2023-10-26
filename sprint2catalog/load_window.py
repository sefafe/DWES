import tkinter as tk
import requests

class LoadingWindow:
    def __init__(self, root, launch_main_window):
        
        self.root = root
        self.root.title("Cargando...")
        self.root.geometry("170x120")
        self.root.resizable(False, False)

        self.label = tk.Label(self.root, text="Cargando datos...", font=("Arial", 14))
        self.label.pack(side=tk.TOP, pady=10)

        label_bg_color = self.label.cget("bg")

        self.canvas = tk.Canvas(self.root, width=60, height=60, bg=label_bg_color)
        self.canvas.pack()

        self.progress = 0

        self.draw_progress_circle(self.progress)

        self.update_progress_circle()

        self.finished = False
        self.json_data = []

        self.launch_main_window = launch_main_window

        try:
            self.fetch_json_data()
        except Exception as e:
            print(e)
            self.root.destroy()
            return

        self.check_thread()

        loading_width = 170
        loading_height = 120
        screen_width = root.winfo_screenwidth()
        screen_height = root.winfo_screenheight()
        x = (screen_width // 2) - (loading_width // 2)
        y = (screen_height // 2) - (loading_height // 2)
        self.root.geometry(f"{loading_width}x{loading_height}+{x}+{y}")

    def draw_progress_circle(self, progress):
        self.canvas.delete("progress")
        angle = int(360 * (progress / 100))

        self.canvas.create_arc(10, 10, 35, 35,
                               start=0, extent=angle, tags="progress", outline="green", width=4, style=tk.ARC)

    def update_progress_circle(self):
        if self.progress < 100:
            self.progress += 5
        else:
            self.progress = 0

        self.draw_progress_circle(self.progress)
        self.root.after(100, self.update_progress_circle)

    def fetch_json_data(self):
        response = requests.get("https://raw.githubusercontent.com/sefafe/DWES/main/recursos/catalog.json")
        if response.status_code == 200:
            self.json_data = response.json()
        else:
            raise Exception(f"HTTP request failed with status code {response.status_code}")
        self.finished = True

    def check_thread(self):
        if self.finished:
            self.root.after(2000, self.launch_main_window, self.json_data)  # Muestra la ventana principal después de 2 segundos
            self.root.after(2000, self.root.destroy)  # Cierra la ventana de carga después de 2 segundos
        else:
            self.root.after(100, self.check_thread)


