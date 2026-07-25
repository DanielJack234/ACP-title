# Parent Class
class Pet:
    def __init__(self, name, age, health):
        self.name = name
        self.age = age
        self.__health = health   # Private attribute (Encapsulation)

    # Getter method
    def get_health(self):
        return self.__health

    # Setter method
    def set_health(self, new_health):
        if 0 <= new_health <= 100:
            self.__health = new_health
        else:
            print("Health must be between 0 and 100.")

    # Method to be overridden
    def pet_info(self):
        print(f"{self.name} is {self.age} years old.")


# Child Class Dog
class Dog(Pet):
    def pet_info(self):
        print(f"Dog: {self.name}, Age: {self.age}, Health: {self.get_health()}%")


# Child Class Cat
class Cat(Pet):
    def pet_info(self):
        print(f"Cat: {self.name}, Age: {self.age}, Health: {self.get_health()}%")


# Child Class Bird
class Bird(Pet):
    def pet_info(self):
        print(f"Bird: {self.name}, Age: {self.age}, Health: {self.get_health()}%")


# Creating Objects
dog = Dog("Buddy", 4, 90)
cat = Cat("Kitty", 2, 85)
bird = Bird("Tweety", 1, 95)

# Updating health using setter method
dog.set_health(92)
cat.set_health(88)
bird.set_health(97)

# List of pet objects
pets = [dog, cat, bird]

# Demonstrating Polymorphism using a loop
print("====== PET CARE DASHBOARD ======")

for pet in pets:
    pet.pet_info()

print("\nUpdated Health Records")
print("------------------------")
print("Dog Health :", dog.get_health(), "%")
print("Cat Health :", cat.get_health(), "%")
print("Bird Health:", bird.get_health(), "%")