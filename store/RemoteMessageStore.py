class RemoteMessageStore:
    stored_messages = []

    def get_all_messages(self):
        return self.stored_messages

    def get_important_messages(self):
        important_messages = [m for m in self.stored_messages if m.priority == "important"]
        return important_messages

    def add_new_message(self, message):
        self.stored_messages.append(message)

    def print_stored_messages(self):
        for message in self.stored_messages:
            print("Sender: " + message.sender)
            print("Text: " + message.text)
            print("Priority: " + message.priority)

    