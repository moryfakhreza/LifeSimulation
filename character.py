# character.py
class Character:
    def __init__(self, name, age=0):
        self.name = name
        self.age = age
        self.happiness = 50
        self.health = 50
        self.intelligence = 50
        self.money = 1000

    def display_status(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Happiness: {self.happiness}")
        print(f"Health: {self.health}")
        print(f"Intelligence: {self.intelligence}")
        print(f"Money: ${self.money}")

    def age_up(self):
        self.age += 1
        self.happiness -= 1
        self.health -= 1
        self.intelligence += 1
        print(f"Happy Birthday! You are now {self.age} years old.")