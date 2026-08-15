# Study Notes Organizer
# Python File Handling Assignment

# 1. Create two subject notes files
with open("math_notes.txt", "w") as file:
    file.write("Mathematics is the study of numbers, shapes, and patterns.\n")
    file.write("Algebra uses letters and symbols to represent numbers.\n")
    file.write("Geometry deals with shapes, sizes, and measurements.\n")

with open("computer_notes.txt", "w") as file:
    file.write("Computer science is the study of computers and computing.\n")
    file.write("Python is a popular programming language.\n")
    file.write("File handling allows programs to store and retrieve information.\n")


# 2. Read the files safely using with open()
print("MATHEMATICS NOTES")
with open("math_notes.txt", "r") as file:
    math_notes = file.read()
    print(math_notes)

print("COMPUTER SCIENCE NOTES")
with open("computer_notes.txt", "r") as file:
    computer_notes = file.read()
    print(computer_notes)


# 3. Count the words using split()
math_word_count = len(math_notes.split())
computer_word_count = len(computer_notes.split())

print("Number of words in Mathematics notes:", math_word_count)
print("Number of words in Computer Science notes:", computer_word_count)


# 4. Check whether the merged file already exists
import os

merged_file = "study_notes.txt"

if os.path.exists(merged_file):
    print("\nOld merged file found. Removing it...")
    os.remove(merged_file)
else:
    print("\nNo old merged file found.")


# 5. Merge the two files into one organized study notes file
with open(merged_file, "w") as file:
    file.write("========== STUDY NOTES ==========\n\n")

    file.write("========== MATHEMATICS ==========\n")
    with open("math_notes.txt", "r") as math_file:
        file.write(math_file.read())

    file.write("\n========== COMPUTER SCIENCE ==========\n")
    with open("computer_notes.txt", "r") as computer_file:
        file.write(computer_file.read())


# 6. Read and display the final merged file
print("\n========== MERGED STUDY NOTES ==========\n")

with open(merged_file, "r") as file:
    print(file.read())

print("Study notes successfully organized!")