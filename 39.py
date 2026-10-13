# Binary Number System and Decimal Conversion
# This program converts binary numbers to decimal
# and decimal numbers to binary.

def binary_to_decimal(binary):
    decimal = 0
    power = 0

    # Read the binary number from right to left
    for digit in reversed(binary):
        decimal += int(digit) * (2 ** power)
        power += 1

    return decimal


def decimal_to_binary(decimal):
    if decimal == 0:
        return "0"

    binary = ""

    while decimal > 0:
        remainder = decimal % 2
        binary = str(remainder) + binary
        decimal = decimal // 2

    return binary


def main():
    print("====================================")
    print(" BINARY AND DECIMAL CONVERTER")
    print("====================================")

    while True:
        print("\nChoose an option:")
        print("1. Convert Binary to Decimal")
        print("2. Convert Decimal to Binary")
        print("3. Learn About Binary Numbers")
        print("4. Exit")

        choice = input("Enter your choice (1-4): ")

        if choice == "1":
            binary = input("Enter a binary number: ")

            # Check that the input contains only 0s and 1s
            if binary != "" and all(digit in "01" for digit in binary):
                decimal = binary_to_decimal(binary)

                print("\nBinary Number:", binary)
                print("Decimal Equivalent:", decimal)
            else:
                print("Invalid input! Binary numbers contain only 0 and 1.")

        elif choice == "2":
            try:
                decimal = int(input("Enter a decimal number: "))

                if decimal < 0:
                    print("Please enter a non-negative number.")
                else:
                    binary = decimal_to_binary(decimal)

                    print("\nDecimal Number:", decimal)
                    print("Binary Equivalent:", binary)

            except ValueError:
                print("Invalid input! Please enter a whole number.")

        elif choice == "3":
            print("\n--- ABOUT BINARY NUMBERS ---")
            print("1. Binary is a number system that uses only 0 and 1.")
            print("2. Computers use binary to represent and process data.")
            print("3. Each binary digit is called a bit.")
            print("4. Binary uses base 2.")
            print("5. Decimal uses base 10.")
            print("\nExample:")
            print("Binary: 1010")
            print("Decimal: 10")
            print("Calculation: (1*8) + (0*4) + (1*2) + (0*1) = 10")

        elif choice == "4":
            print("Thank you for using the converter!")
            break

        else:
            print("Invalid choice! Please select 1, 2, 3, or 4.")


if __name__ == "__main__":
    main()