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

class AllMessagesLabel:

    def __init__(self, master, count):
        frm_all_messages_label = tk.Frame(master)

        self.all_messages_label_text = tk.Label(frm_all_messages_label, text="All messages (" + str(count) + ")")
        self.all_messages_label_text.configure(font=("Open Sans", 12, "bold"))
        self.all_messages_label_text.pack(side=tk.LEFT, padx=(10,10), pady=10)

        frm_all_messages_label.grid(column=0, row=0, sticky="ew")

class AllMessagesToDisplay:

    def __init__(self, master):
        frm_all_messages_to_display = tk.Frame(master)

        for i in range(5):
            if i == 0:
                i = MessagePreview(frm_all_messages_to_display, "User", "Lorem Ipsum...", True)
            else:
                i = MessagePreview(frm_all_messages_to_display, "User", "Lorem Ipsum...", False)

        frm_all_messages_to_display.grid(column=0, row=1, sticky="nsew")
