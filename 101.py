from datetime import datetime

# Get current date and time
now = datetime.now()

# User inputs
name = input("Enter your name: ")
mood = input("How are you feeling today? (happy, sad, stressed, excited): ").lower()
energy = int(input("Enter your energy level (1-10): "))

# Display date and time
print("\n===== MY DAILY MOOD ADVISOR =====")
print("Current Date and Time:", now.strftime("%Y-%m-%d %H:%M:%S"))

# Personalized greeting
print(f"\nHello, {name}!")

# Mood advice using conditional statements
if mood == "happy":
    print("Great! Keep spreading positivity and enjoy your day.")
elif mood == "sad":
    print("Take some time to do something you enjoy and talk to someone you trust.")
elif mood == "stressed":
    print("Try taking short breaks, relaxing, and organizing your tasks.")
elif mood == "excited":
    print("That's wonderful! Use your enthusiasm to achieve something meaningful today.")
else:
    print("Thank you for sharing your mood. Remember to take care of yourself.")

# Energy level advice
if energy >= 8:
    print("Your energy is high! It's a great day to be productive.")
elif energy >= 5:
    print("Your energy is moderate. Pace yourself and stay focused.")
else:
    print("Your energy is low. Get some rest, drink water, and recharge.")

print("\nHave a fantastic day!")