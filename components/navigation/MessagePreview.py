import tkinter as tk

class MessagePreview(tk.Frame):

    def __init__(self, master, sender, content, highlighted):
        if highlighted:
            highlighted_background = "#AFCA0B"
        else:
            highlighted_background = "#131A1C"

        super().__init__(master, highlightbackground=highlighted_background, highlightthickness=2, cursor="hand2")
        
        self.message_sender = tk.Label(self, text=sender, anchor=tk.W, bg="white")
        self.message_sender.configure(font=("Open Sans", 10, "bold"))
        self.message_sender.pack(side=tk.TOP, fill=tk.X)
        
        self.message_content_preview = tk.Label(self, text=content, anchor=tk.W, bg="white")
        self.message_content_preview.configure(font=("Open Sans", 10))
        self.message_content_preview.pack(side=tk.TOP, fill=tk.X)

        self.pack(side=tk.TOP, fill=tk.X, padx=10, pady=10)

