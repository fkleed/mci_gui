import tkinter as tk

# crate the root window
root = tk.Tk()
root.title("MCI Chat")

window_width = 1200
window_height = 600

root.geometry(f'{window_width}x{window_height}')
root.minsize(1200, 600)
root.iconbitmap("./assets/images/favicon.ico")
root.configure(bg="white")

# specify the layout of root frame
root.columnconfigure(0, weight=1)
root.columnconfigure(1, weight=3)
root.rowconfigure(0, weight=0)
root.rowconfigure(1, weight=1)


# creating the top label for the apoplication
top_label = tk.Label(root, text="MCI Chat", bg="#131A1C", fg="#AFCA0B", pady=10)
top_label.configure(font=("Open Sans", 24, "bold"))


# creating frame to display navigation
frm_navigation = tk.Frame(root, relief=tk.RIDGE, bd=2)
frm_navigation.columnconfigure(0, weight=1)
frm_navigation.rowconfigure(0, weight=1)
frm_navigation.rowconfigure (1, weight=0)

# preview important messages

# creating the all messages and new message button
frm_buttons = tk.Frame(frm_navigation, bg="#131A1C")

btn_all_messages = tk.Button(frm_buttons, text="All messages", bg="#AFCA0B", fg="#131A1C")
btn_all_messages.configure(font=("Open Sans", 12, "bold"))
btn_all_messages.pack(side=tk.LEFT, expand=tk.TRUE, fill=tk.BOTH, padx=(10,5), pady=10)

btn_new_message = tk.Button(frm_buttons, text="New message", bg="#AFCA0B", fg="#131A1C")
btn_new_message.configure(font=("Open Sans", 12, "bold"))
btn_new_message.pack(side=tk.LEFT, expand=tk.TRUE, fill=tk.BOTH, padx=(5,10), pady=10)


# creating frame for answering / sending messages


# creating the gui
top_label.grid(column=0, columnspan=2, row=0, sticky="ew")
frm_navigation.grid(column=0, row=1, sticky="nsew")
frm_buttons.grid(column=0, row=1, sticky="ew")

# run the gui
root.mainloop()
