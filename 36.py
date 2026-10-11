```python
# MY TRAIN SEAT FINDER
# Topic: Time and Space Complexity

# Sorted list of available train seat numbers
seats = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]


# METHOD 1: ITERATIVE BINARY SEARCH
def iterative_binary_search(seats, target):
    low = 0
    high = len(seats) - 1
    steps = 0

    while low <= high:
        steps += 1
        mid = (low + high) // 2

        if seats[mid] == target:
            return mid, steps

        elif seats[mid] < target:
            low = mid + 1

        else:
            high = mid - 1

    return -1, steps


# METHOD 2: RECURSIVE BINARY SEARCH
def recursive_binary_search(seats, target, low, high, steps=0):
    if low > high:
        return -1, steps

    steps += 1
    mid = (low + high) // 2

    if seats[mid] == target:
        return mid, steps

    elif seats[mid] < target:
        return recursive_binary_search(
            seats, target, mid + 1, high, steps
        )

    else:
        return recursive_binary_search(
            seats, target, low, mid - 1, steps
        )


# MAIN PROGRAM
print("================================")
print("      MY TRAIN SEAT FINDER")
print("================================")

print("Available seats:", seats)

try:
    target = int(input("Enter the seat number you want to find: "))

    # Iterative search
    index1, steps1 = iterative_binary_search(seats, target)

    print("\n--- ITERATIVE BINARY SEARCH ---")

    if index1 != -1:
        print("Seat found:", target)
        print("Position in list:", index1)
    else:
        print("Seat not found.")

    print("Number of steps:", steps1)

    # Recursive search
    index2, steps2 = recursive_binary_search(
        seats, target, 0, len(seats) - 1
    )

    print("\n--- RECURSIVE BINARY SEARCH ---")

    if index2 != -1:
        print("Seat found:", target)
        print("Position in list:", index2)
    else:
        print("Seat not found.")

    print("Number of steps:", steps2)

except ValueError:
    print("Invalid input! Please enter a whole number.")
```
