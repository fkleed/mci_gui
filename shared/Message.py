class Message:
    sender = ""
    text = ""
    priority = "default"

    def __init__(self, sender, text):
        self.sender = sender
        self.text = text