import tkinter as tk
from load_window import LoadingWindow
from window import launch_main_window

def main():
    root = tk.Tk()
    app = LoadingWindow(root, launch_main_window)
    root.mainloop()

if __name__ == "__main__":
    main()
