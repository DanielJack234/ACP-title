```python
# MY QUIZ RESULT SEARCHER
# Topic: Asymptotic Analysis and Big-O Notation

scores = [45, 78, 90, 65, 78, 88, 56, 90, 72, 60]


# 1. DIRECT ACCESS - O(1)
def direct_access(scores, position):
    if 0 <= position < len(scores):
        return scores[position]
    return None


# 2. LINEAR SEARCH - O(n)
def linear_search(scores, target):
    steps = 0

    for i in range(len(scores)):
        steps += 1

        if scores[i] == target:
            return i, steps

    return -1, steps


# 3. PAIR COMPARISON - O(n^2)
def pair_comparison(scores):
    comparisons = 0
    matching_pairs = []

    for i in range(len(scores)):
        for j in range(i + 1, len(scores)):
            comparisons += 1

            if scores[i] == scores[j]:
                matching_pairs.append(
                    (scores[i], i, j)
                )

    return matching_pairs, comparisons


# MAIN PROGRAM
print("====================================")
print("       MY QUIZ RESULT SEARCHER")
print("====================================")

print("Quiz Scores:", scores)

# Direct Access
try:
    position = int(
        input("\nEnter a position to view its score (0-9): ")
    )

    result = direct_access(scores, position)

    if result is not None:
        print("Direct Access Result:", result)
        print("Time Complexity: O(1)")
    else:
        print("Invalid position!")

    # Linear Search
    target = int(input("\nEnter a score to search for: "))

    index, steps = linear_search(scores, target)

    if index != -1:
        print("Score Found:", target)
        print("Position:", index)
    else:
        print("Score not found.")

    print("Number of comparisons:", steps)
    print("Time Complexity: O(n)")

    # Pair Comparison
    pairs, comparisons = pair_comparison(scores)

    print("\n--- PAIR COMPARISON ---")

    if pairs:
        for score, first, second in pairs:
            print(
                f"Score {score} appears at positions "
                f"{first} and {second}"
            )
    else:
        print("No duplicate scores found.")

    print("Total Pair Comparisons:", comparisons)
    print("Time Complexity: O(n^2)")

    # COMPLEXITY ANALYSIS
    print("\n--- COMPLEXITY ANALYSIS ---")

    print("Direct Access:")
    print("Best Case: O(1)")
    print("Average Case: O(1)")
    print("Worst Case: O(1)")
    print("Space Complexity: O(1)")

    print("\nLinear Search:")
    print("Best Case: O(1)")
    print("Average Case: O(n)")
    print("Worst Case: O(n)")
    print("Space Complexity: O(1)")

    print("\nPair Comparison:")
    print("Best Case: O(n^2)")
    print("Average Case: O(n^2)")
    print("Worst Case: O(n^2)")
    print("Space Complexity: O(n)")

    # BIG-O, OMEGA, AND THETA
    print("\n--- ASYMPTOTIC NOTATION ---")

    print("Big-O (O): Upper bound")
    print("Omega (Ω): Lower bound")
    print("Theta (Θ): Tight bound")

    print("\n--- COMPLEXITY LADDER ---")

    print("O(1)     - Constant")
    print("O(log n) - Logarithmic")
    print("O(n)     - Linear")
    print("O(n log n) - Linearithmic")
    print("O(n^2)   - Quadratic")
    print("O(2^n)   - Exponential")
    print("O(n!)    - Factorial")

    print("\nMost efficient for known positions: Direct Access")
    print("Suitable for searching scores: Linear Search")
    print("Useful for finding matching pairs: Pair Comparison")

except ValueError:
    print("Invalid input! Please enter a whole number.")
```
