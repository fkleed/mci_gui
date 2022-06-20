import tkinter as tk

from components.navigation.MessagePreview import MessagePreview

class AllMessags(tk.Frame):

    def __init__(self, master):
        super().__init__(master)
        
        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=0)
        self.rowconfigure(1, weight=1)

        self.all_messages_label = AllMessagesLabel(self, 5)
        self.all_messages_to_display = AllMessagesToDisplay(self)

        self.grid(column=0, row=0, sticky="nsew")

class AllMessagesLabel(tk.Frame):

    def __init__(self, master, count):
        super().__init__(master)

        self.all_messages_label_text = tk.Label(self, text="All messages (" + str(count) + ")")
        self.all_messages_label_text.configure(font=("Open Sans", 12, "bold"))
        self.all_messages_label_text.pack(side=tk.LEFT, padx=(10,10), pady=10)

        self.grid(column=0, row=0, sticky="ew")

class AllMessagesToDisplay(tk.Frame):

    def __init__(self, master):
        super().__init__(master)

        for i in range(5):
            if i == 0:
                i = MessagePreview(self, "User", "Lorem Ipsum...", True)
            else:
                i = MessagePreview(self, "User", "Lorem Ipsum...", False)

        self.grid(column=0, row=1, sticky="nsew")
