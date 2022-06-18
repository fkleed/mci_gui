import tkinter as tk

# crate the root window
root = tk.Tk()
root.title("MCI Chat GUI")

window_width = 800
window_height = 400

root.geometry(f'{window_width}x{window_height}')
root.minsize(800, 400)
root.iconbitmap("./assets/images/favicon.ico")
root.configure(bg="white")

# specify the layout of root frame
root.columnconfigure(0, weight=0)
root.columnconfigure(1, weight=1)
root.rowconfigure(0, weight=0)
root.rowconfigure(1, weight=1)

# create the top frame label
top_label = tk.Label(root, text="MCI Chat", bg="#131A1C", fg="#AFCA0B", pady=10)
top_label.configure(font=("Open Sans", 20, "bold"))
top_label.grid(column=0, columnspan=2, row=0, sticky="we")

# create frame to display notifications

# create frame for answering / sending messages

# run the gui
root.mainloop()
