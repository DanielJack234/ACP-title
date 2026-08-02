# Shopping List Manager using Python File Handling

filename = "shopping_list.txt"

# Step 1: Create a text file and write a shopping list into it
shopping_items = ["Rice", "Milk", "Bread", "Eggs", "Sugar"]

with open(filename, "w") as file:
    for item in shopping_items:
        file.write(item + "\n")

print("Shopping list has been created.\n")

# Step 2: Read the complete file
print("Current Shopping List:")
with open(filename, "r") as file:
    print(file.read())

# Step 3: Append new items
new_items = ["Butter", "Soap", "Juice"]

with open(filename, "a") as file:
    for item in new_items:
        file.write(item + "\n")

print("New items have been added.\n")

# Step 4: Read the updated file line by line
print("Updated Shopping List:")
with open(filename, "r") as file:
    for line in file:
        print(line.strip())