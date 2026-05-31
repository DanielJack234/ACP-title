# My Travel Ticket Counter

traveler = "Daniel"
destination = "Lagos"
ticket1 = 15000
ticket2 = 20000

# Calculate total cost
total_cost = ticket1 + ticket2

# Compare ticket prices
if ticket1 > ticket2:
    print("Ticket 1 is more expensive")
else:
    print("Ticket 2 is more expensive")

# Display booking details
print("Traveler:", traveler)
print("Destination:", destination)
print("Total Cost:", total_cost)

# Swap ticket prices
ticket1, ticket2 = ticket2, ticket1

print("After swapping:")
print("Ticket 1 =", ticket1)
print("Ticket 2 =", ticket2)