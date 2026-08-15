from tkinter import * 

window = Tk()
window.title("My Profile Card")
window.geometry("400x380")

title = Label(window, text="My Profile Card", fg="white", bg="purple", width=40)
title.grid(row=0, column=0, columnspan=2, padx=10)

name_label = Label(window, text="Name:", fg="black", bg="lightblue")
name_label.grid(row=1, column=0, padx=10, pady=10)

name_entry = Entry(window, fg="black", bg="lightyellow", width=30)
name_entry.grid(row=1, column=1, padx=10, pady=5)

hobby_label = Label(window, text="Hobby:", fg="black", bg="lightblue")
hobby_label.grid(row=2, column=0, padx=10, pady=10)

hobby_entry = Entry(window, fg="black", bg="lightyellow", width=30) 
hobby_entry.grid(row=2, column=1, padx=10, pady=5)


about_frame = Frame(window, relief=RAISED, borderwidth=3)
about_frame.grid(row=3, column=0, columnspan=2, padx=10, pady=10)

about_label = Label(about_frame, text="About Me:")
about_label.pack()

about_text = Text(about_frame, fg="black", bg="lightyellow", width=30, height=5)
about_text.pack()

sumbit = Button(window, text="Submit", fg="white", bg="green", width=20)
sumbit.grid(row=4, column=0, columnspan=2, padx=10, pady=10)

window.mainloop()
