import tkinter as tk

from components.navigation.MessagePreview import MessagePreview

class AllMessags:

    def __init__(self, master):
        self.frm_all_messages = tk.Frame(master)
        self.frm_all_messages.columnconfigure(0, weight=1)
        self.frm_all_messages.rowconfigure(0, weight=0)
        self.frm_all_messages.rowconfigure(1, weight=1)

        all_messages_label = AllMessagesLabel(self.frm_all_messages, 5).frm_all_messages_label
        all_messages_to_display = AllMessagesToDisplay(self.frm_all_messages).frm_all_messages_to_display

        all_messages_label.grid(column=0, row=0, sticky="ew")
        all_messages_to_display.grid(column=0, row=1, sticky="nsew")

class AllMessagesLabel:

    def __init__(self, master, count):
        self.frm_all_messages_label = tk.Frame(master)

        self.all_messages_label_text = tk.Label(self.frm_all_messages_label, text="All messages (" + str(count) + ")")
        self.all_messages_label_text.configure(font=("Open Sans", 12, "bold"))
        self.all_messages_label_text.pack(side=tk.LEFT, padx=(10,10), pady=10)

class AllMessagesToDisplay:

    def __init__(self, master):
        self.frm_all_messages_to_display = tk.Frame(master)

        for i in range(5):
            if i == 0:
                i = MessagePreview(self.frm_all_messages_to_display, "User", "Lorem Ipsum...", True).frm_message_preview
                i.pack(side=tk.TOP, fill=tk.X, padx=10, pady=10)
            else:
                i = MessagePreview(self.frm_all_messages_to_display, "User", "Lorem Ipsum...", False).frm_message_preview
                i.pack(side=tk.TOP, fill=tk.X, padx=10, pady=10)