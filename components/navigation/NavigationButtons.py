import tkinter as tk

class NavigationButtons(tk.Frame):

    def __init__(self, master):
        super().__init__(master)

        self.btn_important_messages = tk.Button(self, text="Important messages", bg="#AFCA0B", fg="#131A1C", cursor="hand2")
        self.btn_important_messages.configure(font=("Open Sans", 12, "bold"))
        self.btn_important_messages.pack(side=tk.LEFT, padx=(10,5), pady=10)

        self.btn_all_messages = tk.Button(self, text="All messages", bg="#AFCA0B", fg="#131A1C", cursor="hand2")
        self.btn_all_messages.configure(font=("Open Sans", 12, "bold"))
        self.btn_all_messages.pack(side=tk.LEFT, padx=(10,5), pady=10)

        self.btn_new_message = tk.Button(self, text="New message", bg="#AFCA0B", fg="#131A1C", cursor="hand2")
        self.btn_new_message.configure(font=("Open Sans", 12, "bold"))
        self.btn_new_message.pack(side=tk.LEFT, padx=(5,10), pady=10)

        self.grid(column=0, row=1, sticky="ew")