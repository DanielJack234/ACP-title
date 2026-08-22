import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk


# Create the main window
root = tk.Tk()
root.title("My Photo Album")
root.geometry("600x600")
root.resizable(False, False)


# Load the image
image = Image.open("photo.jpg")
image = image.resize((400, 350))
photo = ImageTk.PhotoImage(image)


# Title
title_label = tk.Label(
    root,
    text="My Photo Album",
    font=("Arial", 24, "bold")
)
title_label.pack(pady=15)


# Display the photo
image_label = tk.Label(root, image=photo)
image_label.pack(pady=10)


# Function for the messagebox
def show_message():
    messagebox.showinfo(
        "Photo Album",
        "Welcome to my photo album!"
    )


# Function to open photo details
def show_details():
    details_window = tk.Toplevel(root)
    details_window.title("Photo Details")
    details_window.geometry("350x250")
    details_window.resizable(False, False)

    tk.Label(
        details_window,
        text="Photo Details",
        font=("Arial", 18, "bold")
    ).pack(pady=15)

    tk.Label(
        details_window,
        text="File Name: photo.jpg",
        font=("Arial", 12)
    ).pack(pady=5)

    tk.Label(
        details_window,
        text="Photo Album: My Photo Album",
        font=("Arial", 12)
    ).pack(pady=5)

    tk.Label(
        details_window,
        text="This photo is displayed using Pillow.",
        font=("Arial", 11)
    ).pack(pady=10)

    tk.Button(
        details_window,
        text="Close",
        command=details_window.destroy
    ).pack(pady=10)


# Buttons
button_frame = tk.Frame(root)
button_frame.pack(pady=15)

welcome_button = tk.Button(
    button_frame,
    text="Show Message",
    command=show_message,
    width=15
)
welcome_button.grid(row=0, column=0, padx=10)

details_button = tk.Button(
    button_frame,
    text="Photo Details",
    command=show_details,
    width=15
)
details_button.grid(row=0, column=1, padx=10)


# Start the application
root.mainloop()