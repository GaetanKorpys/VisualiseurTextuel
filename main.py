import tkinter as tk
from VisualiseurTextuel import VisualiseurTextuel

if __name__ == '__main__':

    root = tk.Tk()
    root.title("Visualiseur Textuel")
    root.geometry("400x100")
    visualiseurTextuel = VisualiseurTextuel(root)
    root.mainloop()