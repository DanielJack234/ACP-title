# Program to Find All Two-Digit Prime Numbers

print("All two-digit prime numbers are:")

for num in range(10, 100):
    is_prime = True

    for i in range(2, num):
        if num % i == 0:
            is_prime = False
            break

    if is_prime:
        print(num, end=" ")

print()