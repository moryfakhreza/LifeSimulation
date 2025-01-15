import random

class Relationship:
    def __init__(self, name, relation_type):
        self.name = name
        self.relation_type = relation_type
        self.happiness = random.randint(40, 60)

    def interact(self):
        print(f"You interact with your {self.relation_type} {self.name}.")
        self.happiness += random.randint(-5, 10)
        print(f"Your relationship happiness with {self.name} is now {self.happiness}.")