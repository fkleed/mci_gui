import tkinter as tk
from PIL import ImageTk, Image

# import required components
from components.layout.TopLabel import TopLabel
from components.navigation.Navigation import Navigation

# create the root window and configure it
class Gui(tk.Tk):

    def __init__(self):
        super().__init__()
    
        self.title("MCI Chat")

        window_width = 1200
        window_height = 600
        self.geometry(f'{window_width}x{window_height}')

        self.minsize(1200, 600)
        self.iconphoto(False, ImageTk.PhotoImage(file='./assets/images/favicon.png'))
        self.configure(bg="white")

        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=0)
        self.rowconfigure(1, weight=1)

if __name__ == "__main__":
    gui = Gui()
    
    # define the components
    top_label = TopLabel(gui)
    navigation = Navigation(gui)

    # create the gui
    gui.mainloop()