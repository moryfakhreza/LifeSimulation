import random

class Character:
    def __init__(self, name, age=0, country=None, gender=None):
        self.name = name
        self.age = age
        self.country = country if country else self.random_country()
        self.gender = gender if gender else self.random_gender()
        self.happiness = random.randint(40, 60)
        self.health = random.randint(40, 60)
        self.intelligence = random.randint(40, 60)
        self.appearance = random.randint(40, 60)
        self.money = 1000
        self.assets = []
        self.alive = True

    def random_country(self):
        countries = [
            "USA", "UK", "Canada", "Australia", "Germany",
            "France", "Italy", "Spain", "Japan", "China",
            "India", "Brazil", "Russia", "Mexico", "South Korea",
            "South Africa", "Argentina", "New Zealand", "Sweden", "Norway",
            "Netherlands", "Belgium", "Switzerland", "Austria", "Denmark",
            "Finland", "Ireland", "Portugal", "Greece", "Turkey",
            "Saudi Arabia", "United Arab Emirates", "Israel", "Egypt", "Nigeria",
            "Kenya", "Indonesia", "Malaysia", "Singapore", "Thailand"
        ]
        return random.choice(countries)

    def random_gender(self):
        return random.choice(["Male", "Female"])

    def display_status(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Country: {self.country}")
        print(f"Gender: {self.gender}")
        print(f"Happiness: {self.happiness}")
        print(f"Health: {self.health}")
        print(f"Intelligence: {self.intelligence}")
        print(f"Appearance: {self.appearance}")
        print(f"Money: ${self.money}")
        print(f"Assets: {', '.join(self.assets) if self.assets else 'None'}")

    def age_up(self):
        self.age += 1
        self.happiness = max(0, self.happiness - 1)
        self.health = max(0, self.health - 1)
        self.intelligence += 1
        print(f"Happy Birthday! You are now {self.age} years old.")
        if self.health <= 0:
            self.alive = False
            print(f"{self.name} has passed away due to poor health.")