import tkinter as tk
from tkinter import messagebox

# Create the main window
root = tk.Tk()
root.title("Personal Bio Form")
root.geometry("500x500")
root.resizable(False, False)

# Heading
title_label = tk.Label(
    root,
    text="Personal Bio Form",
    font=("Arial", 22, "bold")
)
title_label.pack(pady=20)

# Create the form frame
form_frame = tk.Frame(root)
form_frame.pack(pady=10)

# Name
tk.Label(form_frame, text="Full Name:", font=("Arial", 12)).grid(
    row=0, column=0, padx=10, pady=10, sticky="w"
)
name_entry = tk.Entry(form_frame, width=30)
name_entry.grid(row=0, column=1, padx=10, pady=10)

# Age
tk.Label(form_frame, text="Age:", font=("Arial", 12)).grid(
    row=1, column=0, padx=10, pady=10, sticky="w"
)
age_entry = tk.Entry(form_frame, width=30)
age_entry.grid(row=1, column=1, padx=10, pady=10)

# Email
tk.Label(form_frame, text="Email:", font=("Arial", 12)).grid(
    row=2, column=0, padx=10, pady=10, sticky="w"
)
email_entry = tk.Entry(form_frame, width=30)
email_entry.grid(row=2, column=1, padx=10, pady=10)

# Hobbies
tk.Label(form_frame, text="Hobbies:", font=("Arial", 12)).grid(
    row=3, column=0, padx=10, pady=10, sticky="w"
)
hobbies_entry = tk.Entry(form_frame, width=30)
hobbies_entry.grid(row=3, column=1, padx=10, pady=10)

# About yourself
tk.Label(form_frame, text="About Me:", font=("Arial", 12)).grid(
    row=4, column=0, padx=10, pady=10, sticky="nw"
)

about_text = tk.Text(form_frame, width=30, height=5)
about_text.grid(row=4, column=1, padx=10, pady=10)


# Function to display the bio
def display_bio():
    name = name_entry.get()
    age = age_entry.get()
    email = email_entry.get()
    hobbies = hobbies_entry.get()
    about = about_text.get("1.0", tk.END).strip()

    # Check if fields are empty
    if not name or not age or not email or not hobbies or not about:
        messagebox.showwarning(
            "Missing Information",
            "Please fill in all the fields."
        )
        return

    bio = f"""
Personal Bio

Name: {name}
Age: {age}
Email: {email}
Hobbies: {hobbies}

About Me:
{about}
"""

    messagebox.showinfo("My Personal Bio", bio)


# Submit button
submit_button = tk.Button(
    root,
    text="Display My Bio",
    command=display_bio,
    font=("Arial", 12, "bold"),
    width=20
)
submit_button.pack(pady=20)

# Run the application
root.mainloop()