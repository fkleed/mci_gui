import tkinter as tk
from PIL import ImageTk, Image

# import required components
from components.layout.TopLabel import TopLabel
from components.navigation.Navigation import Navigation

# create the root window and configure it
root = tk.Tk()
root.title("MCI Chat")

window_width = 1200
window_height = 600
root.geometry(f'{window_width}x{window_height}')

root.minsize(1200, 600)
root.iconphoto(False, ImageTk.PhotoImage(file='./assets/images/favicon.png'))
root.configure(bg="white")

root.columnconfigure(0, weight=1)
root.columnconfigure(1, weight=3)
root.rowconfigure(0, weight=0)
root.rowconfigure(1, weight=1)

# defining the components
top_label = TopLabel(root).top_label
navigation = Navigation(root).frm_navigation

# creating the gui
top_label.grid(column=0, columnspan=2, row=0, sticky="ew")
navigation.grid(column=0, row=1, sticky="nsew")


root.mainloop()