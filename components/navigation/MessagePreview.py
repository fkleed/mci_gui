import tkinter as tk

class MessagePreview:

    def __init__(self, master, sender, content, highlighted):
        if highlighted:
            highlighted_background = "#AFCA0B"
        else:
            highlighted_background = "#131A1C"

        frm_message_preview = tk.Frame(master, highlightbackground=highlighted_background, highlightthickness=2, cursor="hand2")
        
        self.message_sender = tk.Label(frm_message_preview, text=sender, anchor=tk.W, bg="white")
        self.message_sender.configure(font=("Open Sans", 10, "bold"))
        self.message_sender.pack(side=tk.TOP, fill=tk.X)
        
        self.message_content_preview = tk.Label(frm_message_preview, text=content, anchor=tk.W, bg="white")
        self.message_content_preview.configure(font=("Open Sans", 10))
        self.message_content_preview.pack(side=tk.TOP, fill=tk.X)

        frm_message_preview.pack(side=tk.TOP, fill=tk.X, padx=10, pady=10)

