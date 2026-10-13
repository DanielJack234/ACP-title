```python
# My Secret Code Bit Scanner

print("===== MY SECRET CODE BIT SCANNER =====")

# Enter secret code and access key
secret_code = int(input("Enter your secret code: "))
access_key = int(input("Enter your access key: "))

# Display binary representation
print("\nBinary Representation")
print("Secret Code:", bin(secret_code))
print("Access Key:", bin(access_key))

# Bitwise AND
print("\nBitwise AND")
print("Result:", secret_code & access_key)

# Bitwise OR
print("\nBitwise OR")
print("Result:", secret_code | access_key)

# Bitwise XOR
print("\nBitwise XOR")
print("Result:", secret_code ^ access_key)

# Bitwise NOT
print("\nBitwise NOT")
print("Flipped Secret Code:", ~secret_code)
print("Flipped Access Key:", ~access_key)

# Left shift
print("\nLeft Shift")
print("Secret Code:", secret_code << 1)
print("Access Key:", access_key << 1)

# Right shift
print("\nRight Shift")
print("Secret Code:", secret_code >> 1)
print("Access Key:", access_key >> 1)

# Count the number of 1 bits
print("\nCount Set Bits")
print("Secret Code:", bin(secret_code).count("1"))
print("Access Key:", bin(access_key).count("1"))

# Compare secret code and access key
print("\nAccess Check")
if secret_code == access_key:
    print("Access Granted!")
else:
    print("Access Denied!")

print("\nScanning Completed!")
```
