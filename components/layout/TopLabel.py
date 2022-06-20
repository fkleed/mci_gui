import tkinter as tk


class TopLabel(tk.Label):
    
    def __init__(self, master):
        super().__init__(master, text="MCI Chat", bg="#131A1C", fg="#AFCA0B", pady=10)

        self.configure(font=("Open Sans", 24, "bold"))
        self.grid(column=0, columnspan=2, row=0, sticky="ew")