import tkinter as tk

from components.navigation.NavigationButtons import NavigationButtons
from components.navigation.ImportantMessages import ImportantMessages

class Navigation:

    def __init__(self, master):
        self.frm_navigation = tk.Frame(master)
        self.frm_navigation.columnconfigure(0, weight=1)
        self.frm_navigation.rowconfigure(0, weight=1)
        self.frm_navigation.rowconfigure (1, weight=0)

        navigation_buttons = NavigationButtons(self.frm_navigation).frm_navigation_buttons
        important_messages = ImportantMessages(self.frm_navigation).frm_important_messages

        navigation_buttons.grid(column=0, row=1, sticky="ew")
        important_messages.grid(column=0, row=0, sticky="nsew")


