import datetime
import calendar

city = input("Enter your city name:")
temp = float(input("Enter today's temperature in celsius:"))
now = datetime.datetime.now()

print("Current date and time:", now)

print("City:", city)
print(calendar.calendar(now.year))


# PART 1 - USER INPUT 


# PART 2 - IF STATEMENT
if temp > 35:
    print("Warning: It is very hot today! ")

    # PART 3 - if-else
    if temp > 25:   
        print("Great day to go outside")
    else:
        print("Grab a jacket before you go out!")

        # PART 4 - if-elif-else
        if temp > 35:
            print("Weather: Scoring Hot")
        elif temp > 25:
            print("Weather: Warm and Sunny")
        elif temp > 15:
            print("Weather: Cool and Breezy")
        else:
            print("Weather: Cold - stay warm!")
        





