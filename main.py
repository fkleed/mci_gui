import tkinter as tk
from PIL import ImageTk, Image

# create the root window
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


# create the top label for the apoplication
top_label = tk.Label(root, text="MCI Chat", bg="#131A1C", fg="#AFCA0B", pady=10)
top_label.configure(font=("Open Sans", 24, "bold"))


# create frame to display navigation
frm_navigation = tk.Frame(root, relief=tk.RIDGE, bd=2)
frm_navigation.columnconfigure(0, weight=1)
frm_navigation.rowconfigure(0, weight=1)
frm_navigation.rowconfigure (1, weight=0)

# preview important messages
frm_important_messages = tk.Frame(frm_navigation)
frm_important_messages.columnconfigure(0, weight=1)
frm_important_messages.rowconfigure(0, weight=0)
frm_important_messages.rowconfigure(1, weight=1)

# create the important message label
frm_important_messages_label = tk.Frame(frm_important_messages, bg="white")

notification_image = ImageTk.PhotoImage(Image.open("./assets/images/notification.png"))
important_messages_label_image = tk.Label(frm_important_messages_label, image=notification_image, bg="white")
important_messages_label_image.pack(side=tk.LEFT, padx=(10,5), pady=10)

important_message_label_text = tk.Label(frm_important_messages_label, text="Imortant messages (3)", bg="white")
important_message_label_text.configure(font=("Open Sans", 12, "bold"))
important_message_label_text.pack(side=tk.LEFT, padx=(5,10), pady=10)

frm_important_messages_label.grid(column=0, row=0, sticky="ew")

# create the important messages to display
frm_important_messages_to_display = tk.Frame(frm_important_messages, bg="white")

# create a message to display
frm_message = tk.Frame(frm_important_messages_to_display, highlightbackground="#AFCA0B", highlightthickness=2)
message_sender = tk.Label(frm_message, text="Thomas Müller", anchor=tk.W, bg="white")
message_sender.configure(font=("Open Sans", 10, "bold"))
message_sender.pack(side=tk.TOP, fill=tk.X)

message_content_preview = tk.Label(frm_message, text="Lorem ipsum...", anchor=tk.W, bg="white")
message_content_preview.configure(font=("Open Sans", 10))
message_content_preview.pack(side=tk.TOP, fill=tk.X)

frm_message_2 = tk.Frame(frm_important_messages_to_display, highlightbackground="#131A1C", highlightthickness=2)
message_sender = tk.Label(frm_message_2, text="Mats Hummels", anchor=tk.W, bg="white")
message_sender.configure(font=("Open Sans", 10, "bold"))
message_sender.pack(side=tk.TOP, fill=tk.X)

message_content_preview = tk.Label(frm_message_2, text="Lorem ipsum...", anchor=tk.W, bg="white")
message_content_preview.configure(font=("Open Sans", 10))
message_content_preview.pack(side=tk.TOP, fill=tk.X)

frm_message_3 = tk.Frame(frm_important_messages_to_display, highlightbackground="#131A1C", highlightthickness=2)
message_sender = tk.Label(frm_message_3, text="Timo Werner", anchor=tk.W, bg="white")
message_sender.configure(font=("Open Sans", 10, "bold"))
message_sender.pack(side=tk.TOP, fill=tk.X)

message_content_preview = tk.Label(frm_message_3, text="Lorem ipsum...", anchor=tk.W, bg="white")
message_content_preview.configure(font=("Open Sans", 10))
message_content_preview.pack(side=tk.TOP, fill=tk.X)



frm_message.pack(side=tk.TOP, fill=tk.X, padx=10, pady=10)
frm_message_2.pack(side=tk.TOP, fill=tk.X, padx=10, pady=10)
frm_message_3.pack(side=tk.TOP, fill=tk.X, padx=10, pady=10)

frm_important_messages_to_display.grid(column=0, row=1, sticky="nsew")

# create the all messages and new message button
frm_buttons = tk.Frame(frm_navigation, bg="#131A1C")

btn_all_messages = tk.Button(frm_buttons, text="All messages", bg="#AFCA0B", fg="#131A1C")
btn_all_messages.configure(font=("Open Sans", 12, "bold"))
btn_all_messages.pack(side=tk.LEFT, expand=tk.TRUE, fill=tk.BOTH, padx=(10,5), pady=10)

btn_new_message = tk.Button(frm_buttons, text="New message", bg="#AFCA0B", fg="#131A1C")
btn_new_message.configure(font=("Open Sans", 12, "bold"))
btn_new_message.pack(side=tk.LEFT, expand=tk.TRUE, fill=tk.BOTH, padx=(5,10), pady=10)


# create for interacting with the message detail
frm_detail_display = tk.Frame(root, relief=tk.RIDGE, bd=2, bg="white")


# create the gui
top_label.grid(column=0, columnspan=2, row=0, sticky="ew")

frm_navigation.grid(column=0, row=1, sticky="nsew")
frm_important_messages.grid(column=0, row=0, sticky="nsew")
frm_buttons.grid(column=0, row=1, sticky="ew")

frm_detail_display.grid(column=1, row=1, sticky="nsew")

# run the gui
root.mainloop()
