from abc import ABC, abstractmethod

# Abstract Parent Class
class Instrument(ABC):
    def __init__(self, name):
        self.name = name

    # Abstract method
    @abstractmethod
    def play_sound(self):
        pass


# Child Class 1
class Guitar(Instrument):
    def __init__(self, name):
        super().__init__(name)

    def play_sound(self):
        print(f"{self.name}: Strum Strum!")


# Child Class 2
class Piano(Instrument):
    def __init__(self, name):
        super().__init__(name)

    def play_sound(self):
        print(f"{self.name}: Ding Ding!")


# Child Class 3
class Drum(Instrument):
    def __init__(self, name):
        super().__init__(name)

    def play_sound(self):
        print(f"{self.name}: Boom Boom!")


# Creating objects
guitar = Guitar("Acoustic Guitar")
piano = Piano("Grand Piano")
drum = Drum("Bass Drum")

# List of instruments
instruments = [guitar, piano, drum]

# Music Instrument Sound Show
print("====== MUSIC INSTRUMENT SOUND SHOW ======")

for instrument in instruments:
    instrument.play_sound()