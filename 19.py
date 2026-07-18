class Cricket:
    def __init__(self, player, score):
        self.__player = player  # Private attribute
        self.__score = score    # Private attribute

    def info(self):

        print(f"cricket - Player: {self.__player}, Score: {self.__score}")

    def play(self):

       print(f"{self.__player} hits a six!")
    
    def get_score(self):

        return self.__score
    
    def set_score(self, new_score):

        if new_score >= 0:
            self.__score = new_score
            print(f"Score updated to {self.__score}")
        else:
            print("Score cannot be negative. ")

class Football:
    def __init__(self, player, score):
        self.__player = player  
        self.__score = score    

    def info(self):
        print(f"football - Player: {self.__player}, Score: {self.__score}")

    def play(self):

          print(f"{self.__player} score a goal!")
    def get_score(self):
        return self.__score
    
    def set_score(self, new_score):
        if new_score >= 0:
            self.__score = new_score
            print(f"Score updated to {self.__score}")
        else:
            print("Score cannot be negative. ")

# Create objects
cricket = Cricket("Rohit", 85)
football = Football("Arjun", 2)

#Polymorphism - same method, different behaviour 
print("=== Sport Scoreboard ===\n")
for sport in (cricket, football):
    sport.info()
    sport.play()
    print()

# Encapsulation - direct change does NOT work 
print("--- Direct change attempt ---")
cricket.__score = 999
print(f"get_score() still shows: {cricket.get_score()}")

# Setter - the only safe way to update 
print("\n--- Updating scores ---")
cricket.set_score(100)
football.set_score(3)

