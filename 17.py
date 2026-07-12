# Robot Introduction using OOP

class Robot:

    # Constructor
    def __init__(self, name, model, purpose):
        self.name = name
        self.model = model
        self.purpose = purpose
        print("Robot has been created successfully!\n")

    # Method to introduce the robot
    def introduce(self):
        print("----- ROBOT INTRODUCTION -----")
        print(f"My name is {self.name}.")
        print(f"My model is {self.model}.")
        print(f"My purpose is {self.purpose}.")
        print("I am happy to assist you!")

    # Destructor
    def __del__(self):
        print("\nRobot object has been deleted.")
        print("Goodbye!")

# Main Program
robot1 = Robot("RoboMax", "RX-2026", "Helping people with daily tasks")

robot1.introduce()

# Delete the object
del robot1