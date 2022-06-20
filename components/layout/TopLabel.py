import tkinter as tk


class TopLabel:
    
    def __init__(self, master):
        self.top_label = tk.Label(master, text="MCI Chat", bg="#131A1C", fg="#AFCA0B", pady=10)
        self.top_label.configure(font=("Open Sans", 24, "bold"))