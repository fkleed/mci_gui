import tkinter as tk
import sys

sys.path.append('../shared')

from components.navigation.MessagePreview import MessagePreview
from shared.Message import Message

class ImportantMessages(tk.Frame):

    def __init__(self, master):
        super().__init__(master)
        
        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=0)
        self.rowconfigure(1, weight=1)

        self.important_messages_label = ImportantMessagesLabel(self)
        self.important_messages_to_display = ImportantMessagesToDisplay(self)

        self.important_messages_to_display.add_important_message(Message("Guido W", "-Test"))

        self.grid(column=0, row=0, sticky="nsew")

class ImportantMessagesLabel(tk.Frame):

    def __init__(self, master):
        super().__init__(master)

        self.important_messages_label_text = tk.Label(self, text="Important messages")
        self.important_messages_label_text.configure(font=("Open Sans", 12, "bold"))
        self.important_messages_label_text.pack(side=tk.LEFT, padx=(10,10), pady=10)

        self.grid(column=0, row=0, sticky="ew")

class ImportantMessagesToDisplay(tk.Frame):

    def __init__(self, master):
        super().__init__(master)
        self.grid(column=0, row=1, sticky="nsew")

    def add_important_message(self, message):
        MessagePreview(self, message.sender, message.text, False)