import tkinter as tk


class TopLabel:
    
    def __init__(self, master):
        top_label = tk.Label(master, text="MCI Chat", bg="#131A1C", fg="#AFCA0B", pady=10)
        top_label.configure(font=("Open Sans", 24, "bold"))
        top_label.grid(column=0, columnspan=2, row=0, sticky="ew")