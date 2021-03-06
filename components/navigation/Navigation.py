import tkinter as tk
from components.navigation.DisplayMessage import DisplayMessage

from components.navigation.NavigationButtons import NavigationButtons
from components.navigation.ImportantMessages import ImportantMessages
from components.navigation.AllMessages import AllMessags
from components.navigation.NewMessage import NewMessage

class Navigation(tk.Frame):

    def __init__(self, master):
        super().__init__(master)
        
        self.columnconfigure(0, weight=0)
        self.columnconfigure(1, weight=1)
        self.rowconfigure(0, weight=1)
        self.rowconfigure (1, weight=0)

        self.navigation_buttons = NavigationButtons(self)
        self.all_messages = AllMessags(self)
        self.important_messages = ImportantMessages(self)
        self.new_message = NewMessage(self)
        self.display_message = DisplayMessage(self)

        # add handlers to navigation buttons
        self.navigation_buttons.btn_all_messages["command"] = self.show_all_messages
        self.navigation_buttons.btn_important_messages["command"] = self.show_important_messages
        self.navigation_buttons.btn_new_message["command"] = self.show_new_message

        self.grid(column=0, row=1, sticky="nsew")

    def show_all_messages(self):
        self.all_messages.tkraise()
        self.display_message.tkraise()

    def show_important_messages(self):
        self.important_messages.tkraise()
        self.display_message.tkraise()

    def show_new_message(self):
        self.new_message.tkraise()
