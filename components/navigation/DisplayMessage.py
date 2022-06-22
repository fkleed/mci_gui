import tkinter as tk

class DisplayMessage(tk.Frame):
    def __init__(self, master):
        super().__init__(master)

        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=0)
        self.rowconfigure(1, weight=0)


        self.sender_messages_label = SenderMessageLabel(self)
        self.display_message_text = DisplayMessageText(self)

        self.grid(column=1, row=0, rowspan=2, sticky="nsew")

class SenderMessageLabel(tk.Frame):
    def __init__(self, master):
        super().__init__(master)

        self.sender_message_label_text = tk.Label(self, text="User")
        self.sender_message_label_text.configure(font=("Open Sans", 12, "bold"))
        self.sender_message_label_text.pack(side=tk.LEFT, padx=(10, 10), pady=10)

        self.grid(column=0, row=0, sticky="ew")

class DisplayMessageText(tk.Frame): 
    def __init__(self, master):
        super().__init__(master)

        self.message = tk.Message(self, text="Content")
        self.message.configure(font=("Open Sans", 10))
        self.message.pack(side=tk.LEFT, padx=(10, 10), fill=tk.X)

        self.grid(column = 0, row=1, sticky="nsew")
