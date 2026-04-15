import tkinter as tk
from database import crear_tabla
from ui import App

crear_tabla()

root = tk.Tk()
app = App(root)
root.mainloop()