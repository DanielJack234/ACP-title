```python
# My Train Seat Finder
# Topic: Analysis and Space Complexity

# Sorted list of available train seat numbers
seats = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50]


# 1. ITERATIVE BINARY SEARCH
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


# 2. RECURSIVE BINARY SEARCH
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


# 3. MAIN PROGRAM
print("====================================")
print("       MY TRAIN SEAT FINDER")
print("====================================")

print("Available train seats:", seats)

try:
    target = int(input("Enter the seat number you want to find: "))

    # Iterative search
    index1, steps1 = iterative_binary_search(seats, target)

    print("\n--- ITERATIVE BINARY SEARCH ---")

    if index1 != -1:
        print("Seat found:", seats[index1])
        print("Position in list:", index1 + 1)
    else:
        print("Seat not found.")

    print("Number of steps:", steps1)
    print("Time Complexity: O(log n)")
    print("Space Complexity: O(1)")
    print("Call Stack: No recursive calls")

    # Recursive search
    index2, steps2 = recursive_binary_search(
        seats, target, 0, len(seats) - 1
    )

    print("\n--- RECURSIVE BINARY SEARCH ---")

    if index2 != -1:
        print("Seat found:", seats[index2])
        print("Position in list:", index2 + 1)
    else:
        print("Seat not found.")

    print("Number of steps:", steps2)
    print("Time Complexity: O(log n)")
    print("Space Complexity: O(log n)")
    print("Call Stack: Uses recursive function calls")

    # Complexity comparison
    print("\n====================================")
    print("       COMPLEXITY COMPARISON")
    print("====================================")

    print("Iterative Binary Search:")
    print("Time: O(log n), Space: O(1)")

    print("\nRecursive Binary Search:")
    print("Time: O(log n), Space: O(log n)")

    print("\nComplexity Ladder (lower to higher):")
    print("1. O(1)       - Constant")
    print("2. O(log n)   - Logarithmic")
    print("3. O(n)       - Linear")
    print("4. O(n log n) - Linearithmic")
    print("5. O(n^2)     - Quadratic")
    print("6. O(2^n)     - Exponential")
    print("7. O(n!)      - Factorial")

except ValueError:
    print("Invalid input! Please enter a valid seat number.")
```
