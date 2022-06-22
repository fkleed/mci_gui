import tkinter as tk
from tkinter import messagebox

class NewMessage(tk.Frame):
    def __init__(self, master):
        super().__init__(master)

        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=0)
        self.rowconfigure(1, weight=1)
        self.rowconfigure(2, weight=0)


        self.new_messages_label = NewMessageLabel(self)
        self.new_message_text = NewMessageText(self)
        self.new_message_button = NewMessageButton(self)

        # add handler to new message button
        self.new_message_button.send_btn["command"] = self.submit 

        self.grid(column=1, row=0, rowspan=2, sticky="nsew")

    def submit(self):
        messagebox.showinfo("Success!", "Your message has been sent!")
        self.new_message_text.message.delete("1.0", tk.END)

class NewMessageLabel(tk.Frame):
    def __init__(self, master):
        super().__init__(master)

        self.new_message_label_text = tk.Label(self, text="Type New Message")
        self.new_message_label_text.configure(font=("Open Sans", 12, "bold"))
        self.new_message_label_text.pack(side=tk.LEFT, padx=(10, 10), pady=10)

        self.grid(column=0, row=0, sticky="ew")

class NewMessageText(tk.Frame): 
    def __init__(self, master):
        super().__init__(master)

        self.message = tk.Text(self, height = 20)
        self.message.configure(font=("Open Sans", 10))
        self.message.pack(side=tk.TOP, padx=(10, 10), fill=tk.X)

        self.grid(column = 0, row=1, sticky="nsew")

class NewMessageButton(tk.Frame):
    def __init__(self, master):
        super().__init__(master)

        self.send_btn = tk.Button(self, text="SEND", bg="#AFCA0B", fg="#131A1C", cursor="hand2", width=10)
        self.send_btn.configure(font=("Open Sans", 12, "bold"))
        self.send_btn.pack(side=tk.RIGHT, padx=(10, 10), pady=10)

        self.grid(column=0, row=2, sticky="ew")
