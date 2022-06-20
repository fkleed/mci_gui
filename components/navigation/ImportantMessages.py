import tkinter as tk

from components.navigation.MessagePreview import MessagePreview

class ImportantMessages:

    def __init__(self, master):
        frm_important_messages = tk.Frame(master)
        frm_important_messages.columnconfigure(0, weight=1)
        frm_important_messages.rowconfigure(0, weight=0)
        frm_important_messages.rowconfigure(1, weight=1)

        self.important_messages_label = ImportantMessagesLabel(frm_important_messages, 3)
        self.important_messages_to_display = ImportantMessagesToDisplay(frm_important_messages)

        frm_important_messages.grid(column=0, row=0, sticky="nsew")

class ImportantMessagesLabel:

    def __init__(self, master, count):
        frm_important_messages_label = tk.Frame(master)

        self.important_messages_label_text = tk.Label(frm_important_messages_label, text="Imortant messages (" + str(count) + ")")
        self.important_messages_label_text.configure(font=("Open Sans", 12, "bold"))
        self.important_messages_label_text.pack(side=tk.LEFT, padx=(10,10), pady=10)

        frm_important_messages_label.grid(column=0, row=0, sticky="ew")

class ImportantMessagesToDisplay:

    def __init__(self, master):
        frm_important_messages_to_display = tk.Frame(master)

        for i in range(3):
            if i == 0:
                i = MessagePreview(frm_important_messages_to_display, "User", "Lorem Ipsum...", True)
            else:
                i = MessagePreview(frm_important_messages_to_display, "User", "Lorem Ipsum...", False)

        frm_important_messages_to_display.grid(column=0, row=1, sticky="nsew")