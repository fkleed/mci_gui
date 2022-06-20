import tkinter as tk

from components.navigation.MessagePreview import MessagePreview

class ImportantMessages:

    def __init__(self, master):
        self.frm_important_messages = tk.Frame(master)
        self.frm_important_messages.columnconfigure(0, weight=1)
        self.frm_important_messages.rowconfigure(0, weight=0)
        self.frm_important_messages.rowconfigure(1, weight=1)

        important_messages_label = ImportantMessagesLabel(self.frm_important_messages, 3).frm_important_messages_label
        important_messages_to_display = ImportantMessagesToDisplay(self.frm_important_messages).frm_important_messages_to_display

        important_messages_label.grid(column=0, row=0, sticky="ew")
        important_messages_to_display.grid(column=0, row=1, sticky="nsew")

class ImportantMessagesLabel:

    def __init__(self, master, count):
        self.frm_important_messages_label = tk.Frame(master)

        self.important_messages_label_text = tk.Label(self.frm_important_messages_label, text="Imortant messages (" + str(count) + ")")
        self.important_messages_label_text.configure(font=("Open Sans", 12, "bold"))
        self.important_messages_label_text.pack(side=tk.LEFT, padx=(10,10), pady=10)

class ImportantMessagesToDisplay:

    def __init__(self, master):
        self.frm_important_messages_to_display = tk.Frame(master)

        for i in range(3):
            if i == 0:
                i = MessagePreview(self.frm_important_messages_to_display, "User", "Lorem Ipsum...", True).frm_message_preview
                i.pack(side=tk.TOP, fill=tk.X, padx=10, pady=10)
            else:
                i = MessagePreview(self.frm_important_messages_to_display, "User", "Lorem Ipsum...", False).frm_message_preview
                i.pack(side=tk.TOP, fill=tk.X, padx=10, pady=10)