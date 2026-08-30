n = 4

guess = input("Total points: 1 + 2 + 3 + 4 = ")

input("Formula: one calculation. Press Enter to run ")
total = n * (n + 1) // 2
print(" Total =", total, " step = 1")

input("Loop: add one student at a time. Press Enter to run ")
total = 0
for student in range(1, n + 1):
    total += student
print(" Total =", total, " step =", n)

input("Double loop: counts every single point. Press Enter to run")
total = 0
step = 0
for student in range (1, n + 1):
    for point in range(1, student + 1):
        total += 1
        step += 1
print(" total =", total, " step =", step, " your guess was: guess")

    