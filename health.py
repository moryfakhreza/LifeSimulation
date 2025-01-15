import random

def visit_doctor(character):
    cost = 200
    if character.money >= cost:
        character.money -= cost
        health_gain = random.randint(10, 20)
        character.health += health_gain
        print(f"You visited the doctor and gained {health_gain} health points.")
    else:
        print("You don't have enough money to visit the doctor.")

def plastic_surgery(character):
    cost = 500
    if character.money >= cost:
        character.money -= cost
        appearance_gain = random.randint(10, 20)
        character.appearance += appearance_gain
        print(f"You had plastic surgery and gained {appearance_gain} appearance points.")
    else:
        print("You don't have enough money for plastic surgery.")