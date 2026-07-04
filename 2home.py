# My Library Book Organiser

# List of books
books = ["Python Basics", "Mathematics", "English Grammar", "Physics", "Chemistry"]

print("Original Book List:")
print(books)

# Add a new book
books.append("Computer Science")
print("\nAfter Adding a Book:")
print(books)

# Remove a book
books.remove("Physics")
print("\nAfter Removing a Book:")
print(books)

# Sort the list
books.sort()
print("\nSorted Book List:")
print(books)

# Reverse the list
books.reverse()
print("\nReversed Book List:")
print(books)

# Access a book using index
print("\nFirst Book:", books[0])

# Slice the list
print("First Three Books:", books[:3])

# Dictionary of librarian details
librarian = {
    "Name": "Daniel Jack",
    "Library": "School Library",
    "Phone": "08012345678"
}

print("\nLibrarian Details:")
print(librarian)

# Add a new key-value pair
librarian["Email"] = "daniel@example.com"

# Update a value
librarian["Phone"] = "08198765432"

# Remove a key-value pair
librarian.pop("Library")

print("\nUpdated Librarian Details:")
print(librarian)

# Convert two lists into a dictionary
book_ids = [101, 102, 103, 104]
book_names = ["Python", "Math", "English", "Chemistry"]

book_directory = dict(zip(book_ids, book_names))

print("\nBook Directory:")
print(book_directory)