import tkinter as tk

from components.navigation.NavigationButtons import NavigationButtons
from components.navigation.ImportantMessages import ImportantMessages
from components.navigation.AllMessages import AllMessags

class Navigation:

    def __init__(self, master):
        frm_navigation = tk.Frame(master)
        frm_navigation.columnconfigure(0, weight=0)
        frm_navigation.columnconfigure(1, weight=1)
        frm_navigation.rowconfigure(0, weight=1)
        frm_navigation.rowconfigure (1, weight=0)

        self.navigation_buttons = NavigationButtons(frm_navigation)
        self.all_messages = AllMessags(frm_navigation)
        self.important_messages = ImportantMessages(frm_navigation)

        # add handlers to navigation buttons
        self.navigation_buttons.btn_all_messages["command"] = self.show_all_messages
        self.navigation_buttons.btn_important_messages["command"] = self.show_important_messages

        frm_navigation.grid(column=0, row=1, sticky="nsew")

    def show_all_messages(self):
        self.all_messages.tkraise()

    def show_important_messages(self):
        self.important_messages.tkraise()
