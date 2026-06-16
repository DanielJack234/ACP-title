# Program to check if a number is an Armstrong number

num = int(input("Enter a number: "))

original_num = num
num_digits = len(str(num))
sum_of_powers = 0

# Calculate the sum of each digit raised to the power of number of digits
temp = num
while temp > 0:
    digit = temp % 10
    sum_of_powers += digit ** num_digits
    temp //= 10

# Check if it is an Armstrong number
if sum_of_powers == original_num:
    print(original_num, "is an Armstrong number.")
else:
    print(original_num, "is not an Armstrong number.")