# My School Subject Planner

# Student details stored in a tuple
student = ("Daniel Jack", "CSC101", "100 Level")

# Accessing tuple values
print("=== Student Details ===")
print("Name:", student[0])
print("Department:", student[1])
print("Level:", student[2])

# Subject sets for different days
monday = {"Mathematics", "English", "Physics", "Computer Science"}
tuesday = {"English", "Chemistry", "Computer Science", "Biology"}

print("\nMonday Subjects:", monday)
print("Tuesday Subjects:", tuesday)

# Adding a subject to Monday
monday.add("Civic Education")

# Removing a subject from Tuesday
tuesday.remove("Biology")

print("\nAfter Modification")
print("Monday Subjects:", monday)
print("Tuesday Subjects:", tuesday)

# Set operations
print("\n=== Set Operations ===")

# Common subjects
print("Common Subjects:", monday.intersection(tuesday))

# All subjects
print("All Subjects:", monday.union(tuesday))

# Subjects only on Monday
print("Only on Monday:", monday.difference(tuesday))

# Subjects only on Tuesday
print("Only on Tuesday:", tuesday.difference(monday))
