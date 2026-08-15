# Smart Notes Organizer
# Python File Handling

# 1. Create a sample notes file
with open("notes.txt", "w") as file:
    file.write("Python is a programming language.\n")
    file.write("File handling allows us to work with files.\n")
    file.write("Python can read and write text files.\n")
    file.write("Loops are useful for processing data.\n")
    file.write("Functions help organize Python programs.\n")
    file.write("File handling is important in programming.\n")


# 2. Preview file content using read(n)
print("===== FILE PREVIEW =====")

with open("notes.txt", "r") as file:
    preview = file.read(50)
    print(preview)


# 3. Read all lines using readlines()
print("\n===== ALL LINES =====")

with open("notes.txt", "r") as file:
    lines = file.readlines()

for line in lines:
    print(line.strip())


# 4. Loop through the file line by line
print("\n===== FILE LINE BY LINE =====")

with open("notes.txt", "r") as file:
    for line in file:
        print(line.strip())


# 5. Filter lines containing the word "Python"
print("\n===== FILTERED NOTES =====")

selected_lines = []

with open("notes.txt", "r") as file:
    for line in file:
        if "Python" in line:
            print(line.strip())
            selected_lines.append(line)


# 6. Copy selected lines into a new file
with open("selected_notes.txt", "w") as file:
    for line in selected_lines:
        file.write(line)


# 7. Display the new file
print("\n===== SELECTED NOTES FILE =====")

with open("selected_notes.txt", "r") as file:
    print(file.read())

print("Selected notes have been copied successfully!")